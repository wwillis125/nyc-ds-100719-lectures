#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:07:09 2019

@author: charleneawillis


"""
#data - where you will hold your data
#.length - that tells you the length of your data list
#.mean
##.median
#.variance
#.stand_dev
#Your class should have the following methods:

#.add_data() - which can take in a value or a list of values and extend the .data attribute
#.remove_data() accept a list of numbers and remove any of the numbers in that list from your object data
#Bonus:

#- calc_correlation(second_variable) this method should accept a list of data for the second variable, 
#and then calculate the correlation coefficient for the two variables.


class Calculator:
    def __init__(self):
        self.data = []
        self.length = len(self.data)
        self.mean = None
        self.median = None
        self.variance = 0
        self.stand_dev = None
    def add_data(self, new):
        # aooend causes data entered as list
        self.data.extend(new)
#        print(self.data)
        self.length = len(self.data)
#        print(self.length)
        self.mean = self.calc_mean()
        self.median = self.calc_med()
        self.variance = self.calc_var()
        self.stand_dev = self.calc_std()
    def remove_data(self):
        pass

    def calc_mean(self):
        return sum(self.data)/self.length    
    
    def calc_med(self):
        self.data = sorted(self.data)
        if self.length < 2:
            return self.data
        elif self.length % 2:
            return self.data[self.length//2]
        else:
            return (self.data[self.length//2] + self.data[(self.length//2)-1])/2
    
    def calc_var(self):
        variance = 0
        for x in self.data:
            variance += (x - self.calc_mean())**2
        return variance / self.length
        # print(self.variance)

    def calc_std(self):
        return self.calc_var()**.5
    
