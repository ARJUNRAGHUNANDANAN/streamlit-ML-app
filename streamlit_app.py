import streamlit as st
import pandas as pd
st.title('🧮 Streamlit Machine Learning App')

st.write('Hello world!')

st.info('This is a Streamlit Cloud Python App that builds a ML Model.')

with st.expander('Data'):
  st.write('**Raw Data**')
  # Taken from Github -> dataprofessor -> data -> penguins_cleaned.csv
  df = pdf.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df

  st.write('**X**')
  x = df.drop('species, axis=1')
  x

  st.write('**Y**')
  y = df.species
  y
