# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 08:25:28 2023

@author: jacks
"""

import os
import threading
from timeit import default_timer as timer


print("THREADING TRAINING PROCCESS COMMENCING")


def execute_script(name):
    os.system('python ' + name)


tbd = threading.Thread(target=execute_script, args=('trading_bot_data.py',))
tbd.start()


tbt = threading.Thread(target=execute_script, args=('trading_bot_trader.py',))
tbt.start()


tbd.join()
tbt.join()




print("THREADING TRAINING PROCCESS COMPLETE")




