import requests
import math
import json
import app
from currency_converter_app_alternative import currency_converter,main
from streamlit_option_menu import option_menu
import streamlit as st
from forex_python.converter import CurrencyRates
def print_currency_rate(from_currency, to_currency):
    c = CurrencyRates()
    rate = c.get_rate(from_currency, to_currency)
    return rate
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select a page", ["Weather for Limassol", "Weather for a city", "Currency Converter","Currency Converter to Euro"])

    # Main content
if page == "Weather for Limassol":
    st.header("Check the current weather")
    st.image("https://media.istockphoto.com/id/1041721794/photo/aerial-view-of-molos-limassol-cyprus.jpg?s=2048x2048&w=is&k=20&c=ufiTRg0EsCSSJvPqG1F58e1fwAmOKg1BaWxILGJQlyE=")
    app.app("Limassol")

if page== "Weather for a city":
    st.header("Check the current weather")
    st.image("https://www.theschoolrun.com/sites/theschoolrun.com/files/styles/188x148/public/weather_.jpg?itok=DLfCnBiD")
    city = st.text_input("Enter city name")
    if st.button("Get Weather"):
        app.app(city)

if page == "Currency Converter":
  
   st.title("Currency Converter App")
   amount = st.number_input("Enter the amount:", min_value=0.01, value=1.00, step=0.01)
   from_currency = st.selectbox("From Currency:", ["USD", "EUR", "GBP", "JPY", "INR"])
   to_currency = st.selectbox("To Currency:", ["USD", "EUR", "GBP", "JPY", "INR"])

   if st.button("Convert"):
        converted_amount = currency_converter(amount, from_currency, to_currency)
        st.success(f"{amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

if page == "Currency Converter to Euro":
    
    from_currency_USD = "USD"
    from_currency_JPY = "JPY"
    from_currency_GBP = "GBP"
    to_currency_EUR = "EUR"

    c = CurrencyRates()
    rate = c.get_rate(from_currency_USD, to_currency_EUR)
    st.success(f" {from_currency_USD} is equal to {rate:.2f} {to_currency_EUR}")

    rate1 = c.get_rate(from_currency_JPY, to_currency_EUR)
    st.success(f" {from_currency_JPY} is equal to {rate:.2f} {to_currency_EUR}")

    rate2 = c.get_rate(from_currency_GBP, to_currency_EUR)
    st.success(f" {from_currency_GBP} is equal to {rate:.2f} {to_currency_EUR}")
