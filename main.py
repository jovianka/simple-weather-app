import streamlit as st
import pandas as pd
import altair as alt
from streamlit_gsheets import GSheetsConnection
import requests
import pygsheets

conn = st.experimental_connection("gsheets", type=GSheetsConnection)
df = conn.read(spreadsheet=st.secrets.connections.gsheets.spreadsheet, worksheet=st.secrets.connections.gsheets.worksheet)

# client = pygsheets.authorize()
# sheets = client.open('sickathon-weather')

# locations = {
#   "Jakarta Pusat": (-8.7909, 115),
#   "Bogor": (-6.5944, 106.7892),
#   "Depok": (-6.4, 106.8186),
#   "Tangerang": (-6.1781, 106.63),
#   "Bekasi": (-6.2349, 106.9896),
# }

# location = st.selectbox("Please pick your location", ("Jakarta Pusat", "Bogor", "Depok", "Tangerang", "Bekasi"), index=None, placeholder="--Location--")

# data = requests.get("https://api.open-meteo.com/v1/forecast", params={ "latitude": locations[location][0], \
#                                                                       "longitude": locations[location][1], \
#                                                                       "hourly": ["temperature_2m", "dewpoint_2m", "apparent_temperature"]}).json()

# conn = st.experimental_connection("gsheets", type=GSheetsConnection)
# df = conn.read(url="https://docs.google.com/spreadsheets/d/1KQ_vqbycPrnZGtn2Ylk_cT8bpCkzsmf2KklJasKr9K4/edit?usp=sharing")

def get_chart(df, weather_variable):
    hover = alt.selection_point(
        fields=["time"],
        nearest=True,
        on="mouseover",
        empty=True,
        )
    
    # Temperature
    lines_temperature = (
        alt.Chart(df, title="Temperature Forecast")
        .mark_line()
        .encode(
            x=alt.X("time:T"),
            y="temperature_2m",
            )
        )

    points_temperature = lines_temperature.transform_filter(hover).mark_circle(size=65)

    tooltips_temperature = (
        alt.Chart(df)
        .mark_rule()
        .encode(
            x=alt.X("time:T").title("Date").axis(format="%d - %B"),
            y=alt.Y("temperature_2m").title("Temperature (°C)"),
            opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
            tooltip=[
                alt.Tooltip("time:T", title="Time", format="%a, %d %B %Y %H:%M"),
                alt.Tooltip("temperature_2m", title="Temperature"),
            ],
        ).add_params(hover)
        )

    # Dewpoint
    lines_dewpoint = (
        alt.Chart(df, title="Dewpoint Forecast")
        .mark_line()
        .encode(
            x=alt.X("time:T"),
            y="dewpoint_2m",
            )
        )

    points_dewpoint = lines_dewpoint.transform_filter(hover).mark_circle(size=65)

    tooltips_dewpoint = (
        alt.Chart(df)
        .mark_rule()
        .encode(
            x=alt.X("time:T").title("Date").axis(format="%d - %B"),
            y=alt.Y("dewpoint_2m").title("Dewpoint (°C)"),
            opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
            tooltip=[
                alt.Tooltip("time:T", title="Time", format="%a, %d %B %Y %H:%M"),
                alt.Tooltip("dewpoint_2m", title="Dewpoint"),
            ],
        ).add_params(hover)
        )

    # Apparent Temperature
    lines_apparent_temperature = (
        alt.Chart(df, title="Apparent Temperature Forecast")
        .mark_line()
        .encode(
            x=alt.X("time:T"),
            y="apparent_temperature",
            )
        )

    points_apparent_temperature = lines_apparent_temperature.transform_filter(hover).mark_circle(size=65)

    tooltips_apparent_temperature = (
        alt.Chart(df)
        .mark_rule()
        .encode(
            x=alt.X("time:T").title("Date").axis(format="%d - %B"),
            y=alt.Y("apparent_temperature").title("Apparent Temperature (°C)"),
            opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
            tooltip=[
                alt.Tooltip("time:T", title="Time", format="%a, %d %B %Y %H:%M"),
                alt.Tooltip("apparent_temperature", title="Apparent Temperature"),
            ],
        ).add_params(hover)
        )
    
    
    if weather_variable == "temperature":
        return (lines_temperature + points_temperature + tooltips_temperature).interactive()
    elif weather_variable == "dewpoint":
        return (lines_dewpoint + points_dewpoint + tooltips_dewpoint).interactive()
    elif weather_variable == "apparent_temperature":
        return (lines_apparent_temperature + points_apparent_temperature + tooltips_apparent_temperature).interactive()

chart_temperature = get_chart(df, "temperature")
chart_dewpoint = get_chart(df, "dewpoint")
chart_apparent_temperature = get_chart(df, "apparent_temperature")

st.header("Weather in Jimbaran")

st.altair_chart(chart_temperature, use_container_width=True)
st.altair_chart(chart_dewpoint, use_container_width=True)
st.altair_chart(chart_apparent_temperature, use_container_width=True)
