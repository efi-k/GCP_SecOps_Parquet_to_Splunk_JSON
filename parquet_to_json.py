import pandas as pd
import argparse
import os
import sys
import json
import numpy as np

def clean_value(x):
    # Handle missing values for scalars
    if isinstance(x, (float, int, type(None))):
        if pd.isnull(x):
            return x
        return x
    # Convert bytes to UTF-8 string
    if isinstance(x, bytes):
        try:
            return x.decode('utf-8', errors='replace')
        except Exception:
            return str(x)
    # Convert NumPy arrays to lists
    if isinstance(x, np.ndarray):
        return [clean_value(i) for i in x.tolist()]
    # Recursively clean lists
    if isinstance(x, list):
        return [clean_value(i) for i in x]
    # Recursively clean dicts
    if isinstance(x, dict):
        return {k: clean_value(v) for k, v in x.items()}
    # Clean strings
    if isinstance(x, str):
        return x.encode('utf-8', 'replace').decode('utf-8', 'replace')
    # For other types, just return as is
    return x

def clean_string_columns(df):
    """
    Ensures all object columns are serializable and UTF-8 safe.
    """
    for col in df.select_dtypes(include=['object', 'string']):
        df[col] = df[col].apply(clean_value)
    return df

def parquet_to_json(parquet_file_path, json_file_path):
    try:
        print(f"Reading Parquet file: {parquet_file_path}")
        df = pd.read_parquet(parquet_file_path, engine='pyarrow')
        print(f"Successfully read {len(df)} records.")

        print("Cleaning object columns for UTF-8 and JSON compatibility...")
        df = clean_string_columns(df)

        print(f"Converting to JSON Lines format and saving to: {json_file_path}")
        df.to_json(json_file_path, orient='records', lines=True, force_ascii=False)
        print("Conversion completed successfully.")

    except Exception as e:
        print(f"Error during conversion: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Convert Parquet file (even with .csv extension) to JSON Lines for Splunk ingestion.')
    parser.add_argument('parquet_file', help='Path to the input Parquet file (even if it has .csv extension)')
    parser.add_argument('json_file', help='Path to the output JSON file')

    args = parser.parse_args()

    if not os.path.isfile(args.parquet_file):
        print(f"Error: Parquet file '{args.parquet_file}' does not exist.")
        sys.exit(1)

    parquet_to_json(args.parquet_file, args.json_file)

if __name__ == "__main__":
    main()
