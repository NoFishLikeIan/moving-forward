import pandas as pd 
import numpy as np
import wbdata
import pycountry_convert

from datetime import datetime, date, time, timedelta

class WBData():

    def __init__(self, 
                country_list = None,
                indicators = None,
                year = 2016):
        self.countries = ['Italy', 'France', 'United States', 'Japan'] if (country_list is None) else country_list       
        self.date = year (date(year[0],1,1), date(year[1],1,1)) if type(year) == tuple else date(year, 1, 1)

        if indicators != None:
            self.indicators = indicators

        else:
            self.indicators = { 
                  "SE.XPD.TERT.PC.ZS": "expenditure per student", 
                  "IC.REG.DURS": 'Time to start business', 
                  'IC.TAX.TOTL.CP.ZS': 'Commercial tax rate',
                  'NE.CON.PRVT.PP.CD': 'Houshold final consumption'
                  }
    
    def country_converter(self, countries):
        country_alpha3 = []
        for country in countries:
            if len(country) == 2:
                alpha3 = pycountry_convert.map_country_alpha2_to_country_alpha3()[country]                 
            elif len(country) == 3:
                alpha3 = country
            else:
                alpha3 = pycountry_convert.country_name_to_country_alpha3(country)
            
            if alpha3 not in country_alpha3:
                country_alpha3.append(alpha3)

        return country_alpha3

    def retrieve_data(self):
        self.df = wbdata.get_dataframe(self.indicators, 
                                country = self.country_converter(self.countries), 
                                data_date=self.date,
                                convert_date= True)

        self.df = self.df.reset_index().dropna(thresh = 0.9*len(self.df), axis = 1)

        return self.df