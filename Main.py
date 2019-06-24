import sys
from RetrieveApiKey import RetrieveApiKey
from ApiCall import ApiCall
from WeatherObject import WeatherObject

class Main():
    def __init__(self):
        #get ApiKey variable
        self.apiKey = RetrieveApiKey().getApiKey()
        self.verifyApiKey()
        self.cityName =''

        print('Welcome to the weather app')

        while self.cityName != '0':
            print('To view current weather please type city name below, to exit enter 0:')
            self.cityName = input()
            if(self.cityName != '0'):
                data = self.apiCall.sendRequest(self.cityName)

                if(self.apiCall.getStatus()):
                    self.weather = WeatherObject(data)
                    self.weather.printParameters()
        sys.exit()

    def verifyApiKey(self):
        self.apiCall = ApiCall(self.apiKey)
        #send sample request with default city to check if api key is correct
        data = self.apiCall.sendRequest('London')

        if(self.apiCall.getStatus() == False):
            print("Api key incorrect, please insert correct key and restart program")
            sys.exit()
        else:
            print("Api key correct!\n")



weatherApp = Main()
