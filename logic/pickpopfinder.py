import pandas as pd

def get_nearest(user_postal_code, sg_postal_path, station_path):
    # 1. Load the datasets
    sg_postal = pd.read_csv(sg_postal_path)
    stations = pd.read_csv(station_path)
    
    # 2. Clean and merge coordinates
    stations = stations.dropna(subset=['postal_code'])
    stations['postal_code'] = stations['postal_code'].astype(int)
    sg_postal['postal_code'] = sg_postal['postal_code'].astype(int)

    # Attach coordinates to the stations
    stations_with_coords = stations.merge(
        sg_postal[['postal_code', 'lat', 'lon']], 
        on='postal_code', 
        how='left'
    ).dropna(subset=['lat', 'lon'])

    # 3. Get user coordinates
    user_info = sg_postal[sg_postal['postal_code'] == int(user_postal_code)]
    if user_info.empty:
        return f"Error: Postal code {user_postal_code} not found."
    
    u_lat, u_lon = user_info.iloc[0]['lat'], user_info.iloc[0]['lon']
    
    # 4. Euclidean Distance Calculation
    stations_with_coords['euclidean_dist'] = (
        (stations_with_coords['lat'] - u_lat)**2 + 
        (stations_with_coords['lon'] - u_lon)**2
    ) ** 0.5
    stations_with_coords['estimated_dist_km'] = round(stations_with_coords['euclidean_dist'] * 111.32 * 1000, 2)

    # 5. Sort and take Top 40
    top_choices = stations_with_coords.sort_values(by='euclidean_dist').head(40)
    
    return top_choices