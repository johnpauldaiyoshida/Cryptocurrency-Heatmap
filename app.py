from dash import Dash
from components.heatmap import create_heatmap_layout
from components.filters import create_filters
from data.api_client import fetch_crypto_data, APIClient

def create_app(api_client=APIClient()):
    app = Dash(__name__)
    app.layout = create_heatmap_layout(api_client.fetch_data())
    return app

app = Dash(__name__)
app.layout = html.Div([
    create_filters(),  # From components/filters.py
    create_heatmap_layout(fetch_crypto_data())  # From components/heatmap.py
])

if __name__ == "__main__":
    app.run(debug=True)