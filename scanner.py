#!/usr/bin/python
import time    
import os
from os import system, name 
from time import sleep
import random
import threading
import requests
import cloudscraper
import sys
import colorama
import time
from colorama import Fore
class colors:
    black = Fore.LIGHTBLACK_EX
    blue = Fore.LIGHTBLUE_EX
    cyan = Fore.LIGHTCYAN_EX
    green = Fore.LIGHTGREEN_EX
    magenta = Fore.LIGHTMAGENTA_EX
    red = Fore.LIGHTRED_EX
    white = Fore.LIGHTWHITE_EX
    yellow = Fore.LIGHTYELLOW_EX
c = colors()
banner = c.cyan + """
  _____      _                  _____ _     _      _     _ 
 / ____|    | |                / ____| |   (_)    | |   | |
| |    _   _| |__   ___ _ __  | (___ | |__  _  ___| | __| |
| |   | | | | '_ \ / _ \ '__|  \___ \| '_ \| |/ _ \ |/ _` |
| |___| |_| | |_) |  __/ |     ____) | | | | |  __/ | (_| |
 \_____\__, |_.__/ \___|_|    |_____/|_| |_|_|\___|_|\__,_|
        __/ |                                              
       |___/                                                                                                                        
                        { v2.0.0 }

OmerSimko,Zhyar Muhamad,Safin Mohammed,Ahmad Abdulla,Muhammad Salah,Sarkar

"""

print(banner)

#sudo apt install python3-pip
#pip3 install cloudscraper
dir_path = os.path.dirname(os.path.realpath(__file__))
proxy_path = dir_path + '//' + 'Proxies.txt'
pages_path = dir_path + '//' + 'Pages.txt'
ext_path = dir_path + '//' + 'Extensions.txt'
paths_path = dir_path + '//' + 'Paths.txt'
proxyList=[]; 
loginPagesList=[]; 

# ////////////////////////////////////////////////////
        # StartSearching if the starting point
# ///////////////////////////////////////////////////


def CLS():
    if name == 'nt': 
        _ = system('cls')  
    else: 
        _= system('clear')
    
def readProxyList():
    proxyFile = open(proxy_path, 'r') 
    for proxy in proxyFile.readlines(): 
        proxyList.append(proxy.strip())
        #print(proxy.strip())

def readLoginList():
    loginFile = open(pages_path, 'r') 
    for login in loginFile.readlines(): 
        loginPagesList.append(login.strip())


def getRandomProxy():
    print("\033[94mGetting Working proxy\033[0m")
    if (proxyList != []):
    	while True:
    	    proxy=random.choice(proxyList)
    	    try:
    	        r = requests.get("https://google.com" , proxies={
    	                'http': "http://" + proxy,
    	                'https': "https://" + proxy,
     	           } , timeout=3 ) 

                print("\033[92mWorking Proxy Found!\033[0m")
    	        return proxy
    	    except:
            	continue
    else:
        print('The Proxy List Is Empty')


def sendRequest(url,timeout=3):
    global proxy

    proxies={
    	'http': "http://" + proxy,
    	'https': "https://" + proxy,
    }

    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    scraper = cloudscraper.create_scraper(
        browser={
            'browser': 'firefox',
            'mobile': False
        },
        debug=False,
        delay=timeout,
    ) 

    scraperGet=scraper.get(url=url)
    if scraperGet.status_code==200:
        result = url + ": \033[92mOK\033[0m"
        print(result)
    elif scraperGet.status_code==404:
        print(url + ": \033[91m404\033[0m")
        

readProxyList()
readLoginList()

def find_login_page(url, timeout):

    while(len(loginPagesList) > 0):
        page = get_page()
        sendRequest(url + page, 10000);


def get_page():
    temp = loginPagesList[0]
    loginPagesList.pop(0)
    return temp


proxy = getRandomProxy();
def StartSearching(url, thread = 5, timeout = 2000):

    # Chcek if the last letter of the url is (/) otherwise it'll be added
    if(url[-1] != "/"):
        url = url + "/"

    tList = []
    for i in range(thread):
        t = threading.Thread(target=find_login_page, args=(url, timeout))
        t.start()
        tList.append(t)

    for t in tList:
        t.join()


StartSearching("https://kurdsubtitle.net/", thread = 10, timeout = 2000)
