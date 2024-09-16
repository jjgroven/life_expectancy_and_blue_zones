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

#Drop unneccesary columns
#This file is huge. Most of the clearning will concern weeding down to only the necessary data.
HNP_stats = HNP_stats.drop(columns=['Indicator Code'])

#The structure of this data inherantly has years across the columns and
#attributes down the column "Indicator Name"
#This should be flipped
#This will make the year column in to a single column with matching values
yearColumns = HNP_stats.columns[3:]
HNP_stats = pd.melt(HNP_stats, id_vars=['Country Name','Country Code','Indicator Name'], 
                    value_vars=yearColumns, ignore_index=False)
#Correct Column names after transition
HNP_stats = HNP_stats.rename(columns={'variable':'Year', 'value':'Value'})

#Review how many indicators there are:
#HNP_stats["Indicator Name"].value_counts()
#470 indicators

#Now pivot the indicators so that they become the columns
HNP_stats = HNP_stats.pivot_table(index=['Country Name','Country Code','Year'], 
                                  columns='Indicator Name', values='Value').reset_index()

#Review a list of the indicators to help consider what to keep:
HNP_stats.columns.tolist()

keepColumns = ['Country Name',
               'Country Code',
               'Year',
               'Adults (ages 15+) and children (0-14 years) living with HIV',
               'Cause of death, by non-communicable diseases (% of total)',
               'Diabetes prevalence (% of population ages 20 to 79)',
               'Domestic general government health expenditure (% of GDP)',
               'Domestic general government health expenditure per capita (current US$)',
               'Life expectancy at birth, total (years)',
               'Mortality from CVD, cancer, diabetes or CRD between exact ages 30 and 70 (%)',
               'People practicing open defecation (% of population)',
               'People using safely managed drinking water services (% of population)',
               'People using safely managed sanitation services (% of population)',
               'People with basic handwashing facilities including soap and water (% of population)',
               'Physicians (per 1,000 people)',
               'Population ages 80 and above, male (% of male population)',
               'Population ages 80 and older, female (% of female population)',
               'Population, total',
               'Poverty headcount ratio at national poverty line (% of population)',
               'Prevalence of HIV, total (% of population ages 15-49)',
               'Prevalence of overweight (% of adults)',
               'Prevalence of undernourishment (% of population)',
               'Proportion of population spending more than 10% of household consumption or income on out-of-pocket health care expenditure (%)',
               'Proportion of population spending more than 25% of household consumption or income on out-of-pocket health care expenditure (%)',
               'Total alcohol consumption per capita (liters of pure alcohol, projected estimates, 15+ years of age)'
              ]

#Build a dataframe with only desired columns
HNP_stats_selected = HNP_stats[keepColumns]

#Merge in the API countryInfo  on Country Code
HNP_stats_selected = HNP_stats_selected.merge(countryInfo, how='inner', on='Country Code')

#Save a separate dataframe with world-level data in case needed
HNP_stats_world = HNP_stats_selected[HNP_stats_selected['Country Name'] == 'World']

#There are additional items in the countries list that are not countries
#There are regions, territories, and other summaries included.
#Make a list to filter these out of the country dataset
regionsList = ["Africa Eastern and Southern",
               "Africa Western and Central",
               "Arab World",
               "Central Europe and the Baltics",
               "Early-demographic dividend",
               "East Asia & Pacific",
               "East Asia & Pacific (IDA & IBRD countries)",
               "East Asia & Pacific (excluding high income)",
               "Euro area",
               "Europe & Central Asia",
               "Europe & Central Asia (excluding high income)",
               "Europe & Central Asia (IDA & IBRD countries)",
               "European Union",
               "Fragile and conflict affected situations",
               "Heavily indebted poor countries (HIPC)",
               "High income",
               "IDA & IBRD total",
               "IDA blend",
               "IDA only",
               "Late-demographic dividend",
               "Lower middle income",
               "Low & middle income",
               "Low income",
               "Middle income",
               "Latin America & Caribbean",
               "Latin America & Caribbean (excluding high income)",
               "Latin America & the Caribbean (IDA & IBRD countries)",
               "Least developed countries: UN classification",
               "Low income",
               "Hong Kong SAR, China",
               "Macao SAR, China",
               "Middle East & North Africa",
               "Middle East & North Africa (excluding high income)",
               "Middle East & North Africa (IDA & IBRD countries)",
               "OECD members",
               "Other small states",
               "Post-demographic dividend",
               "Pre-demographic dividend",
               "East Asia and the Pacific",
               "Europe and Central Asia",
               "Latin America and the Caribbean",
               "Middle East and North Africa",
               "North America",
               "Small states",
               "Sub-Saharan Africa",
               "Sub-Saharan Africa (IDA & IBRD countries)",
               "Sub-Saharan Africa (excluding high income)",
               "South Asia",
               "Sub-Saharan Africa",
               "World",
               "South Asia (IDA & IBRD)",
               "Upper middle income",
               "West Bank and Gaza",
               "Aruba",
               "Curacao",
               "Bahamas, The",
               "British Virgin Islands",
               "Carribean small states",
               "Channel Islands",
               "French Polynesia",
               "Guam",
               "Isle of Man",
               "Kosovo",
               "New Caledonia",
               "Pacific Islands small states",
               "Sint Maarten (Dutch part)",
               "St. Martin (French part)",
               "St. Vincent and the Grenadines",
               "Turks and Caicos Islands",
               "Virgin Islands (U.S.)",
               "Cayman Islands"
               ]

HNP_stats_selected = HNP_stats_selected[(HNP_stats_selected['Country Name'].isin(regionsList) == False)]


#Review the data:
#Everything is in the proper data type.

HNP_stats_selected.info()

#Review the missing data:
#Review of missing data by years
HNP_Stats_missing = HNP_stats_selected.groupby(['Year']).count()
HNP_Stats_missing

#Much of the data isn't provided annually back to 1960s.
#This data is informed by several reports that appear to have different collection cycles.
#Best way to handle this data will be to review key time points that have more alignment in collection
#Let's take 1990, 2000, 2010, 2015, and 2020.

#For some reports, they were collected in 2019 or 2021, 
#Leaving the year 2020 empty. 
#We should resolve these empty results by reviewing the null values in 2020
#and checking for a value that can be pulled forward from 2019 or backwards from 2021.
#For this project that will be accurate enough:
import numpy as np

for index in HNP_stats_selected.index:#For all rows in the datafram
    if HNP_stats_selected["Year"][index] == "2020":#if the year is 2020
        #print(index)
        for column in HNP_stats_selected.columns:#Look across all columns
            if str(HNP_stats_selected[column][index]) == "nan":#if a value is nan
                #print(HNP_stats_selected[column][index])
                HNP_stats_selected.loc[index,column] = HNP_stats_selected.loc[index-1,column] #Substitute for the previous year
                #print(HNP_stats_selected.loc[index, column])
            if str(HNP_stats_selected[column][index]) == "nan":#if the cell is still empty
                #print(HNP_stats_selected[column][index])
                HNP_stats_selected.loc[index,column] = HNP_stats_selected.loc[index+1,column]#Try the following year
                #print(HNP_stats_selected.loc[index, column])

#Review missing data again. 
HNP_Stats_missing2 = HNP_stats_selected.groupby(['Year']).count()
HNP_Stats_missing2


#identify that the aim is to use data from 1990, 2000 2010, 2015, and 2020.
#Build dataframe of only this data.
keyYears = HNP_stats_selected[(HNP_stats_selected["Year"] == "1990")|
                                        (HNP_stats_selected["Year"] == "2000")|
                                        (HNP_stats_selected["Year"] == "2010")|
                                        (HNP_stats_selected["Year"] == "2015")|
                                        (HNP_stats_selected["Year"] == "2020")]
keyYears

###Remaining cleaning will be done in smaller chunks to maximize information in specific contexts.

#ChronicIllnesses
#Pull data related to chronic illnesses
chronicIllness = keyYears[['Country Name',
                            'Year',
                            'Life expectancy at birth, total (years)',
                            'Adults (ages 15+) and children (0-14 years) living with HIV',
                            'Cause of death, by non-communicable diseases (% of total)',
                            'Diabetes prevalence (% of population ages 20 to 79)',
                            'Mortality from CVD, cancer, diabetes or CRD between exact ages 30 and 70 (%)',
                            'Prevalence of HIV, total (% of population ages 15-49)']]
chronicIllness

#After review of missing values
#Drop Diabetes Prevalence, not enough records
chronicIllness = chronicIllness.drop(columns=['Diabetes prevalence (% of population ages 20 to 79)'])
chronicIllness

#After review of missing data by decade
#chronicIllness.info()
#chronicIllness[chronicIllness["Year"] =="1990"].info()
#chronicIllness[chronicIllness["Year"] =="2000"].info()
#chronicIllness[chronicIllness["Year"] =="2010"].info()
#chronicIllness[chronicIllness["Year"] =="2015"].info()
#chronicIllness[chronicIllness["Year"] =="2020"].info()
#Remove 1990's data from data set.
chronicIllness  = chronicIllness[chronicIllness["Year"] != "1990"]

#Review missing data by country
#Some counties are entirely left out of the surveys.
#Drop countries that have no data across the health metrics
chronicIllness  = chronicIllness.dropna()
#Leaves 567 records

#Alcohol Consumption
alcoholUse = keyYears[['Country Name',
                       'Year',
                       'Life expectancy at birth, total (years)',
                       'Total alcohol consumption per capita (liters of pure alcohol, projected estimates, 15+ years of age)'
                            ]]
#Not reported for all countries across all years
alcoholUse = alcoholUse.dropna()
#Leaves 742 records


#Public Health
publicHealth = keyYears[['Country Name',
                         'Year',
                         'Life expectancy at birth, total (years)',
                         'People practicing open defecation (% of population)',
                         'People using safely managed drinking water services (% of population)',
                         'People using safely managed sanitation services (% of population)']]
                         #'Physicians (per 1,000 people)']]
#Upon data preview seeing the same patterns than 1990 is not 
#well documented
publicHealth  = publicHealth[publicHealth["Year"] != "1990"]

#Not enough records for Physican (per 1,000 people), removed from data frame above

publicHealth = publicHealth.dropna()
#Leaves 412 records


#Government Investment
economicCost = keyYears[['Country Name',
                        'Year',
                        'Life expectancy at birth, total (years)',
                        'Domestic general government health expenditure (% of GDP)',
                        'Domestic general government health expenditure per capita (current US$)']]
                        #'Proportion of population spending more than 10% of household consumption or income on out-of-pocket health care expenditure (%)',
                        #'Proportion of population spending more than 25% of household consumption or income on out-of-pocket health care expenditure (%)']]
#economicCost  = economicCost[economicCost["Year"] != "1990"]

#Not sufficient records in 1990 and in these two household consumption columns.
#Remove from data frame
economicCost = economicCost.dropna()
#Leaves 728 records
