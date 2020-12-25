import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


st.title("Alan Wong's Portfoilo")
st.sidebar.title("Select Page")
page = ["Main", "Work Example", "Contact"]
st.sidebar.radio("",page)