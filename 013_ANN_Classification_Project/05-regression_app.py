import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
import pickle

# load trained model
model=tf.keras.models.load_model("regression_model.h5")

# load the encoders and scaler
## load pickle file - label encoder geography
with open("onehot_encoder_geo.pkl", "rb") as file:
    label_encoder_geo=pickle.load(file)

# label encoder gender
with open("label_encoder_gender.pkl","rb") as file:
    label_encoder_gender=pickle.load(file)

## load scaler pickle file
with open("scaler.pkl","rb") as file:
    scaler=pickle.load(file)


## streamlit app
st.set_page_config(
    page_title="Estimated Salary Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Estimated Salary Prediction")

st.header("👤 Customer Information")

# user input
with st.container(gap="small"):
    col1, col2, col3 = st.columns(3, gap="small")

    with col1:
        geography = st.selectbox(
            "Geography",
            label_encoder_geo.categories_[0]
        )
        gender = st.selectbox(
            "Gender",
            label_encoder_gender.classes_
        )
        age = st.slider("Age", 18, 92)

    with col2:
        credit_score = st.number_input("Credit Score")
        balance = st.number_input("Balance")
        estimated_salary = st.number_input("Estimated Salary")

        num_of_products = st.selectbox(
            "Number of Products",
            [0, 1, 2, 3, 4]
        )

    with col3:
        tenure = st.slider("Tenure", 0, 10)

        # has_cr_card = st.selectbox("Has Credit Card", [0, 1])
        # is_active_member = st.selectbox("Is Active Member", [0, 1])
        has_cr_card = st.selectbox(
            "Has Credit Card",
            [0, 1],
            format_func=lambda x: "Yes" if x == 1 else "No"
        )

        is_active_member = st.selectbox(
            "Is Active Member",
            [0, 1],
            format_func=lambda x: "Yes" if x == 1 else "No"
        )

        exited = st.selectbox(
            "Is Exit",
            [0, 1],
            format_func=lambda x: "Yes" if x == 1 else "No"
        )

# prepare the data
input_data=pd.DataFrame({
    "CreditScore": [credit_score],
    "Gender": [label_encoder_gender.transform([gender])[0]],
    "Age": [age],
    "Tenure": [tenure],
    "Balance": [balance],
    "NumOfProducts": [num_of_products],
    "HasCrCard": [has_cr_card],
    "IsActiveMember": [is_active_member],
    "Exited": [exited]
})

# onehot encoding of geography
geo_encoded=label_encoder_geo.transform([[geography]]).toarray()
geo_endcoded_df=pd.DataFrame(geo_encoded,columns=label_encoder_geo.get_feature_names_out(["Geography"]))

# combine the onehot encoding with input data
input_data=pd.concat([input_data.reset_index(drop=True), geo_endcoded_df],axis=1)

## scaling the input data
input_scaled=scaler.transform(input_data)

## prediction the estimated salary
prediction=model.predict(input_scaled)

prediction_salary=prediction[0][0]

# display output
st.header("Prediction Results")

st.metric(
        "Predicted Estimated Salary",
        f"{prediction_salary:.2f}"
    )