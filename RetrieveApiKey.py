import sys

class RetrieveApiKey():

    #constructor
    def __init__(self):
        # get current working directory with sys.path[0]
        path = sys.path[0]+'\\apiKey.txt'
        #open file
        file = open(path, 'r')
        #read api key into variable
        self.apiKey = file.read()

    #getter
    def getApiKey(self):
        return self.apiKey



