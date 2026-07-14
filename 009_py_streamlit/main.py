import streamlit as st # https://streamlit.io
import pandas as pd
import numpy as np

st.title("Hello streamlit!")

df = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry", "Ivy", "Jack"],
    "Department": ["HR", "IT", "Finance", "Marketing", "Sales", "IT", "HR", "Finance", "Sales", "Marketing"],
    "Age": [25, 30, 28, 35, 27, 32, 29, 41, 26, 33],
    "Salary": [50000, 75000, 68000, 82000, 59000, 77000, 54000, 91000, 61000, 80000]
})

st.write("This is Dataframe")
st.write(df)
df.to_csv("sample.csv")
# line chart
# chart_data=pd.DataFrame(np.random.randn(20,3), columns=['a','b','c'])
# st.line_chart(chart_data)

# form field
name = st.text_input("Enter Your Name")
age = st.slider("Select Your Age", 18, 100, None, 1)
language = st.selectbox("Select language",["Hindi", "English"])

uploaded_file = st.file_uploader("Upload Your Document", type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)