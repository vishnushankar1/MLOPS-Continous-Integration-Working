import streamlit as st
st.title('Power calculator')

st.write("Enter a number to calulate its square,cube, and fifthe power")

n=st.number_input("enter a integer",step=1)

square=n**2
cube=n**3
fifth_power=n**5

#display results
st.write(f"the square of {n} is: {square}")
st.write(f"the cube of { n} is: {cube}")
st.write(f"the fifth power of {n} is: {fifth_power}")