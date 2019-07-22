# The World Bank countries Data API

## Overview

This project is a basic overview of how to perform a Data Analysis using APIs. In our case, the project uses the  income distribution of different countries in the world. This infomation is accessible though their link[data helpdesk worldbank](https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information).Our partical API is accesses using the API[Country Queries endpoint](http://api.worldbank.org/v2/countries) to request the data.

## Technology Used

1. Flask
2. Pandas
3. Seaborn
4. gunicorn
5. matplotlib

## Installation and set-up

1. Clone the project - git@github.com:bafiam/iRepoter-api.git
2. create a virtual environment using virtualenv.
3. Install the dependencies - pip install -r requirements.txt.

## Run the server

1. Next is to start the server with the command python run.py.
2. The server should be running on [localhost](http://127.0.0.1:5000)

## API Endpoints

API Endpoint | Functionality
------------ | -------------
GET/| Fetch all the countries data
GET/regions?name=region name| Fetch countries data based  on the region name
GET/plots?name=region name | Fetch countries data based on the region name and plot a glid based on the countries income levels in a region

### region name

Region | region name to be used in the URL query
------------ | -------------
 East Asia & Pacific| EAP
Latin America & Caribbean|LAC
Europe & Central Asia|ECA
Middle East & North Africa|MENA
South Asia|SA
North America|NA
Sub-Saharan Africa|SSA

## Reference

1. [Exploratory Data Analysis using APIs](https://medium.com/aseladassanayake/exploratory-data-analysis-using-apis-5cee03894d52)
2. [python-pandas-dataframe](https://www.geeksforgeeks.org/python-pandas-dataframe/)

## online access

To access the online version [heroku](https://world-bank-api.herokuapp.com/)

## Author

**Stephen Gumba**
