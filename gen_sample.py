import os
import pandas as pd
import numpy as np
import random

# Define the necessary parameters
tuning_params = [1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
distance_threshes = [0, 2500, 5000, 10000, 25000, 50000]
ayalon_only = ["Yes", "No"]

# Create the assets directory if it doesn't exist
os.makedirs('assets', exist_ok=True)

# Generate data.csv with randomized values
data_rows = []
for tp in tuning_params:
    for dt in distance_threshes:
        for ay in ayalon_only:
            network_length = round(random.uniform(50, 500),2)
            covered_network_length = round(random.uniform(0, network_length),2)
            estimated_price = round(random.uniform(1000, 100000),2)
            num_polygons = random.randint(1, 20)
            data_rows.append([tp, dt, ay, network_length, covered_network_length, estimated_price, num_polygons])

data_columns = ["Tuning Parameter", "Distance Threshold", "Ayalon Only", "Network length", "Covered Network Length", "Estimated Price", "Number of Polygons"]
data_df = pd.DataFrame(data_rows, columns=data_columns)
data_df.to_csv('assets/data.csv', index=False)

# Generate .txt and .csv files for each combination
polygon_template = """
POLYGON ((34.7818 32.0853, 34.7998 32.0853, 34.7998 32.0753, 34.7818 32.0753, 34.7818 32.0853))
"""

for tp in tuning_params:
    for dt in distance_threshes:
        for ay in ayalon_only:
            file_prefix = f"{tp}_{dt}_{ay.lower()}"
            
            # Create .txt file with polygon data
            with open(f'assets/{file_prefix}.txt', 'w') as txt_file:
                txt_file.write(polygon_template.strip())
            
            # Create .csv file with road data
            road_rows = []
            for i in range(5):  # Generating 5 road names with random values
                road_name = f"Road {i+1}"
                num_polygons = random.randint(1, 10)
                road_rows.append([road_name, num_polygons])
            
            road_columns = ["Road Name", "Number of Polygons"]
            road_df = pd.DataFrame(road_rows, columns=road_columns)
            road_df.to_csv(f'assets/{file_prefix}.csv', index=False)

print("Assets generated successfully!")