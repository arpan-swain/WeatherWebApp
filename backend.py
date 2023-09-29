import requests

api_key = "141710af2113bab9f55ef73e1bcd33d5"

def get_data(place,forecastday=None,kind=None):
    url=f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8*forecastday
    filtered_data=filtered_data[:nr_values]
    if kind == "Temperature":
        filtered_data=[x["main"]["temp"] for x in filtered_data]
    elif kind == "Sky":
        filtered_data = [x["weather"][0]["main"] for x in filtered_data]

    return filtered_data

if __name__ == "__main__":
    print(get_data("Delhi",forecastday=2,kind="Temperature"))