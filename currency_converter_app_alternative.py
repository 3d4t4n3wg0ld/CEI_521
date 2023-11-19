import streamlit as st
import requests

API_KEY = '83754dc3d2-6c852bf831-s3rryq'  # Replace with your actual ExchangeRate-API key

def currency_converter(amount, from_currency, to_currency):
    base_url = "https://open.er-api.com/v6/latest"
    params = {"apikey": API_KEY, "symbols": f"{from_currency},{to_currency}"}

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200 and data["result"] == "success":
        rate = data["rates"][to_currency] / data["rates"][from_currency]
        converted_amount = amount * rate
        return converted_amount
    else:
        st.error("Error fetching exchange rates. Please check your API key and try again.")
        st.stop()

def main():
    st.title("Currency Converter App")

    amount = st.number_input("Enter the amount:", min_value=0.01, value=1.00, step=0.01)

    from_currency = st.selectbox("From Currency:", ["USD", "EUR", "GBP", "JPY", "INR"])

    to_currency = st.selectbox("To Currency:", ["USD", "EUR", "GBP", "JPY", "INR"])

    if st.button("Convert"):
        converted_amount = currency_converter(amount, from_currency, to_currency)
        st.success(f"{amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

    st.info("Note: Replace 'YOUR_EXCHANGERATE_API_KEY' with your actual ExchangeRate-API key.")

if __name__ == "__main__":
    main()



