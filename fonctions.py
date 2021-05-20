from csv import reader
import logging
import os
import re


logging.basicConfig(level=logging.DEBUG)


def read_csv(filename):
    """
    This function opens the csv file read it and divide the strings in 2 parts first 
    one as the restaurant name and 2 seconde one only for the restaurant working days and time
    """

    with open(filename, 'r') as f:
        liste = []
        csv_reader = reader(f)
        for row in csv_reader:
            resto = row[0]
            time = row[1]
            time = time.replace("/", "")
            data = resto, time
            #print(time)
            liste.append(data)  
        # print(liste)
    return liste



def open_food():
    """
    """
    datas = read_csv('rest_hours.csv')
    for i in datas:
        resto,time = i
        jour=time[:3]
        jours=time[4:7]
        tm = time.find("am")
        open_hour = time[7:tm]
        print (open_hour)
        

open_food()
            





