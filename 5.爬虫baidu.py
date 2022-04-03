import sys
sys.path.append('/home/aistudio/external-libraries')

import requests
import json
import time
import random
import urllib.request
import re

def  baitu_decode(str):
    res = ''
    special = ['_z2C$q', '_z&e3B', 'AzdH3F']
    table = {'w':'a', 'k':'b', 'v':'c', '1':'d', 'j':'e', 'u':'f', '2':'g', 'i':'h', 't':'i', '3':'j', 'h':'k', 's':'l', '4':'m', 'g':'n', '5':'o', 'r':'p', 'q':'q', '6':'r', 'f':'s', 'p':'t', '7':'u', 'e':'v', 'o':'w', '8':'1', 'd':'2', 'n':'3', '9':'4', 'c':'5', 'm':'6', '0':'7', 'b':'8', 'l':'9', 'a':'0', '_z2C$q':':', '_z&e3B':'.', 'AzdH3F':'/'}
    if (str == None) or ('http' in str):
        return str
    else:
        temp = str
        for s in special:
            temp = temp.replace(s,table[s])
        for c in temp:
            if re.match('^[a-w\d]+$',c):
                c = table[c]
            res= res+c
        return res

def get_page_image(url, keyword, num):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
    }

    payload = {
        'tn': 'resultjson_com',
        'ipn':'rj',
        'ct': '201326592',
        'is': '',
        'fp': 'result',
        'queryWord':keyword,
        'cl': '2',
        'lm': '-1',
        'ie': 'utf-8',
        'oe': 'utf-8',
        'adpicid': '',
        'st': '-1',
        'z': '',
        'ic': '0',
        'hd': '',
        'latest': '',
        'copyright': '',
        'word': keyword,
        's': '',
        'se': '',
        'tab': '',
        'width': '',
        'height': '',
        'face': '0',
        'istype': '2',
        'qc':'',
        'nc': '1',
        'fr':'',
        'expermode':'',
        'force':'',
        'pn': 0,
        'rn': 30,
        'gsm': 0,
    }

    payload['pn'] = int(num)*30
    payload['gsm'] = hex(int(num)*30)
    response = requests.get(url, params=payload, headers=header)
    img_num = payload['pn']
    jdata = json.loads(response.text)
    for i in range(30):
        img_url = baitu_decode(jdata['data'][i]['objURL'])
        print(img_url)
        try:
            urllib.request.urlretrieve(img_url,"/home/aistudio/data/img_{:02d}.jpg".format(img_num+i))
        except:
            print("-")
            continue
        finally:
            print("运行完毕")

with open('/tmp/pr0n.gif', 'wb') as f: 
    f.write(requests.get(uri).content) 

for j in range(5):
    get_page_image("https://image.baidu.com/search/acjson", "猫",j)
    time.sleep(3)
import requests
import json
import time
import random
import urllib.request
import re


def  baitu_decode(str):
    res = ''
    special = ['_z2C$q', '_z&e3B', 'AzdH3F']
    table = {'w':'a', 'k':'b', 'v':'c', '1':'d', 'j':'e', 'u':'f', '2':'g', 'i':'h', 't':'i', '3':'j', 'h':'k', 's':'l', '4':'m', 'g':'n', '5':'o', 'r':'p', 'q':'q', '6':'r', 'f':'s', 'p':'t', '7':'u', 'e':'v', 'o':'w', '8':'1', 'd':'2', 'n':'3', '9':'4', 'c':'5', 'm':'6', '0':'7', 'b':'8', 'l':'9', 'a':'0', '_z2C$q':':', '_z&e3B':'.', 'AzdH3F':'/'}
    if (str == None) or ('http' in str):
        return str
    else:
        temp = str
        for s in special:
            temp = temp.replace(s,table[s])
        for c in temp:
            if re.match('^[a-w\d]+$',c):
                c = table[c]
            res= res+c
        return res
		
def get_page_image(url, keyword, num):
    header = {
        'user-agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 74.0.3729.131Safari / 537.36'
    }

    payload = {
        'tn': 'resultjson_com',
        'ipn':'rj',
        'ct': '201326592',
        'is': '',
        'fp': 'result',
        'queryWord':keyword,
        'cl': '2',
        'lm': '-1',
        'ie': 'utf-8',
        'oe': 'utf-8',
        'adpicid': '',
        'st': '-1',
        'z': '',
        'ic': '',
        'hd': '',
        'latest': '',
        'copyright': '',
        'word': keyword,
        's': '',
        'se': '',
        'tab': '',
        'width': '',
        'height': '',
        'face': '0',
        'istype': '2',
        'qc':'',
        'nc': '1',
        'fr':'',
        'expermode':'',
        'force':'',
        'pn': 0,
        'rn': 30,
        'gsm': 0,
    }

    payload['pn'] = int(num)*30
    payload['gsm'] = hex(int(num)*30)
    response = requests.get(url, params=payload, headers=header)
    img_num = payload['pn']

    jdata = json.loads(response.text)
    for i in range(30):
        img_url = baitu_decode(jdata['data'][i]['objURL'])
        time.sleep(2)
        urllib.request.urlretrieve(img_url,"/home/aistudio/data/img_{:02d}.jpg".format(img_num+i))

for j in range(4):
    get_page_image("https://image.baidu.com/search/acjson", "猫",j)