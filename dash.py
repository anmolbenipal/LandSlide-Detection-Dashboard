import pandas as pd
import os

def merge_csv_files(input_folder, output_file):
    # Create an empty DataFrame to store merged tilt data
    merged_tilt_data = pd.DataFrame()

    # Iterate through each file in the input folder for tilt data
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.csv') and ('DG1' in file_name or 'DG2' in file_name or 'DG3' in file_name):
            file_path = os.path.join(input_folder, file_name)
            # Read each CSV file into a DataFrame
            data = pd.read_csv(file_path)
            # Merge based on date and time
            merged_tilt_data = pd.concat([merged_tilt_data, data], ignore_index=True)
            print("Tilt data merged successfully!")

    # Merge rows with the same date and time
    merged_tilt_data = merged_tilt_data.groupby(['Date Time (UTC+08:00)']).sum().reset_index()

    # Write the merged tilt DataFrame to a new CSV file
    merged_tilt_data.to_csv(output_file, index=False)
    print(f"Merged tilt files successfully! Output file: {output_file}")

def merge_crack_files(input_folder, output_file):
    # Create an empty DataFrame to store merged crack data
    merged_crack_data = pd.DataFrame()

    # Iterate through each file in the input folder for crack data
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.csv') and ('CM01' in file_name or 'CM02' in file_name or 'CM03' in file_name or 'CM04' in file_name):
            file_path = os.path.join(input_folder, file_name)
            # Read each CSV file into a DataFrame
            data = pd.read_csv(file_path)
            # Merge based on date and time
            merged_crack_data = pd.concat([merged_crack_data, data], ignore_index=True)
            print("Crack data merged successfully!")

    # Merge rows with the same date and time
    merged_crack_data = merged_crack_data.groupby(['Date Time (UTC+08:00)']).sum().reset_index()

    # Write the merged crack DataFrame to a new CSV file
    merged_crack_data.to_csv(output_file, index=False)
    print(f"Merged crack files successfully! Output file: {output_file}")

# Provide the input folder containing CSV files and the output file names for tilt and crack data
input_folder = r'C:\Users\hp\OneDrive\Documents\5th SEM\newwww'
output_tilt_file = r'C:\Users\hp\OneDrive\Documents\5th SEM\newwww\merged_files\merged_tilt.csv'
output_crack_file = r'C:\Users\hp\OneDrive\Documents\5th SEM\newwww\merged_files\merged_crack.csv'

# Merge CSV files for tilt and crack data
merge_csv_files(input_folder, output_tilt_file)
merge_crack_files(input_folder, output_crack_file)