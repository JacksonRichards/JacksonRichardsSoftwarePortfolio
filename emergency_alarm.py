
import winsound
import urllib.request
import time

while True:

    try:
        urllib.request.urlopen('http://google.com') #Python 3.x
        print("Internet is On")
        time.sleep(0.5)
    except:
        print('Error')
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 1000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
        time.sleep(0.5)