import requests
import json
from urllib.error import URLError, HTTPError


class ApiCall():

    def __init__(self, apiKey):
        #set weather api URL
        self. apiUrl = 'http://api.openweathermap.org/data/2.5/weather?q='
        #set ApiKey
        self.apiKey = apiKey
        self.dataCorrect = False

    # def verifyApiKey(self):


    def sendRequest(self, city):
        try:
            #concatenate URL
            fullUrl = self.apiUrl+city+'&APPID='+self.apiKey+'&units=metric'
            #send request
            self.response = requests.request(method="get", url=fullUrl)
            #get response as json onject
            self.jsonResponse = self.response.json()

            #check status code
            if(self.response.status_code != 200):
                self.dataCorrect = False
                print(self.jsonResponse)
            else:
                self.dataCorrect = True
                return self.jsonResponse
        #check for errors
        except HTTPError as http_err:
            print(http_err.code)
            self.dataCorrect = False
        except Exception as err:
            print(err)
            self.dataCorrect = False

    def getStatus(self):
        return self.dataCorrect



