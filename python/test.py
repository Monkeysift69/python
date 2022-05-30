import csv
import time
from selenium import webdriver

with open('google form/name.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)
    
    for line in csv_reader:
        print(line)
