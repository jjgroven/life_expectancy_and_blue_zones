### Collect data from an APU
#Source: Wold Bank API (https://datahelpdesk.worldbank.org/knowledgebase/articles/889386-developer-information-overview)
#Desciption: This API can be used to capture information on countries, 
#country codes, regions, and income status for each country

###import required packages
import requests
import json
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

###Build request for api query. Collect info on all Countries
URL = "https://api.worldbank.org/v2/country/all?per_page=500&format=json"
#print(URL)

#Request data from API sources, no login or authenication needed
response1 = requests.get(URL)
#print(response1)
jsontxt = response1.json()
#print(jsontxt)

#File to save json data into
filename = "CountryMetaData.csv"
MyFile = open(filename, "w")
WriteThis = "Country Code,Region,Income Level\n"
MyFile.write(WriteThis)
MyFile.close()

#Write for loop to iterate through country entries
## Open the file for append
MyFILE = open(filename, "a")

countries = jsontxt[1] #excluded some page information
## Go through the json text:
for country in countries:
    #print(country)
  
    id=country["id"]
    #print(id)

    #name=country["name"]
    #name=name.replace(',', '')
    #print(name)

    region=country["region"]["value"]
    #print(region)

    incomeLevel=country["incomeLevel"]["value"]
    #print(incomeLevel)

    WriteThis=str(id)+"," + str(region) + "," + str(incomeLevel) + "\n"

    MyFILE.write(WriteThis)

MyFILE.close()

countryInfo = pd.read_csv("/content/CountryMetaData.csv")


###Import next data source
#upload csv of health indicators and life expectancies
#Source: World Bank Open Data
#Description: This dataset include 470 measured indicators for global health
#ranging from education, prevalance of chronic illnesses, population statistics,
#mortality rates, cost of health care, etc. This data set will provide data used
#to test some of the key arguments for blue zones. 
#Available via download here: See "Bulk CSV Download" 
#(https://datacatalog.worldbank.org/search/dataset/0037652)

HNP_stats = pd.read_csv("/content/HNP_StatsCSV.csv")
HNP_stats.head(10)
