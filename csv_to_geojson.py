import csv
import json
import sys

def load_footprints(footprints_file):
    with open(footprints_file, 'r') as f:
        footprints_data = json.load(f)
    
    footprints = {}
    for feature in footprints_data['features']:
        bin_value = feature['properties'].get('bin')
        if bin_value:
            footprints[int(bin_value)] = feature['geometry']
    
    return footprints

def csv_to_geojson(csv_file, geojson_file, footprints_file):
    features = []
    footprints = load_footprints(footprints_file)

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
                
                # Check if there's a matching footprint
                bin_value = row.get('bin')
                if bin_value and bin_value.isdigit():
                    bin_int = int(bin_value)
                    if bin_int in footprints:
                        feature['geometry'] = footprints[bin_int]
                
                features.append(feature)

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    with open(geojson_file, 'w') as outfile:
        json.dump(geojson, outfile, indent=2)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python csv_to_geojson.py <input_csv_file> <output_geojson_file> <footprints_geojson_file>")
        sys.exit(1)

    input_csv = sys.argv[1]
    output_geojson = sys.argv[2]
    footprints_geojson = sys.argv[3]
    csv_to_geojson(input_csv, output_geojson, footprints_geojson)
    print(f"GeoJSON file '{output_geojson}' has been created with merged footprint geometries.")
