import streamlit as st
import pandas as pd
import joblib  #


model = joblib.load('random-forest.pkl')  

st.set_page_config(page_title="Random Forest Classifier", layout="centered")

st.title("Random Forest Classification Web App")
st.markdown("Provide input values below to get a prediction.")


feature_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']  

# Create input fields for each feature
input_data = {}
for feature in feature_names:
    input_data[feature] = st.number_input(f"Enter value for {feature}", value=0.0)

# Convert input data to DataFrame
input_df = pd.DataFrame([input_data])

# Predict on button click
if st.button("Predict"):
    prediction = model.predict(input_df)
    prediction_proba = model.predict_proba(input_df)

    st.subheader("Prediction Result")
    st.write(f"Predicted Class: **{prediction[0]}**")
    st.write("Prediction Probabilities:")
    st.write(prediction_proba)

# Optional: expand to show raw input
with st.expander("Show input data"):
    st.write(input_df)

st.write("0 : Setosa ")
st.write("1 : Versicolor")
st.write("2 : Virginica ")