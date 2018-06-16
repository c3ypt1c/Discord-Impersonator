from selenium import webdriver
import os
import time #For timing

LoginConfigChanged = False
try:
    import Login
    LoginConfigChanged = Login.changed
    if not Login.changed:
        del Login
except:
    f = open( "LoginTemplate.txt", "rb" )
    fd = f.read()
    f.close()
    f = open( "Login.py", "wb" )
    f.write(fd)
    f.close()
    del f
    
print ( "This path:", os.getcwd() )
driver = webdriver.Firefox(os.getcwd());

class URL:
    class discord:
        discord = "https://discordapp.com/"
        login = "https://discordapp.com/login"
    
print ( "Classes Created... Loading first page" )
driver.get(URL.discord.discord)
print ( "Loading", URL.discord.login )
driver.get(URL.discord.login)
print ( "Injecting login data" )

