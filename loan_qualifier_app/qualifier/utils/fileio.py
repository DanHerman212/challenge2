# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
from pathlib import Path
import sys
import csv
import fire
import questionary

def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

"""Modularized function to save CSV"""
def save_csv(bank_data,csvpath, header):
    """Args:
    bank_data - list of loans that meet the barrower criteris
    csvpath - location where the file will be saved
    header - uses pre-defined header to improve presentation
    """
    # opens CSV in "write mode", using csvpath as the location 
    with open(csvpath, "w", newline = "") as csvfile:
        
        # uses csvwriter to format output in CSV file
        csvwriter = csv.writer(csvfile, delimiter=",")
        csvwriter.writerow(header)

        # loops through every row in bank_data and writes to CSV
        for loan in bank_data:
                csvwriter.writerow(loan)

        