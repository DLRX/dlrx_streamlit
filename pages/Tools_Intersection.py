import streamlit as st
import pandas as pd

from matplotlib_venn import venn2
import matplotlib.pyplot as plt

from tool.venn import venn_analysis


st.markdown(
    """
    <h1 style='text-align: center;'>Focus on the Intersection</h1>
    """,
    unsafe_allow_html=True
)

done = st.session_state.get('done')

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
    btn = st.button("Go to main page", key="main", help="Navigate to main", type="primary")
    st.markdown('<div class="full-width-button"></div>', unsafe_allow_html=True)

if btn:
    st.switch_page("./main.py")


