import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier as RFC

st.title('🧮 Streamlit Machine Learning App')

st.write('Hello world!')

st.info('This is a Streamlit Cloud Python App that builds a ML Model.')

with st.expander('Data'):
  st.write('**Raw Data**')
  # Taken from Github -> dataprofessor -> data -> penguins_cleaned.csv
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df

  st.write('**X**')
  x_raw = df.drop('species', axis=1)
  x_raw

  st.write('**Y**')
  y_raw = df.species
  y_raw

with st.expander('Visualization'):
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')

with st.sidebar:
  st.header('Input Features')
  island = st.selectbox('Island', ('Torgersen', 'Biscoe', 'Dream')) 
  # x_raw['island'].unique() gives 'Torgersen', 'Biscoe', 'Dream'
  
  gender = st.radio('gender', ('male','female'))
  # x_raw['sex'].unique()
  
  bill_length_mm = st.slider('Bill Length in mm', 32.1, 59.6, 43.9)
  # x_raw['bill_length_mm'].min(), x_raw['bill_length_mm'].max(), x_raw['bill_length_mm'].mean()

  bill_depth_mm = st.slider('Bill Depth in mm', 13.1, 21.5, 17.16)
  # x_raw['bill_depth_mm'].min(), x_raw['bill_depth_mm'].max(), x_raw['bill_depth_mm'].mean()

  flipper_length_mm = st.slider('Flipper Length in mm', 172,231, 200)
  # x_raw['flipper_length_mm'].min(), x_raw['flipper_length_mm'].max(), x_raw['flipper_length_mm'].mean()

  body_mass_g = st.slider('Flipper Length in mm', 2700, 6300, 4201)
  # x_raw['body_mass_g'].min(), x_raw['body_mass_g'].max(), x_raw['body_mass_g'].mean()

  data = {'island': island, 
          'bill_length_mm': bill_length_mm,
          'bill_depth_mm': bill_depth_mm,
          'flipper_length_mm': flipper_length_mm,
          'body_mass_g': body_mass_g,
          'sex': gender}

  input_df = pd.DataFrame(data, index=[0])
  input_penquins = pd.concat([input_df, x_raw], axis=0)

# Data Prep
with st.expander('Input Features'): 
  st.write('**Input Penquins**')
  input_df
  st.write('**Combined Data**')
  input_penquins
  
# Convert Categorical Features to Numerical Features using One-Hot Encoding(OHE)
encode = ['island', 'sex']
df_penquins = pd.get_dummies(input_penquins, prefix=encode)
input_row = df_penquins[:1]
X =  df_penquins[1:]

# Convert Categorical Label to Numerical Label using One-Hot Encoding(OHE)
target_mapper = {
  'Adelie' : 0,
  'Chinstrap': 1,
  'Gentoo' : 2
}
def target_encode(val):
  return target_mapper[val]
y=y_raw.apply(target_encode)
                             
with st.expander('Data Preperation'):
  st.write('**One-Hot Encoded Input Penguin [X]**')
  input_row
  st.write('**Encoded Output Label [y]**')
  y

# Model Training
classifier = RFC()
classifier.fit(X,y)

# Apply Model to make prediction
pediction = classifier.predict(input_row)
prediction_probability = classifier.predict_proba(input_row)

df_prediction_probability = pd.DataFrame(prediction_probability)
df_prediction_probability.columns = ['Adelie', 'Chinstrap', 'Gentoo']

st.subheader('Predicted Species')
df_prediction_probability 

penguins_species = np.array(['Adelie', 'Chinstrap', 'Gentoo'])
st.success(str(penguins_species[prediction][0]))
