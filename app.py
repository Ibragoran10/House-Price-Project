import streamlit as st # Use for UI User
import joblib          # Use for loding Model 
import numpy as np     # Creating Array

model = joblib.load("model.pkl")

st.title("House Price Prediction App")

st.divider()

st.write("This app uses machine learning for predicting house price with given features. For using this app you can enter the inputs from this UI and then use predict button.") 

st.divider()

bedrooms = st.number_input("Number of bedrooms", min_value = 0 , value = 0)
bathrooms = st.number_input("Number of bathrooms", min_value = 0 , value = 0)
livingarea = st.number_input("Living area", min_value = 0 , value = 2000)
condition = st.number_input("Condition", min_value = 0 , value = 3)
Numberofschools = st.number_input("Number of schools nearby", min_value = 0 , value = 0)

st.divider()

x = [[bedrooms,bathrooms,livingarea,condition,Numberofschools ]]

predictbutton = st.button("Predict")

if predictbutton:
    
    st.balloons()

    x_array = np.array(x)

    prediction = model.predict(x_array)[0]

    st.write(f"Price prediction is {prediction:,.2f}")

else:
    st.write("Please use predict buttton after enterring values")

#order of x['number of bedrooms', 'number of bathrooms', 'living area',
      # 'condition of the house', 'Number of schools nearby']