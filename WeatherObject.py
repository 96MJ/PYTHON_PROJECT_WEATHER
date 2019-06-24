import json
from collections import namedtuple

class WeatherObject():
    def __init__(self, data):
        #dump json back to str
        self.strData = json.dumps(data)
        self.json = self.json2obj(self.strData)

    def json_hook(self, a):
        return  namedtuple('X', a.keys())(*a.values())

    def json2obj(self, data):
        #load data as json with custom dict
        return json.loads(data, object_hook=self.json_hook)

    def printParameters(self):
        print("Coordinates:")
        print("Latitude: " + str(self.json.coord.lat))
        print("Longitude: " + str(self.json.coord.lon))
        # print("Weather: " + self.json.weather.main)
        print("Temperature: " + str(self.json.main.temp))
        print("Pressure: " + str(self.json.main.pressure) + "hPa")
        print("Humidity: " + str(self.json.main.humidity) + "%")
        print("Cloudiness: " + str(self.json.clouds.all) + "%\n")
