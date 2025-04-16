import urllib.request
import urllib.error
import json
import time

def sendWebexGET(url):
    request = urllib.request.Request(url,
                                     headers={"Accept": "application/json",
                                              "Content-Type": "application/json"})
    request.add_header("Authorization", "Bearer " + bearer)
    response = urllib.request.urlopen(request)
    return response

bearer = "PERSONAL_ACCESS_TOKEN"

while True:
    try:
        result = sendWebexGET('https://webexapis.com/v1/rooms')
        print(result.getcode(), time.time(), result.headers['Trackingid'])
        except urllib.error.HTTPError as e:
        if e.code == 429:
            print('code', e.code)
            print('headers', e.headers)
            print('Sleeping for', e.headers['Retry-After'], 'seconds')
            sleep_time = int(e.headers['Retry-After'])
            while sleep_time > 10:
                time.sleep(10)
                sleep_time -= 10
                print('Asleep for', sleep_time, 'more seconds')
            time.sleep(sleep_time)
        else:
            print(e, e.code)
            break
