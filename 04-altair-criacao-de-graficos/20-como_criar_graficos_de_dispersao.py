import streamlit as st
import altair as alt
import pandas as pd

source = pd.read_csv('vega_car.csv')

source # imprimindo o dataframe