import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup

PROXY_SETTINGS_URL = "http://web.archive.org/"

class ProxySetter: 

    def __init__(self, proxyUrl, proxyPort): 
        self.proxyUrl = proxyUrl
        self.proxyPort = proxyPort
        self.proxyServers = { "http": "http://" + proxyUrl + ":" + proxyPort }
    
    def changeDate(self, date): 
        
        requestParams = {
            "date": date,
            "dateTolerance": 365,
            "gcFix": "on",
            "quickImages": "on",
            "ctEncoding": "on",
        }
        
        response = requests.get(PROXY_SETTINGS_URL, requestParams, proxies=self.proxyServers)
        if response.reason != "OK":
            raise Exception("Server did not accept date setting")       

        soup = BeautifulSoup(response.text, "html.parser")
        dateInputFields = soup.find(attrs={"name": "date"})
        
        confirmedDate = dateInputFields['value']
        
        return confirmedDate