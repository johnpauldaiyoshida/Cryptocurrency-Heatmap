import plotly.express as px
from utils.helpers import normalize_data

def create_heatmap_layout(data):
    df = normalize_data(data)  # From utils/helpers.py
    fig = px.treemap(
        df, 
        path=['name'],
        color='price_change_percentage_24h',
        color_continuous_scale='RdYlGn'
    )
    return fig