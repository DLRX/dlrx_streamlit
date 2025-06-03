import streamlit as st
import pandas as pd
import numpy as np
import altair as alt 

st.write("""
         # My first app
         Hello *world!*
         """)


st.header('st.button')

if st.button('say hello'):
    st.write('why hello?')
else:
    st.write('goodbye')

st.header('st.write')

st.write('Hello, *world* :sunglasses:')

st.write(1234)

df = pd.DataFrame({
    'colonne 1' : [1, 2, 3, 4],
    'colonne 2' : [10, 20, 30, 40]
})

st.write('le DataFrame est au dessus:', df, 'le DataFrame est en dessous.')

df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns=['a','b','c']
)

c = alt.Chart(df2).mark_circle().encode(
    x='a',y='b', size='c', color='c',tooltip=['a','b','c']
)
st.write(c)


