# Simple Weather App
 
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![LICENSE](https://img.shields.io/github/license/jovianka/simple-weather-app?style=for-the-badge)

With this app you can view weather conditions in your area displayed using graphs and such!

## Prerequisites 📋

- python 3.11.5 or higher
- pip
- Dependencies: streamlit 1.27.0 or higher, st-gsheets-connection

## Installation 🛠

- Clone the repository:

```bash
git clone https://github.com/jovianka/simple-weather-app.git
```

- Install the packages:

```bash
pip install -r requirements.txt
```

- Set up secret for database connection (Google Sheets):
See [this page](https://github.com/streamlit/gsheets-connection/tree/main#service-account--crud-example) to learn about connecting streamlit app to Google Sheets using the [st-gsheets-connection](https://github.com/streamlit/gsheets-connection) package.

- Run the application:

```bash
streamlit run main.py
```

## Story
### How We Built It?
This app is based on the Weather Forecast API from [Open Meteo](https://open-meteo.com) and streamlit. Here's how the app works: We make a request to get data on some weather variables (currently 3), extracted data from the response to a `pandas DataFrame`. Then, we used `st.experimental_connection("gsheets", type=GSheetsConnection)` to connect our app to a google sheets spreadsheet and updated the spreadsheet based on the data. After that, we display the data using line charts made with `st.altair_chart()`.

### Challenges We Ran Into
Using altair, hardware problems (slows down development) python indentations, pip packages dependency conflict, and minimal understanding of data science ecosystem in python.

### Accomplishments That We're Proud Of
We were able to learn so much. From learning pandas, pip, retrieving data from API, making data frames, and how data is displayed programmatically. All that, in such little time (in our perspective).

### What We Learned
Streamlit's made it so much easier to connect to a particular database and even make changes to it. Python has a library for pretty much anything you need in data science.

### What's Next?
Let users pick more locations and display more weather variables elegantly. Make a page about how some of these weather variables are useful for the general audience

## License 📝

This project is licensed under the GPLv3 License. See the [LICENSE](LICENSE) file for details.
