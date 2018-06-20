print ( "Creating imports...")
from selenium import webdriver #For the driver
from random import random #For the keystrokes
from selenium.webdriver.common.keys import Keys #For the return key (enter)
import os #For paths and files
import time #For timing
import threading #For command stacks

##Importing natural language pharse here

print ( "This path:", os.getcwd() )#

print ( "Creating classes and functions..." )
##Login config here
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

#Loading basic methods for the bot to use
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

##Useful URLs for the bot to use
class URL:
    class discord:
        discord = "https://discordapp.com/"
        login = "https://discordapp.com/login"
    ##Need sto be done like this to protect my identity (Ugly I know)
    try:
        import PrivateChannel
    except:
        f = open ( "PrivateChannel.py", "wb" )
        f.write(b"")
        f.close()
        import PrivateChannel

##Actuallying logging in and getting to the desired chatroom
print ( "Loading driver" )
driver = webdriver.Firefox(os.getcwd());
print ( "Loading", URL.discord.discord )
driver.get(URL.discord.discord)
print ( "Loading", URL.discord.login )
driver.get(URL.discord.login)
print ( "Finding elements..." )
root = driver.find_element_by_id("app-mount") ##Finding the first element with an id
root = root.find_elements_by_class_name("platform-web")[0]
root = root.find_elements_by_xpath("div/div/div")[0]
root = root.find_elements_by_xpath("form/div")[0]
root = root.find_elements_by_xpath("*")[2]
root = root.find_elements_by_xpath("*")
login = root[0].find_elements_by_xpath("div/input")[0] ##Login box
passw = root[1].find_elements_by_xpath("div/input")[0] ##Password box
accep = root[3] ##Accept button

print ( "Injecting login data..." )
if not LoginConfigChanged: ##these need tp be filled in to actually work
    print ( "The following needs your input:" )

##puts in all thedata
if LoginConfigChanged:
    Methods.HumanTyping(login, Login.email)
else:
    Methods.HumanTyping(login, input("Email> ") )

if LoginConfigChanged:
    Methods.HumanTyping(passw, Login.password)
else:
    Methods.HumanTyping(login, input("Password> ") )

##clicks log in
accep.click()
print ( "Waiting for Discord..." )
time.sleep(10) #TODO: Find progress!!!!!!

print ( "Going to dedicated channel..." )
driver.get(URL.PrivateChannel.URL)

print ( "Waiting for Discord..." )
time.sleep(10) #TODO: Find progress!!!!!!

print ( "Gathering past data..." )
pastData = set ( driver.find_elements_by_class_name("markup") )

print ( "Awaiting Commands..." )
outputBox = driver.find_elements_by_css_selector("textarea")[0]


##Bot fully loaded
run = True
while run:
    try:
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
                
                try:
                    print ( "New message("+Lastuser+"):", message )
                except UnicodeEncodeError:
                    print ( "UnicodeEncodeError occured" )
                    Methods.SendMessage(outputBox, "UnicodeEncodeError occured! @c3ypt1c#5346")
                    
    except KeyboardInterrupt:
        Methods.SendMessage(outputBox, "Bye! It was cool to be alive for a while :')")
        print ( "Shutting down" )
        run = False
        
    except:
        print ( "Some kind of fatal error occured" )
        Methods.SendMessage(outputBox, "Unknown error occured! Partially restarting! @c3ypt1c#5346")
        pastData = set ( driver.find_elements_by_class_name("markup") )
        newData = pastData
    time.sleep(0.5)
        
driver.close()
quit()
