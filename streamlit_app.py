import streamlit as st
import pandas as pd
import numpy as np

st.title('🧮 Streamlit Machine Learning App')

st.write('Hello world!')

st.info('This is a Streamlit Cloud Python App that builds a ML Model.')

with st.expander('Data'):
  st.write('**Raw Data**')
  # Taken from Github -> dataprofessor -> data -> penguins_cleaned.csv
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df

  st.write('**X**')
  x = df.drop('species', axis=1)
  x

  st.write('**Y**')
  y = df.species
  y

with st.expander('Visualization'):
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')

with st.sidebar:
  st.header('Input Features')
  island = st.selectbox('Island', ('Torgersen', 'Biscoe', 'Dream')) 
  # x['island'].unique() gives 'Torgersen', 'Biscoe', 'Dream'
  
  gender = st.radio('gender', ('male','female'))
  # x['sex'].unique()
  
  bill_length_mm = st.slider('Bill Length in mm', 32.1, 59.6, 43.9)
  # x['bill_length_mm'].min(), x['bill_length_mm'].max(), x['bill_length_mm'].mean()

  bill_depth_mm = st.slider('Bill Depth in mm', 13.1, 21.5, 17.16)
  # x['bill_depth_mm'].min(), x['bill_depth_mm'].max(), x['bill_depth_mm'].mean()

  flipper_length_mm = st.slider('Flipper Length in mm', 172,231, 200.96)
  # x['flipper_length_mm'].min(), x['flipper_length_mm'].max(), x['flipper_length_mm'].mean()

  body_mass_g = st.slider('Flipper Length in mm', 2700, 6300, 4201.05)
  # x['body_mass_g'].min(), x['body_mass_g'].max(), x['body_mass_g'].mean()

  data = {'island', island, 
          'bill_length_mm': bill_length_mm,
          'bill_depth_mm': bill_depth_mm,
          'flipper_length_mm': flipper_length_mm,
          'body_mass_g': body_mass_g,
          'gender': gender}

  input_df = pf.DataFrame(data, index=[0])
  input_penquins = pd.concat([input_df, X] axis=0)
                             
with st.expander('Input Features'): 
  st.write('**Input Penquins')
  input_df
  st.write('**Combined Data**')
  input_penquins
