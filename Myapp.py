import streamlit as st
import pandas as pd
import numpy as np
import altair as alt 
from datetime import time, datetime

st.write("""
         # My first app
         Hello *world!*
         Première question : quand je touche un outil intéractif (slider, box, etc.) les random.randn se relance cela change les graphiques
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

st.header('st.slider')

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# Example 2

st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# Example 3

st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# Example 4

st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

st.header('Line chart')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.header('st.selectbox')

option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))

st.write('Your favorite color is ', option)

st.header('st.multiselect')

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)

st.header('st.checkbox')

st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
     st.write("Great! Here's some more 🍦")

if coffee: 
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")

df = pd.read_csv(r"C:\Users\dodol\Documents\LBM\Stage\test_recup_43k.csv")
st.write(df)
