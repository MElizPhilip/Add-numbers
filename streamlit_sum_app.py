
import streamlit as st

st.title("Simple Adder App")

# Input fields
num1 = st.number_input("Enter first number", value=0)
num2 = st.number_input("Enter second number", value=0)

# Display sum
if st.button("Calculate Sum"):
    st.success(f"Sum : {num1 + num2}")
