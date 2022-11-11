#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 17:54:16 2022

@author: karthikshivaprasad
"""


import pandas as pd 
import matplotlib.pyplot as plt

def main():
    '''The function is used to read the whole data from csv file '''
    data=pd.read_csv("/Users/karthikshivaprasad/Downloads/vyshakpgm/uk_climate_data_new.csv")
    return data

def fgsize():
    ''' The function is used to plot the figure in 13,7 size '''
    plt.figure(figsize=(13,7))
    
def lineplot():
    ''' The function is used to plot the line graph'''
    fgsize()
    # by calling main function  it can return whole data into variable name data 
    data=main()
    plt.title("MAXIMUM AIR TEMPRATURE IN SPRING,SUMMER AND AUTUMN FROM 1884 T0 2021",fontsize=18)
    # by avoiding white space in the starting of graph to provide a range between 1884 to 2040
    plt.xlim([1884,2040])
    # first line  plot plots year in x axis and spring maximum temprature in y axis 
    plt.plot(data["year"],data["spr"] ,linestyle='--', label="spring")
    # second line plot plots year in x axis and summer maximum temprature in y axis 
    plt.plot(data["year"],data["sum"],label="summer")
    # third line  plot plots year in x axis and autumn maximum temprature in y axis 
    plt.plot(data["year"],data["aut"],label="autumn")
    plt.xlabel("YEAR")
    plt.ylabel("TEMPRATURE")
    plt.legend(loc="upper right")
    plt.show()
    
def barplot(): 
    ''' The function is used to plot the bar graph '''
    data=main()
    fgsize()
    # select all the rows where year is greater than 2014
    mask=data["year"]>2014
    plt.figure()
    plt.title("ANUAL MAXIMUM AIR TEMPRATURE  FROM 2015 T0 2022",fontsize=14)
    # plot the bar graph by using given data between the year 2015 to 2021
    # year in x axis and annual maximum temprature in y axis 
    plt.bar(data.loc[mask]["year"],data.loc[mask]["ann"],color='lightskyblue') 
    plt.xlabel("YEAR")
    plt.ylabel("TEMPRATURE IN DEGREE CELSIUS ")
    plt.xticks(rotation=30, horizontalalignment="center")
    plt.show()
    
def pieplot():
    ''' The function is used to plot pie chart '''
    data=main()
    fgsize()
    plt.figure()
    mask=data["year"]>2014
    plt.title("MAXIMUM AIR TEMPRATURE IN JANUARY FROM 2015 T0 2022",fontsize=14)
    # plot pie cahrt of maximum temprature of janury from 2015 to 2022
    plt.pie(data.loc[mask]["jan"],labels=data.loc[mask]["year"], autopct='%1.1f%%', explode=[0,0,0,0,0,.3,0.2,0], shadow=True, startangle=90)
    plt.show()
    
lineplot()
barplot()
pieplot()
