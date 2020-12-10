import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st
import sqlite3

st.title('Load data from Purchases!')


@st.cache
def load_data():
    database = 'db.sqlite3'
    conn = sqlite3.connect(database)
    data = pd.read_sql("select * from data_purchase", con=conn)
    return data


data_load_state = st.text('loading data...')
data = load_data()
data_load_state.text("Done! (using st.cache)")

if st.checkbox("Show raw data"):
    st.subheader('Raw Data')
    st.write(data)
