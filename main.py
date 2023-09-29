import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for Next Days")

place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days to forecast")
option = st.selectbox("Select data to view",
                      ("Temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}")
if place:
    filtered_data = get_data(place,days)
    if option == "Temperature":
        temperature = [int(x["main"]["temp"])/10 for x in filtered_data]
        dates = [x["dt_txt"] for x in filtered_data]
        figure = px.line(x=dates,y=temperature, labels={"x":"Date","y":"Temperature(C)"})
        st.plotly_chart(figure)

    if option == "Sky":
        stored_img = {"Clear":"images/clear.png","Clouds":"images/cloud.png","Rain":"images/rain.png",
                      "Snow":"images/snow.png"}
        sky_conditions = [x["weather"][0]["main"] for x in filtered_data]
        images = [stored_img[x] for x in sky_conditions]
        st.image(images, width=110)