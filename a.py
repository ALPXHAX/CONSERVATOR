import colorama
import json
import requests
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
o=int(input("𝐒𝐞𝐥𝐞𝐜𝐭 𝐲𝐨𝐮𝐫 𝐨𝐩𝐭𝐢𝐨𝐧\n𝟏.𝐋𝐢𝐧𝐤 𝐒𝐡𝐨𝐫𝐭𝐧𝐞𝐫\n\n\n\n----->"))
if o==1:
    url="https://api.shrtco.de/v2/shorten?url="
    link=str(input("Enter your link without http// or https//: "))
    final=url+link
    response=requests.get(final)
    if response["ok"]=='true':
        print(f"Code : {response['code']}")
        print(f"Link : {response['short_link']}")
        print(f"Share : {response['share_link']}")
    else:
        print("Error at processing the API")
else:
    print("Error")