import csv
import os

def transpose_csv(input_file):
    with open(input_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pops_number = row['pops_number']
            filename = f"{pops_number}.env"
            
            with open(filename, 'w') as envfile:
                for key, value in row.items():
                    # Replace newlines and quotes in the value
                    value = value.replace('\n', '\\n').replace('"', '\\"')
                    envfile.write(f'{key}="{value}"\n')

if __name__ == "__main__":
    input_file = 'pops.csv'
    transpose_csv(input_file)
    print(f"Transposed {input_file} into individual .env files.")
