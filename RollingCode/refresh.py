import requests
import time

while True:
    try:
        response = requests.get('http://35.227.24.107/807a88557c/')
        if response.status_code == 200:
            print "GET: Status " + str(response.status_code) + " (success)"
        else:
            print "GET: Status " + str(response.status_code) + " (failed)"
    except Exception as e:
        print e
    time.sleep(30)
