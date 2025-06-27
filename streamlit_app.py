import streamlit as st
from components.heatmap import create_heatmap_layout
from data.api_client import fetch_crypto_data

st.title("Crypto Heatmap")
data = fetch_crypto_data()

if data:
    st.plotly_chart(create_heatmap_layout(data))

    # --- Real-time Price Alert Section ---
    coin_names = [coin['name'] for coin in data]
    selected_coin = st.selectbox("Select a coin for price alert:", coin_names)
    threshold = st.number_input("Set price alert threshold (USD):", min_value=0.0, value=0.0, step=0.01)

    # Find the selected coin's current price
    selected_coin_data = next((coin for coin in data if coin['name'] == selected_coin), None)
    if selected_coin_data:
        current_price = selected_coin_data.get('current_price')
        st.write(f"Current price of {selected_coin}: ${current_price}")

        # Check if the price crosses the threshold
        if current_price is not None and threshold > 0:
            if current_price >= threshold:
                st.warning(f"🚨 {selected_coin} price has reached or exceeded your alert threshold (${threshold})!")
                st.experimental_rerun()
    else:
        st.info("Coin data not found.")
else:
    st.error("Failed to load data.")