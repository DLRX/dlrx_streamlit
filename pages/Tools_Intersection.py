import streamlit as st
import pandas as pd
from matplotlib_venn import venn2
import matplotlib.pyplot as plt

def venn_analysis(tab):
    
    count_testIsSubset = 0
    count_otherIsSubset = 0
    count_test_empty = 0
    count_other_empty = 0
    count_nothing = 0
    count_test_completed_by_other= 0
    count_other_completed_by_test = 0
    count_noIntersection = 0
    count_same = 0

    for index, row in tab.iterrows():  

        test = row[tab.columns[-2]]
        other = row[tab.columns[-1]]

        other = other.replace('|', '  ')

        other_set = set(other.split())
        test_set = set(test.split())


        if len(test_set) == 0 and len(other_set) == 0:
            count_nothing += 1
                
        elif len(test_set) == 0:
            count_test_empty += 1
                
        elif len(other_set) == 0:
            count_other_empty += 1      
            
        elif test_set == other_set:
            count_same += 1      
            
        else:
                 
            if test_set.issubset(other_set):
                count_testIsSubset += 1     

            elif other_set.issubset(test_set):
                count_otherIsSubset += 1
                    

            else:

                if len(test_set.intersection(other_set)) != 0:
                    if len(test_set) >= len(other_set):
                        count_other_completed_by_test += 1  
                     
                    elif len(other_set) > len(test_set):
                            count_test_completed_by_other += 1    
                else:
                    count_noIntersection += 1
                       
    tot = count_testIsSubset + count_otherIsSubset + count_test_empty + count_other_empty + count_nothing  + count_noIntersection + count_test_completed_by_other + count_other_completed_by_test + count_same
    sous_tot = count_testIsSubset + count_same+count_otherIsSubset + count_test_completed_by_other + count_other_completed_by_test+count_noIntersection


    labels = [
            "Subset = Test",
            "Subset = InterPro",
            "Nothing in common",
            "Similar",
            "Intersection"
        ]

    values = [
            count_testIsSubset,
            count_otherIsSubset,
            count_noIntersection,
            count_same,
            count_test_completed_by_other + count_other_completed_by_test
        ]

    
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    ax.set_title(f"Résulat comparatif de Test et de InterPro (non vide)" + " sur " + str(sous_tot) + " clusters")
    ax.legend(labels, bbox_to_anchor=(1.09, 0), loc="lower right", fontsize="small", title="Categories")
    plt.close(fig)

    result_list = [
        "#####################################################################",
        "Processing completed.",
        "#####################################################################",
        f"Number of Test is susbset of {tab.columns[-1]}: {count_testIsSubset}",
        f"Number of {tab.columns[-1]} is subset of Test: {count_otherIsSubset}",
        f"Number of Test empty: {count_test_empty}",
        f"Number of {tab.columns[-1]} empty: {count_other_empty}",
        f"Number of nothing: {count_nothing}",
        f"Number of no intersection: {count_noIntersection}",
        f"Number of Test completed by {tab.columns[-1]}: {count_test_completed_by_other}",
        f"Number of {tab.columns[-1]} completed by Test: {count_other_completed_by_test}",
        f"Number of same: {count_same}",
        "#####################################################################",
        "Résultat total :",
        f"Somme total des CK analysé {tot}",
        f"Somme total des CK analysé avec prédictions existantes {sous_tot} soit : {round((sous_tot / tot * 100),2)} %",
        "#####################################################################"
    ]
    return fig, result_list


st.markdown(
    """
    <h1 style='text-align: center;'>Focus on the Intersection</h1>
    """,
    unsafe_allow_html=True
)

done = st.session_state.get('done')
df_filtered = st.session_state.get('df_filtered') 

if not done:
    st.write("We saw that for a number of sequences, the both tools predict domain IDs.")
    st.markdown(
        """
        <h3 style='text-align: left;'>Please follow the steps in main page</h3>
        """,
        unsafe_allow_html=True
    )

if done is True:
    file = st.file_uploader("Pick a file")

    if file:
        tab = pd.read_csv(file)
        st.write('Data visualisation', tab)

        fig, result = venn_analysis(tab)

        for elm in result:
            st.write(elm)

        st.pyplot(fig)

col = st.container()
with col:
    btn = st.button("Go to Select_columns page", key="Select_columns", help="Navigate to Select_columns", type="primary")
    st.markdown('<div class="full-width-button"></div>', unsafe_allow_html=True)

if btn:
    st.switch_page("./pages/Select_columns.py")


