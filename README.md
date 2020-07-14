# Cosmos DB trigger in Python to get new documents in database, process them and send sms notifications

Cosmos DB trigger in Python to get new documents saved and store them in CosmosDB using SQL API

This is a Cosmos DB trigger function written in Python in Visual Studio Code as the editor. It waits until a document creates in the database, process it and send notifications to a mobile phone

## Technology stack  
* Python version 3.8.2 64 bit version https://www.python.org/downloads/release/python-382/
* Azure functions for python version 1.2 *(azure-functions 1.2.0)* https://pypi.org/project/azure-functions/
* Requests version 2.24.0, to handle GET and POST requests *(pip install requests)* https://pypi.org/project/requests/

## How to run the solution
 * You have to create a Cosmos DB account with SQL API and go to the Connection String section and get the connectionstring to connect to the database, And then provide the database name and collection name in the *function.json* file 
 * Open the solution from Visual Studio code, create a virtual environment to isolate the environment to the project by running, *py -m venv .venv* command. It will install all the required packages mentioned in the *requirements.txt* file
 * Type *func start* in the terminal window to start the function app

 ## Code snippets
 
 ### Cosmos DB trigger to track the document changes
 ```
 import logging
import azure.functions as func
import requests

def main(documents: func.DocumentList) -> str:
    logging.info('hello')
    if documents:
        logging.info('Document id: %s', documents[0]['id'])
        vehicleNo = documents[0]['vehicleNumber']
        speed = documents[0]['speed']
        city = documents[0]['city']
        mobile = documents[0]['mobile']

    if speed > 80 :
        message = 'High speed detected in {0}, Vehicle No {1} and Speed {2},'.format(city, vehicleNo, speed)
        logging.info(message)
        sendNotifications(mobile, message)
 ```
 
 ### Send sms notification using SMS API, https://www.notify.lk/
 ```
 def sendNotifications (mobile, message) :
    url = 'https://app.notify.lk/api/v1/send'
    
    userId = "";
    APIKey = "";
    senderId = "";
    
    data = {'user_id': userId, 'api_key' : APIKey, 'sender_id' : senderId, 'to' : mobile, 
      'message' : message} 

    result = requests.post(url, data = data)
    logging.info(result)
 ```
