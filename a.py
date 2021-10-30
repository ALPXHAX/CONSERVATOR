import urllib
import colorama
import json
colorama.init(autoreset=True)
print(colorama.Fore.GREEN+ """
  ALPXHAX's
   ____ ___  _   _ ____  _____ ______     ___  _____ ___  ____  
  / ___/ _ \| \ | / ___|| ____|  _ \ \   / / \|_   _/ _ \|  _ \ 
 | |  | | | |  \| \___ \|  _| | |_) \ \ / / _ \ | || | | | |_) |
 | |__| |_| | |\  |___) | |___|  _ < \ V / ___ \| || |_| |  _ < 
  \____\___/|_| \_|____/|_____|_| \_\ \_/_/   \_\_| \___/|_| \_\
                                                                     
 Available EVERYWHERE!  github.com/ALPXHAX
""")
print ("\r")
o=int(input("𝐒𝐞𝐥𝐞𝐜𝐭 𝐲𝐨𝐮𝐫 𝐨𝐩𝐭𝐢𝐨𝐧\n𝟏.𝐋𝐢𝐧𝐤 𝐒𝐡𝐨𝐫𝐭𝐧𝐞𝐫"))
if o==1:
    url="https://api.shrtco.de/v2/shorten?url="
    link=input("Enter your link without http// or https//: ")
    req1=urllib.request.urlopen(url+link)
    json_1=json.loads(req1.read())
    #checking json output
    if json_1['ok']=='true':
        print(f"Code of Shortned URL : {json_1['code']}")