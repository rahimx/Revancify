from re import compile
from sys import argv, stderr
from requests import get, Session
from bs4 import BeautifulSoup


def fetchurl(url):
    return BeautifulSoup(Session().get(url, headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.86 Mobile Safari/537.36'}).content, 'html.parser')

try:

    appurl=f'https://www.apkmirror.com/apk/{argv[1]}/{argv[2]}/{argv[2]}-{argv[3]}-release/'


    data = fetchurl(appurl).find(['div'], class_='variants-table').find_all(['div'], string=compile(f'{argv[4]}|universal|noarch'))

    for element in data:
        if element.parent.find(['span']).string == "APK":
            appurl2 = f"https://apkmirror.com{element.parent.find(['a'], class_='accent_color')['href']}"

    print(33, flush=True)

    appurl3= f"https://apkmirror.com{fetchurl(appurl2).find(['a'], { 'class' : compile('accent_bg btn btn-flat downloadButton')})['href']}"

    print(66, flush=True)
    appdllink = f"https://apkmirror.com{fetchurl(appurl3).find(rel='nofollow')['href']}"
    print(100, flush=True)

    stderr.write(f'{appdllink}\n')

except NameError:
    stderr.write("noapk")
    exit()

except AttributeError:
    stderr.write("noversion")
    exit()

except:
    stderr.write("error")