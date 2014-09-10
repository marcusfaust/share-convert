__author__ = 'marcusfaust'


import csv


class uploadedCSV(file):

    def __init__(self):
        shares = []
        paths = []
        with open('tmp/tmp.csv', 'rb') as csvfile:
            sharescsv = csv.reader(csvfile, delimiter=',')
