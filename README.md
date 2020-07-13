# Cosmos DB trigger in Python to get new documents saved and store them in CosmosDB using SQL API

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
