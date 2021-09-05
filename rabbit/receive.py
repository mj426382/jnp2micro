#!/usr/bin/env python
import pika, sys, os

import requests

import json

def return_string(body, itter):
    ret = ''
    for element in range(itter, len(body)):
        if chr(body[element]) == '~':
            break
        ret = ret + chr(body[element])
        
    return ret
    
def return_itter(body, itter):
    i = itter
    for element in range(itter, len(body)):
        if chr(body[element]) == '~':
            break
        i += 1
        
    return i + 1

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='rabbit')

    def callback(ch, method, properties, body):
        itter = 0;
        coowner = return_string(body, 0)
        itter = return_itter(body, itter)
        project_name = return_string(body, itter)
        itter = return_itter(body, itter)
        date = return_string(body, itter)
        json_data = {
            'coowner': coowner,
            'project_name': project_name,
            'date': date
        }
        print(json_data)
        response = requests.post('http://127.0.0.1:8000/polls/notification/',data=json_data)

    channel.basic_consume(queue='rabbit', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)