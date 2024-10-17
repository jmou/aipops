import csv
import json

def csv_to_geojson(csv_file, geojson_file):
    features = []

    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Check if latitude and longitude are present and not empty
            if row['latitude'] and row['longitude']:
                feature = {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [float(row['longitude']), float(row['latitude'])]
                    },
                    "properties": {
                        key: value for key, value in row.items() if key not in ['latitude', 'longitude']
                    }
                }
                features.append(feature)

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    with open(geojson_file, 'w') as outfile:
        json.dump(geojson, outfile, indent=2)

if __name__ == "__main__":
    csv_to_geojson('pops.csv', 'pops.geojson')
    print("GeoJSON file 'pops.geojson' has been created.")
