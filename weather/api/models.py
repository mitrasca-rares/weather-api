from django.conf import settings 
from django.db import models
from django.contrib.auth.models import User
import datetime, time

import json
from statistics import mean
from scipy.constants import convert_temperature

import requests

# Create your models here.
class Location(models.Model):
    owner = models.ForeignKey(User, related_name='locations', on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)

    @property
    def aggregation(self):
        #get all parameters of this location
        #print('Location: ', self.id)
        aggr = Parameter.objects.filter(location=self.id)
        aggr_list = []
        for param in aggr:
            values = param.values
            if values:
                max_val = max([x['value'] for x in values])
                min_val = min([x['value'] for x in values])
                avr_val = round(mean([x['value'] for x in values]),2)
                aggr_list.append({
                    'id': param.id,
                    'name': param.name,
                    "avg": avr_val,
                    "min": min_val,
                    "max": max_val,
                    "units": param.unit
                    })
        return aggr_list

class Parameter(models.Model):
    name = models.CharField(max_length=20)
    location = models.ForeignKey(Location, related_name='parameters', on_delete=models.CASCADE)
    unit = models.CharField(max_length=10)
    api_id = models.CharField(max_length=20)

    @property
    def values(self):
        val = {}
        try:
            url = settings.EXTERNAL_API
            headers = settings.EXTERNAL_API_HEADERS
            date = datetime.datetime.now() - datetime.timedelta(minutes=5)
            epoch = int(time.mktime(date.timetuple()))
            querystring = {"lat":str(self.location.lat),"lon":str(self.location.lon),"dt":str(epoch)}
            
            #print(querystring)
            response = requests.request("GET", url, headers=headers, params=querystring)
            #print(response.text)
            s_val = []
            if response.status_code == requests.codes.ok:
                val = json.loads(response.text)
                
                for e in val['hourly']:
                    if self.api_id in e:
                        # convert units
                        conv_val = e[self.api_id]
                        if self.api_id == 'temp':
                            conv_val = round(convert_temperature(e[self.api_id], 'Kelvin', self.unit),2) 

                        # insert value in list
                        s_val.append({'dt': e['dt'], 'value':conv_val})
            return s_val 
        except Exception as e:
            print(e)
        return response.text