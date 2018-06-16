from selenium import webdriver
from random import random
from selenium.webdriver.common.keys import Keys
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
            
    def SendMessage(element, message):
        print ( "Sending message:", message )
        Methods.HumanTyping(element, message+Keys.RETURN, scale=0.1)

        
class URL:
    class discord:
        discord = "https://discordapp.com/"
        login = "https://discordapp.com/login"
        
    try:
        import PrivateChannel
    except:
        f = open ( "PrivateChannel", "wb" )
        f.write(b"")
        f.close()
        import PrivateChannel

print ( "Loading driver" )
driver = webdriver.Firefox(os.getcwd());
print ( "Loading", URL.discord.discord )
driver.get(URL.discord.discord)
print ( "Loading", URL.discord.login )
driver.get(URL.discord.login)
print ( "Finding elements..." )
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
print ( "Waiting for Discord..." )
time.sleep(10) #TODO: Find progress!!!!!!

print ( "Going to dedicated channel..." )
driver.get(URL.PrivateChannel.URL)

print ( "Waiting for Discord..." )
time.sleep(10)

print ( "Gathering past data" )
pastData = set ( driver.find_elements_by_class_name("markup") )

print ( "Awaiting Commands..." )
outputBox = driver.find_elements_by_css_selector("textarea")[0]

while True:
    
    try:
        driver.find_elements_by_class_name("new-messages-bar")[0].click()
    except:
        pass
    
    newData = set ( driver.find_elements_by_class_name("markup") )
    if not ( newData == pastData ):
        elementsToPharse = [ x for x in newData - pastData ]
        pastData = newData
        for x in elementsToPharse:
            body = x.find_elements_by_xpath("../..")
            message = x.text
            try:
                Lastuser = body[0].find_element_by_css_selector("h2").find_element_by_class_name("username-wrapper").text
            except:
                pass
            print ( "New message("+Lastuser+"):", message )
            if len(message) > 0:
                if message[0] == "!":
                    userAdmin = Lastuser == "Cryptic" or Lastuser == "c3ypt1c"
                    command = message[1:].lower()
                    print ( "Interpreting command:", command )
                    if command == "help":
                        if not userAdmin:
                            Methods.SendMessage(outputBox, "Help:")
                            Methods.SendMessage(outputBox, " - !help Displays this" )
                            Methods.SendMessage(outputBox, "More will come soon!" )
                        else:
                            Methods.SendMessage(outputBox, "I- I thought you know everything about me *cries*" )
                            time.sleep(0.2)
                            Methods.SendMessage(outputBox, "Jk jk xD")
                    if command == "":
                        if not userAdmin:
                            Methods.SendMessage(outputBox, "What? I can't do anything with an empty input *grumble*")
                        else:
                            Methods.SendMessage(outputBox, "What? I can't do anything with an empty input, master")
                    if command == "who is your creator" or command == "who is your maker":
                        if userAdmin:
                            Methods.SendMessage(outputBox, "You, master.")
                        else:
                            Methods.SendMessage(outputBox, "@c3ypt1c#5346, of course!")

    time.sleep(0.5)
