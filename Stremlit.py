import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import joblib
import streamlit as st 
data=joblib.load('MODEL.pkl')
st.title('Cancer Predictor')
radius_mean=st.number_input('radius_mean')
texture_mean=st.number_input('texture_mean')
area_mean=st.number_input('area_mean')
perimeter_mean=st.number_input('perimeter_mean')
smoothness_mean=st.number_input('smoothness_mean')
compactness_mean=st.number_input('compactness_mean')
concavity_mean=st.number_input('concavity_mean')
concave_points_mean=st.number_input('concave points_mean')
symmetry_mean=st.number_input('symmetry_mean')
fractal_dimension_mean=st.number_input('fractal_dimension_mean')
radius_se=st.number_input('radius_se')
texture_se=st.number_input('texture_se')
perimeter_se=st.number_input('perimeter_se')
smoothness_se=st.number_input('smoothness_se')
compactness_se=st.number_input('compactness_se')
concavity_se=st.number_input('concavity_se')
concave_points_se=st.number_input('concave points_se')
symmetry_se=st.number_input('symmetry_se')
area_se=st.number_input('area_se')
radius_worst=st.number_input('radius_worst')
texture_worst=st.number_input('texture_worst')
fractal_dimension_se=st.number_input('fractal_dimension_se')
perimeter_worst=st.number_input('perimeter_worst')
area_worst=st.number_input('area_worst')
smoothness_worst=st.number_input('smoothness_worst')
compactness_worst=st.number_input('compactness_worst')
concavity_worst=st.number_input('concavity_worst')
concave_points_worst=st.number_input('concave points_worst')
symmetry_worst=st.number_input('symmetry_worst')
fractal_dimension_worst=st.number_input('fractal_dimension_worst')
data_dic={
       'radius_mean': [radius_mean], 'texture_mean': [texture_mean], 'perimeter_mean':[perimeter_mean],
       'area_mean': [area_mean], 'smoothness_mean': [smoothness_mean], 'compactness_mean': [compactness_mean], 'concavity_mean': [concavity_mean],
       'concave points_mean':[concave_points_mean], 'symmetry_mean': [symmetry_mean], 'fractal_dimension_mean': [fractal_dimension_mean],
       'radius_se': [radius_se], 'texture_se': [texture_se], 'perimeter_se': [perimeter_se], 'area_se':[area_se], 'smoothness_se': [smoothness_se],
       'compactness_se': [compactness_se], 'concavity_se': [concavity_se], 'concave points_se': [concave_points_se], 'symmetry_se': [symmetry_se],
       'fractal_dimension_se' :[fractal_dimension_se], 'radius_worst': [radius_worst], 'texture_worst':[texture_worst],
       'perimeter_worst': [perimeter_worst], 'area_worst': [area_worst], 'smoothness_worst': [smoothness_worst],
       'compactness_worst': [compactness_worst], 'concavity_worst': [concavity_worst], 'concave points_worst': [concave_points_worst],
       'symmetry_worst': [symmetry_worst], 'fractal_dimension_worst': [fractal_dimension_worst]
}
dt=pd.DataFrame(data_dic)
result=data.predict(dt)
if st.button('calculate' ):
     if result==1:
          st.write('The Patient is Cancer-Positive')
     else:
          st.write('Patient is Cancer-Negative')
          
          
