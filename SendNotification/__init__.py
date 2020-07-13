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

def sendNotifications (mobile, message) :
    url = 'https://app.notify.lk/api/v1/send'
    
    userId = "";
    APIKey = "";
    senderId = "";
    
    data = {'user_id': userId, 'api_key' : APIKey, 'sender_id' : senderId, 'to' : mobile, 'message' : message} 

    result = requests.post(url, data = data)
    logging.info(result)