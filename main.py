import streamlit as st
import pandas as pd


done = False
st.session_state['done'] = done

st.markdown(
    """
    <h1 style='text-align: center;'> CompTkit : Comparison Tool Kit</h1>
    """,
    unsafe_allow_html=True
)
_, col_img, _ = st.columns(3)
with col_img:
    st.image("img/logo.svg", width=1000)


import importlib.util
st.write('pandas dispo ?', importlib.util.find_spec("pandas") is not None)
st.write('tqdm dispo ?', importlib.util.find_spec("tqdm") is not None)
st.write('matplotlib_venn dispo ?', importlib.util.find_spec("matplotlib_venn") is not None)
st.write('xml.etree.ElementTree dispo ?', importlib.util.find_spec("xml.etree.ElementTree") is not None)
st.write('streamlit dispo ?', importlib.util.find_spec("streamlit") is not None)
st.write('numpy dispo ?', importlib.util.find_spec("numpy") is not None)
st.write('matplotlib dispo ?', importlib.util.find_spec("matplotlib") is not None)
st.write('cafaeval dispo ?', importlib.util.find_spec("cafaeval") is not None)


st.markdown("**Welcome on site!** here we can explore your data and compare two columns on a csv file")
st.markdown("*How does it work?* - here your are on the main page, you can choose a button to go on another. All pages are in the menu at the left")
st.write("Simply use : watch the example of a DataFrame")

df = pd.DataFrame({
    'Key': [str(i) for i in range(1,6)],
    'others': ["that's", "a", "columns", "thats", "we don't care "],
    '1st_result': ['ID1 ID2', 'ID2', 'ID3', '', 'ID5'],
    '2nd_result' : ['ID2|ID3', 'ID1', 'ID3', 'ID2|ID4|ID5', 'ID5']
})


st.write(df)


st.write("""
You can input any csv file but it has to contain:
- 1 column with a recognizable key
- 2 columns to compare
- others are simply ignored
""")

st.write("Here the comparaison show that for result_1 & result_2 some IDs are common and others are differents. Sometimes it is a subset sometimes it isn\'t, etc.")
st.write("gradually, the comparaison becomes more difficult, there are some pages dedicatited for that !")
st.write("Now you can naviguate !")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Select columns"):
        st.switch_page("pages/venn_analysis.py")
