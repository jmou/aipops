import csv
import os
import sys

def transpose_csv(input_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    with open(input_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pops_number = row['pops_number']
            filename = os.path.join(output_dir, f"{pops_number}")
            
            with open(filename, 'w') as envfile:
                for key, value in row.items():
                    # Replace newlines and quotes in the value
                    value = value.replace('\n', '\\n').replace('"', '\\"')
                    envfile.write(f'{key}="{value}"\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python transpose.py <input_csv_file> <output_directory>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_dir = sys.argv[2]
    transpose_csv(input_file, output_dir)
    print(f"Transposed {input_file} into individual .env files in {output_dir}.")
