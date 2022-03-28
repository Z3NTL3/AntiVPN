import httpx
from urllib.parse import urlencode
import asyncio
import random
import json
import sys
import os

'''
This tool is written by Z3NTL3

Usage:
Replace the API key with your API KEY
API KEYS are free with 1000 USAGE DAILY

The same as `anti.py` but faster, with HTTP2 and ASYNC support
'''

APIDETAILS = {
    "key": "m310h2-841586-u9y197-815890",
    "vpn": "1",
    "asn": "1"
}
header = {
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/{random.randint(100,999)}.{random.randint(10,99)} (KHTML, like Gecko) Chrome/99.0.4844.88 Safari/{random.randint(100,999)}.{random.randint(10,99)}'
}
reals = 0 
proxies = 0

async def Lookup(ip):
    iplist = ip
    global reals, proxies, APIDETAILS
    SafeQuery = urlencode(APIDETAILS)
    API = f"https://proxycheck.io/v2/{ip}?%s" % SafeQuery

    with httpx.Client(http2=True, headers=header) as client:
        req = client.get(API)
        content_web = req.text
        httpver = req.http_version
    json_dict = json.loads(content_web)
    await asyncio.sleep(0)
    try:
        query = json_dict[f'{ip}']
        if query['proxy'] == "no":
            print(f"\033[38;5;206m{iplist}\033[38;5;205m : \033[32mReal IP \033[0m- \033[38;5;206mHTTP \033[38;5;207mVERSION: \033[38;5;219m{httpver}\033[0m")
            reals += 1
        else:
            print(f"\033[38;5;206m{iplist} : \033[31mIs a Proxy/VPN \033[0m- \033[38;5;206mHTTP \033[38;5;207mVERSION: \033[38;5;219m{httpver}\033[0m")
            with open("detections.txt",'a+')as f:
                f.write(f"{iplist} : Is a Proxy/VPN HTTP VERSION:{httpver}\n")
                proxies += 1
    except:
        print(f"\033[38;5;206m{iplist}\033[38;5;205m : \033[31mUncatched error occurred.\033[0m")
def List(list):
    try:
        with open(f"{list}", "r")as f:
            ipsToCheck = f.read()
            StrippedSpace = ipsToCheck.strip(' ')

        return StrippedSpace.split('\n')
    except Exception as E:
        sys.exit(f'\033[31m{E}\033[0m')

def Avoid():
    LOGO = """
\033[38;5;206m╔═╗╔╗╔╔╦╗╦  ╦  ╦╔═╗╔╗╔
\033[38;5;207m╠═╣║║║ ║ ║  ╚╗╔╝╠═╝║║║
\033[38;5;219m╩ ╩╝╚╝ ╩ ╩   ╚╝ ╩  ╝╚╝
\033[38;5;206mby Z\033[38;5;207m3NT\033[38;5;219mL3.
\033[38;5;206mUsage:
\033[38;5;207mpython anti.py ip\033[0m
""" 
    print(LOGO)
    if os.path.abspath(f'{sys.argv[1]}'):
        pass
    else:
        print(f"\033[31mError:\033[0m The file {sys.argv[1]} does not exist in the current directory.")

async def Start():
    Avoid()
    IpListToCheck = List(sys.argv[1])
    for check in IpListToCheck:
        await asyncio.gather(Lookup(check))

if __name__ == '__main__':
    '''
    By Z3NTL3 - SavageDevs.net
    '''
    loop = asyncio.get_event_loop()
    loop.run_until_complete(Start())

