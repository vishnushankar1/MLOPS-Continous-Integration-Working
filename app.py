import streamlit as st

st.title('Power calculator')

st.write("Enter a number to calculate its square, cube, and fifth power")

n = st.number_input("Enter an integer", step=1)

square = n ** 2
cube = n ** 3
fifth_power = n ** 5

# Display results
st.write(f"The square of {n} is: {square}")
st.write(f"The cube of {n} is: {cube}")
st.write(f"The fifth power of {n} is: {fifth_power}")
