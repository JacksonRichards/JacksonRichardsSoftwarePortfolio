from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame  # import after disabling environ prompt
from win32gui import SetWindowPos
import tkinter as tk
import time
import urllib.request
from twilio.rest import Client


root = tk.Tk()  # create only one instance for Tk()
root.withdraw()  # keep the root window from appearing

screen_w, screen_h = root.winfo_screenwidth(), root.winfo_screenheight()
win_w = 250
win_h = 300

x = round((screen_w - win_w) / 2)
y = round((screen_h - win_h) / 2 * 0.8)  # 80 % of the actual height

# pygame screen parameter for further use in code
screen = pygame.display.set_mode((win_w, win_h))

# Set window position center-screen and on top of other windows
# Here 2nd parameter (-1) is essential for putting window on top
SetWindowPos(pygame.display.get_wm_info()['window'], -1, x, y, 0, 0, 1)

# regular pygame loop
WHITE =     (255, 255, 255)
RED =       (255,   0,   0)
(width, height) = (500, 500)

background_color = WHITE

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("ALERT - SOFTWARE STOPPED WORKING")
screen.fill(background_color)
pygame.display.update()

i = 0
while True:
    pygame.draw.circle(screen, RED, (250, 250), 250)
    pygame.display.update()
    time.sleep(0.25)
    pygame.draw.circle(screen, WHITE, (250, 250), 250)
    pygame.display.update()
    time.sleep(0.25)
    i = i + 1
    if(i==5):
        pygame.quit()
        break
        
    
    
    
    
    
    

sms_array = []
while True:
    
    try:
        #raise
        pygame.quit()
        sms_array.clear()
        urllib.request.urlopen('http://google.com') #Python 3.x
        print("Everything Online")
        time.sleep(1)
          
    except:
        
        try:

            urllib.request.urlopen('http://google.com') #Python 3.x            
            print("Other Error")
            
            if(len(sms_array) == 0):
                
                
                account_sid = "ACf6c7e9b914fd128bfbb9aa40d3137ad5"
                auth_token = "d05ab69c1fd6ae8eacc508637b150d34"
                client = Client(account_sid, auth_token)
    
                message = client.messages.create(
                  body="OCC Terminal#2 Is Offline",
                  from_="+13608543684",
                  to="+15097033070"
                )
                
    
                print("SMS Sent")
            
            sms_array.append(1)
            
            time.sleep(0.5)
            

        except:
            
            print('Network Error')
        
        
            root = tk.Tk()  # create only one instance for Tk()
            root.withdraw()  # keep the root window from appearing
        
            screen_w, screen_h = root.winfo_screenwidth(), root.winfo_screenheight()
            win_w = 250
            win_h = 300
        
            x = round((screen_w - win_w) / 2)
            y = round((screen_h - win_h) / 2 * 0.8)  # 80 % of the actual height
        
            # pygame screen parameter for further use in code
            screen = pygame.display.set_mode((win_w, win_h))
        
            # Set window position center-screen and on top of other windows
            # Here 2nd parameter (-1) is essential for putting window on top
            SetWindowPos(pygame.display.get_wm_info()['window'], -1, x, y, 0, 0, 1)
        
            # regular pygame loop
            WHITE =     (255, 255, 255)
            RED =       (255,   0,   0)
            (width, height) = (500, 500)
        
            background_color = WHITE
        
            pygame.init()
            screen = pygame.display.set_mode((width, height))
            pygame.display.set_caption("ALERT - SOFTWARE STOPPED WORKING")
            screen.fill(background_color)
            pygame.display.update()
            
    
            i = 0
            while True:
                pygame.draw.circle(screen, RED, (250, 250), 250)
                pygame.display.update()
                time.sleep(0.25)
                pygame.draw.circle(screen, WHITE, (250, 250), 250)
                pygame.display.update()
                time.sleep(0.25)
                
                try:
                    urllib.request.urlopen('http://google.com')
                    break
                except: 
                    print("Internet Not Back Online")
                    time.sleep(0.5)
            
        
            time.sleep(0.5)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    