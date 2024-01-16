import requests
import json
import subprocess
import time
from win11toast import toast


# Function to verify the avaiability of the shoe
def FindYourVansBySize(size, shoesUrl):
        shoesUrl = shoesUrl +  "-"+ str(size)
        response = requests.get(shoesUrl)

        if response.status_code == 200:
            # Finding the json in html
            begin = response.text.find("""props""")
            end = response.text.find("""scriptLoader""")
            begin = response.text.find("{", begin-3, begin)
            end = response.text.find("}", end) + 1
            
            # Turning the content into a json object
            VansJson = response.text[begin: end]
            jsonFromText = json.loads(VansJson)
            baseOptions = jsonFromText['props']['pageProps']['product']['baseOptions']
            
            # replacing "'" just to easily format on my text editor#
            # print(str(baseOptions).replace("'", '"' )) 

            for item in baseOptions:
                if item['variantType'] == "SizeVariantProduct":
                    if item['selected']['stock']['stockLevelStatus'] == "inStock":
                        return("Size " + str(size) + ": Cheguei!!!"), True
                    else:
                        return("Size " + str(size) + ": Não foi desta vez... :C"), False
                
        else:
            return(response.status_code), False
        
# Windows Notifications
def WindowsNotify(message, submessage, url):
    toast(message, submessage, url)

# Just a print with actual local time
def report(message):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time + ": " + message)


shoesUrl = "LINK HERE"
avaiable = False

# Core
subprocess.run('cls', shell = True)
print("Starting to look for your shoes!")

while not avaiable:
    # Clear the terminal

    msg, avaiable = FindYourVansBySize(39, shoesUrl)

    if avaiable:
        WindowsNotify(msg, "Click here to buy it!", shoesUrl)
        report(msg)
    else:
        report("Didn't find it yet, sorry :\ ")

    time.sleep(300)