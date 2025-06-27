# Cryptocurrency Heatmap

A Streamlit web application that visualizes real-time cryptocurrency market data as a heatmap, with optional real-time price alerts.

## Features

- Fetches live data from the CoinGecko API
- Interactive heatmap visualization of crypto price changes
- Real-time price alert system for user-selected coins
- Simple, modern UI built with Streamlit and Plotly

## Requirements

- Python 3.8+
- pip

## Installation

1. **Clone the repository:**
git clone https://github.com/johnpauldaiyoshida/Cryptocurrency-Heatmap.git

2. **Install dependencies:**
pip install -r requirements.txt

## Running the App

1. **From the project root directory, start the Streamlit app:**

streamlit run streamlit_app.py

If `streamlit` is not recognized, try:

python -m streamlit run streamlit_app.py

2. **Open your browser to the local URL provided by Streamlit (usually http://localhost:8501).**

## Usage

- The main page displays a heatmap of cryptocurrencies and their 24h price changes.
- Use the sidebar to select a coin and set a price alert threshold. If the coin’s price meets or exceeds your threshold, an alert will appear.

## Running Tests

To run the unit tests:

python -m unittest discover -s tests

## Configuration

You can adjust API endpoints, color schemes, and refresh intervals in `config/constants.py`.

## Troubleshooting
- **API errors:** The app requires internet access to fetch data from CoinGecko.

## License

MIT License

---

*Built with [Streamlit](https://streamlit.io/) and [Plotly](https://plotly.com/python/).*
