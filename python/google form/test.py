import csv
import time
from selenium import webdriver

with open('name.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)
    print(csv_reader)
