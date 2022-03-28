# Anti VPN
A fast asynchronous VPN & Proxy Detector. Reinforced with HTTP 2 version.

# Requirements
``httpx``
``httpx[http2]``

# Installation
``pip install -r requirements`` or
```
pip install httpx
pip install httpx[http2]
```

# Usage
```
python3 anti-vpn.py list.txt
```
list.txt should contain the IPs list you want to scan. Be sure every IP is formatted under newlines. For example:
```
ip1
ip2
ip3 and so on...
```
