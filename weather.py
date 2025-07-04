import requests

API_KEY="XHECTFR4PN9R59RDRFWDPBCVE"
def scale_rainfall(real_rainfall, min_real=0, max_real=30, min_train=20, max_train=298.560117):
    real_rainfall = min(max(real_rainfall, min_real), max_real)  # clamp to bounds
    scaled = ((real_rainfall - min_real) / (max_real - min_real)) * (max_train - min_train) + min_train
    return scaled
def get_weather_data(city: str):
    url=f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city},IND/today?key={API_KEY}&include=days&elements=precip,humidity,temp&unitGroup=metric&contentType=json"
    response=requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Weather API error: {response.text}")
    data=response.json()
    today=data['days'][0]
    return{
        "temperature": today['temp'],
        "humidity":today['humidity'],
        "precipitation":scale_rainfall(today['precip'])
    }


