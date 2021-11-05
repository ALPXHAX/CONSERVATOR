import colorama
import requests
import urllib
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
o=int(input("𝙎𝙚𝙡𝙚𝙘𝙩 𝙮𝙤𝙪𝙧 𝙤𝙥𝙩𝙞𝙤𝙣\n𝟏. 𝐋𝐢𝐧𝐤 𝐒𝐡𝐨𝐫𝐭𝐧𝐞𝐫\n𝟐. 𝐒𝐮𝐫𝐩𝐫𝐢𝐬𝐞\n\n\n\n----->"))
if o==1:
    url="https://shortlink.api.fayas.me/?query="
    link=str(input("Enter your link without http// or https//: "))
    request=urllib.request.urlopen(url+link)
    json_1=json.loads(request.read())
    print("\n\n\n")
    print(f"First Link : {json_1['chilp.it']}")
    print(f"Second Link : {json_1['click.ru']}")
    print(f"Third Link : {json_1['da.gd']}")
    print(f"Fourth Link : {json_1['is.gd']}")
    print(f"Fifth Link : {json_1['osdb.link']}")
    print(f"Sixth Link : {json_1['qps.ru']}")
    print("\n\nThanks for using the script")
if o==2:
    print("( ͡° ͜つ ͡°)╭∩╮")
    response=requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
    i = response.json()
    print(i['insult'])
    print("\n\nThanks for using the script")
    
