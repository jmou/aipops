# Makefile for generating GeoJSON from CSV

# Variables
CSV_FILE = pops.csv
GEOJSON_FILE = pops.geojson
PYTHON = python3

# Default target
all: $(GEOJSON_FILE)

# Variables
FOOTPRINTS_FILE = footprints.geojson

# Rule to generate GeoJSON from CSV
$(GEOJSON_FILE): $(CSV_FILE) csv_to_geojson.py $(FOOTPRINTS_FILE)
	$(PYTHON) csv_to_geojson.py $(CSV_FILE) $(GEOJSON_FILE) $(FOOTPRINTS_FILE)

# Clean target to remove generated files
clean:
	rm -f $(GEOJSON_FILE)

.PHONY: all clean
