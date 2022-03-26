import urllib.request
import urllib.parse
import ssl
import sys
import json
import threading
import os.path

SSL = ssl.create_default_context()
QUERY = {
    "vpn": "1",
    "asn": "1"
}
reals = 0 
proxies = 0
class Lookup:
    def __init__(self,api):
        self.req = urllib.request.Request(url=api,method='GET')
        self.req.add_header('cache-control', 'no-cache')
        self.req.add_header('connection', 'keep-alive')
        with urllib.request.urlopen(self.req,data=None,context=SSL)as f:
            self.jsonformat = f.read().decode('utf-8')

    def Response(self):
        return self.jsonformat
    @staticmethod
    def JSONReader(ip,dict_val):
        try:
            query = ip
            loadJSON = json.loads(dict_val)
            locateIn = loadJSON[query]

            proxy = locateIn['proxy']   
            return proxy
        except:
            return None

def Main(iplist,api):
    global reals, proxies
    getResponse = Lookup(api).Response()
    ReturnedData = Lookup.JSONReader(iplist,getResponse)

    if ReturnedData == "no":
        print(f"\033[38;5;206m{iplist}\033[38;5;205m : \033[32mReal IP\033[0m")
        reals += 1
    else:
        print(f"\033[38;5;206m{iplist}\033[38;5;205m : \033[31mIs a Proxy/VPN\033[0m")
        with open("detections.txt",'a+')as f:
            f.write(f"{iplist} : Is a Proxy/VPN\n")
            proxies += 1

def List(list):
    try:
        with open(f"{list}", "r")as f:
            ipsToCheck = f.read()
            StrippedSpace = ipsToCheck.strip(' ')

        return StrippedSpace.split('\n')
    except Exception as E:
        sys.exit(f'\033[31m{E}\033[0m')

if __name__ == '__main__':
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
    IpListToCheck = List(sys.argv[1])
    for ips in IpListToCheck:
        SafeQuery = urllib.parse.urlencode(QUERY)
        API = f"https://proxycheck.io/v2/{ips}?%s" % SafeQuery
        th = threading.Thread(target=Main(ips,API))
        th.start()
    print(f"\n\033[38;5;206mReal IPs: \033[32m{reals}\n\033[38;5;206mProxy/VPN: \033[31m{proxies}\033[0m")
