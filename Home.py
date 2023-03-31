import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from PIL import Image

st.set_page_config(layout="wide")

st.header("Farlo MLB Model")

st.subheader("Record this season:")

st.write("This is where we will update our record and a graph showing the units won/loss")

image = Image.open("assets/workinprogress.jpeg")

st.image(image)