# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 15:25:24 2020

@author: dell
"""
import requests

class WeatherTest: 
    def __init__(self, url):
        self.url = url      

    def test_weather(self):
        req = requests.get(self.url)

        if req.status_code == 200:
            print("Request successful")
        elif req.status_code == 404:
            print("Request failed")
            
    def getHumidity(self):
        req = requests.get(self.url)
        res = req.json()
        nineDay = res["forecast_detail"]
        humidity = str(nineDay[1]["min_rh"]) + " - " + str(nineDay[1]["max_rh"]) + "%"
        print("Humidity of the day after tomorrow is: " + humidity)

test = WeatherTest('http://gbpda.weather.gov.hk/locspc/data/fnd_uc.xml')
test.test_weather()
test.getHumidity()