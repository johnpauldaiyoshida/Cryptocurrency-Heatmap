import pandas as pd

def normalize_data(data):
    """
    Converts raw API data into a DataFrame suitable for the heatmap.
    Expects each item in data to have 'name' and 'price_change_percentage_24h'.
    """
    if not data:
        return pd.DataFrame(columns=['name', 'price_change_percentage_24h'])
    df = pd.DataFrame(data)
    # Ensure required columns exist
    if 'name' not in df.columns or 'price_change_percentage_24h' not in df.columns:
        raise ValueError("Data must contain 'name' and 'price_change_percentage_24h' fields.")
    return df