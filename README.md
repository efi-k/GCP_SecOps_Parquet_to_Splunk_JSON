# GCP_SecOps_Parquet_to_Splunk_JSON

# Parquet to JSON Lines Converter for Splunk Ingestion

This Python script provides a robust solution for converting Apache Parquet files into JSON Lines (newline-delimited JSON) format, specifically optimized for ingestion into Splunk. It includes comprehensive data cleaning to ensure UTF-8 compatibility and proper serialization of various data types, preventing common ingestion issues.

## Features

* **Parquet to JSON Lines Conversion**: Efficiently transforms Parquet files into a streamable JSON Lines format, where each line is a valid JSON object representing a single record.
* **Splunk Ingestion Ready**: The output format and data cleaning procedures are tailored to facilitate smooth data ingestion into Splunk.
* **Comprehensive Data Cleaning**:
    * Handles `bytes` objects by decoding them to UTF-8 strings.
    * Converts `NumPy` arrays to standard Python lists.
    * Recursively cleans nested lists and dictionaries.
    * Ensures all string data is UTF-8 compatible, replacing problematic characters where necessary.
    * Manages `None`, `float`, and `int` values for JSON serialization.
* **Flexible Input**: Can accept Parquet files, even if they misleadingly have a `.csv` file extension.

## Prerequisites

Before running this script, you need to have Python installed on your system. The script also relies on the following Python libraries:

* `pandas`: For data manipulation and reading/writing Parquet and JSON.
* `pyarrow`: The underlying engine used by pandas to read Parquet files.
* `numpy`: Used for handling numerical data, especially NumPy arrays, within the data cleaning process.

## Installation

You can install the required libraries using `pip`:

```bash
pip install pandas pyarrow numpy
