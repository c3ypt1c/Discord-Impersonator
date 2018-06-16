from selenium import webdriver
from random import random
import os
import time #For timing

print ( "This path:", os.getcwd() )
print ( "Creating classes and function" )

LoginConfigChanged = False
try:
    import Login
    LoginConfigChanged = Login.changed
    if not Login.changed:
        del Login
        print ( "Default file not changed, not using data..." )
    else:
        print ( "Using data in Login.py" )
except:
    print ( "Login.py not found, creating..." )
    f = open( "LoginTemplate.txt", "rb" )
    fd = f.read()
    f.close()
    f = open( "Login.py", "wb" )
    f.write(fd)
    f.close()
    del f

class Methods:
    global avoidBotBehaviour
    avoidBotBehaviour = 1 #Set to 1 or 0 
    
    def HumanTyping(element, text, scale=0.33):
        global avoidBotBehaviour
        for x in text:
            element.send_keys(x);
            time.sleep(random()*scale*avoidBotBehaviour)
        
class URL:
    class discord:
        discord = "https://discordapp.com/"
        login = "https://discordapp.com/login"



print ( "Loading driver" )
driver = webdriver.Firefox(os.getcwd());
print ( "Loading", URL.discord.discord )
driver.get(URL.discord.discord)
print ( "Loading", URL.discord.login )
driver.get(URL.discord.login)
print ( "Finding elements" )
root = driver.find_element_by_id("app-mount")
root = root.find_elements_by_class_name("platform-web")[0]
root = root.find_elements_by_xpath("div/div/div")[0]
root = root.find_elements_by_xpath("form/div")[0]
root = root.find_elements_by_xpath("*")[2]
root = root.find_elements_by_xpath("*")
login = root[0].find_elements_by_xpath("div/input")[0]
passw = root[1].find_elements_by_xpath("div/input")[0]
accep = root[3]

print ( "Injecting login data..." )
if not LoginConfigChanged:
    print ( "The following needs your input:" )

if LoginConfigChanged:
    Methods.HumanTyping(login, Login.email)
else:
    Methods.HumanTyping(login, input("Email> ") )

if LoginConfigChanged:
    Methods.HumanTyping(passw, Login.password)
else:
    Methods.HumanTyping(login, input("Password> ") )

accep.click()
