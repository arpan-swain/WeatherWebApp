import streamlit as st
import plotly.express as px

st.title("Weather Forecast for Next Days")

place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days to forecast")
option = st.selectbox("Select data to view",
                      ("Temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

figure = px.line(x=[1,2,3],y=[4,5,6], labels={"x":"Date","y":"Temperature(C)"})
st.plotly_chart(figure)