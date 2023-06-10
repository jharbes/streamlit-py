import streamlit as st
import altair as alt
import pandas as pd

source = pd.read_csv('vega_car.csv')

points = alt.Chart(source).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color=alt.Color('Origin:N')   
)

st.altair_chart(points, use_container_width=True)