import streamlit as st
import pandas as pd


done = False
st.session_state['done'] = done

st.markdown(
    """
    <h1 style='text-align: center;'> CompTkit : Comparaison Tool Kit</h1>
    """,
    unsafe_allow_html=True
)
st.image("img/logo.svg", use_container_width=True)

import importlib.util
st.write('pandas dispo ?', importlib.util.find_spec("pandas") is not None)
st.write('tqdm dispo ?', importlib.util.find_spec("tqdm") is not None)
st.write('matplotlib_venn dispo ?', importlib.util.find_spec("matplotlib_venn") is not None)
st.write('xml.etree.ElementTree dispo ?', importlib.util.find_spec("xml.etree.ElementTree") is not None)
st.write('streamlit dispo ?', importlib.util.find_spec("streamlit") is not None)
st.write('numpy dispo ?', importlib.util.find_spec("numpy") is not None)
st.write('matplotlib dispo ?', importlib.util.find_spec("matplotlib") is not None)
st.markdown("**Welcome on site!** here we can explore your data and compare two columns on a csv file")
st.markdown("*How does it work?* - here your are on the main page, you can choose a button to go on another. All pages are in the menu at the left")
st.write("Simply use : watch the example of a DataFrame")

df = pd.DataFrame({
    'Key': [str(i) for i in range(1,6)],
    'others': ["that's", "a", "columns", "thats", "we don't care "],
    '1st_result': ['ID1 ID2', 'ID2', 'ID3', '', 'ID5'],
    '2nd_result' : ['ID2|ID3', 'ID1', 'ID3', 'ID2|ID4|ID5', 'ID5']
})
def highlight_cells(x):
    df = x.copy()
    styles = pd.DataFrame('', index=df.index, columns=df.columns)
    # Highlight row index 2 (third row), columns '1st_result' and '2nd_result'
    styles.loc[2, '1st_result'] = 'background-color: yellow'
    styles.loc[2, '2nd_result'] = 'background-color: yellow'
    return styles

st.dataframe(df.style.apply(highlight_cells, axis=None))


st.write("""
You can input any csv file but it has to contain:
- 1 column with a recognizable key
- 2 columns to compare
- others are simply ignored
""")

st.markdown(
    'Here the comparaison show that for result_1 & result_2 some IDs <span style="background-color: yellow; color: black">are common</span> and others are differents. Sometimes it is a subset sometimes it isn\'t, etc.',

    unsafe_allow_html=True
)
st.write("gradually, the comparaison becomes more difficult, there are some pages dedicatited for that !")
st.write("Now you can naviguate !")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Select columns"):
        st.switch_page("pages/Select_columns.py")
with col2:
    if st.button("Analyse Intersection"):
        st.switch_page("pages/Tools_Intersection.py")
with col3:
    if st.button("InterPro mapping"):
        st.switch_page("pages/InterPro_parser.py")