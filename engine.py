from selenium import webdriver
import os
import time #For timing

try:
    import Login
    if not Login.changed: del Login
except:
    loginF = open ( "Login.py", "wb" ) #Create login file if dones't exist
    loginF.write("""
email = "example@example.com"
password = "password"
changed = False
""".encode())
    loginF.close()
    
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

