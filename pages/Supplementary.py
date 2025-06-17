import streamlit as st
import csv
from tqdm import tqdm
import pandas as pd
import xml.etree.ElementTree as ET


st.markdown(
    """
    <h1 style='text-align: center;'>Supplementary</h1>
    """,
    unsafe_allow_html=True
)


st.write("This page is currently currently being created... ")
st.write("Before the page creation, we propose a pipeline to mapping severals IDs such as InterPro, Pfam, GO etc. in order to compare it easier")
#if st.button("Mapping other to GO"):
#    st.markdown('[Open InterPro to GO Mapping](https://current.geneontology.org/ontology/external2go)')
        

def writter_map_interpro(map_dict, name_dict, output):
    '''Create a csv - interpro_map_id.csv
        For each intepro_id, all matching database_id
        --- arg ---
        map_dict is a dict like {key=interpro_id : value=[database, database_id, ...], ...}
        name_dict is a dict like {key= db : value=[db_id, shortname]...}
        output is the folder direction to save this csv
        -----------'''

    with open(output +"\interpro_map_id.csv", mode='w', newline='',encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([key for key,val in name_dict.items()])
        for interpro_id, entries in map_dict.items(): # entries is a list with db and dbkey associated
            for entry in entries:
                row = [interpro_id] + ["" for _ in name_dict]
                for entry in entries:
                    if entry[0] in name_dict:
                        row[list(name_dict.keys()).index(entry[0])] = entry[1]
            writer.writerow(row)

def main(input_file, output_dir):
    try:
        xml = open(input_file, "r", encoding='utf-8')
    except:
        print(' error with -i : correspond to the path of the dataset ')

    all_db = {}
    map_interpro = {}

    interpro_id = None 
    shortname = None
    name = None
    res_tag = None
    bool_tag = False
    
    context = ET.iterparse(xml, events=('start', 'end'))

    for event, elem in tqdm(context, desc="Processing XML"):
        
        if event == 'start' and elem.tag == 'interpro':
            interpro_id = elem.attrib.get('id')
            shortname = elem.attrib.get('short_name')
        
            if elem.tag not in all_db:
                all_db[elem.tag] = []
            all_db[elem.tag].append([interpro_id, shortname])

        elif event == 'start' and elem.tag == "classification":
            db = elem.attrib.get('class_type')
            dbkey = elem.attrib.get('id')
            cat = ''
            name = ''

            for child in elem:
                if child.tag == 'category':
                    cat = child.text
                elif child.tag == 'description':
                    name = child.text

            if db not in all_db:
                all_db[db] = []

            all_db[db].append([dbkey, name, cat])

            if interpro_id not in map_interpro:
                map_interpro[interpro_id] = []

            if db not in [entry[0] for entry in all_db.get('class_list', [])]:
                map_interpro[interpro_id].append([db, dbkey, cat, name])
            
        elif event == 'start' and elem.tag == 'db_xref' and bool_tag:
            if res_tag == 'member_list' or bool_tag:
                db = elem.attrib.get('db')
                dbkey = elem.attrib.get('dbkey')
                name = elem.attrib.get('name')

                if db not in all_db:
                    all_db[db] = []

                all_db[db].append([dbkey, name])

                if interpro_id not in map_interpro:
                    map_interpro[interpro_id] = []

                if db not in [entry[0] for entry in all_db.get('member_list', [])]:
                    map_interpro[interpro_id].append([db, dbkey])

        elif event == 'start' and elem.tag == 'db_xref' and elem.attrib.get('db') == 'EC':
            if 'EC' not in all_db:
                all_db['EC'] = []
            all_db['EC'].append([elem.attrib.get('dbkey'), elem.attrib.get('name', '')])

            if interpro_id not in map_interpro:
                map_interpro[interpro_id] = []

            if db not in [entry[0] for entry in all_db.get('external_doc_list', [])]:
                map_interpro[interpro_id].append([db, dbkey])
        
        elif event == 'start' and elem.tag == 'member_list':
            res_tag = 'member_list'
            bool_tag = True

        elif event == 'end' and elem.tag == 'member_list':
            res_tag = None
            bool_tag = False

    writter_map_interpro(map_interpro, all_db, output_dir)
    return all_db


option = st.selectbox(
     'Select your task',
     ('InterPro parser', 'FDR'))

if option == 'InterPro parser':
    file = st.text_input("Entrez le chemin d'accès du fichier (.xml & without "")")
    if file:
        op = st.text_input("Entrer le chemin ou sera sauvegardé le parsage du fichier xml")
        if op:
            st.write(main(file, op))

if option == 'FDR':
    st.write('Fasle Discovery Rate')
    file = st.file_uploader("Pick a file")

    if file:
        df = pd.read_csv(file)
        st.write('Data visualisation', df)