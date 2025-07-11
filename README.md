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

## Handling timestamp when ingesting to Splunk

To have Splunk extract the timestamp from the JSON field "event_timestamp" when uploading data via Add Data, you'll need to configure Splunk to recognize and parse this custom timestamp format, as Splunk does not natively extract timestamps from nested JSON fields in this structure by default.

Key Points
Your timestamp is in epoch seconds (e.g., 1751871976), nested inside an object, not as a top-level field.

By default, Splunk expects timestamps in common formats or as top-level fields, so custom configuration is needed.

Solution Steps

Configure props.conf for Custom Timestamp Extraction
You need to tell Splunk how to find and interpret your timestamp. This is done via the props.conf file:

TIME_PREFIX: Regex pattern before the timestamp value.

TIME_FORMAT: Format of the timestamp (epoch seconds = %s).

MAX_TIMESTAMP_LOOKAHEAD: How many characters ahead Splunk reads to find the timestamp.

Example configuration:

text
[your_sourcetype]
TIME_PREFIX = "event_timestamp":\{"seconds":
TIME_FORMAT = %s
MAX_TIMESTAMP_LOOKAHEAD = 20

TIME_PREFIX tells Splunk to look for the string preceding the epoch seconds value.

TIME_FORMAT = %s tells Splunk to interpret the value as epoch seconds (UNIX time).

Adjust MAX_TIMESTAMP_LOOKAHEAD if your JSON structure is more complex or the value appears further in the line.

