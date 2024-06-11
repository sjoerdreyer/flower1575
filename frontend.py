import streamlit as st
import requests

st.title('My Iris flower classifier app')

st.write('Select your features below:')

sep_len = st.slider('Select a value for Sepal length', min_value=0, max_value=10, value=1, step=1)
sep_wid = st.slider('Select a value for Sepal width', min_value=0, max_value=10, value=1, step=1)
pet_len = st.slider('Select a value for Petal length', min_value=0, max_value=10, value=1, step=1)
pet_wid = st.slider('Select a value for Petal width', min_value=0, max_value=10, value=1, step=1)

# Method 1
url = 'https://api1575-cctigceneq-ew.a.run.app/predict'
params = {'sepal_length': sep_len,
          'sepal_width': sep_wid,
          'petal_length': pet_len,
          'petal_width': pet_wid}


response = requests.get(url=url,
                        params=params).json()


#Method 2:
# response = requests.get(f'https://api1575-cctigceneq-ew.a.run.app/predict?\
#         sepal_length={sep_len}&sepal_width={sep_wid}&\
#         petal_length={pet_len}&petal_width={pet_wid}').json()

st.write('The flower belongs to class', str(response['flower:']))
