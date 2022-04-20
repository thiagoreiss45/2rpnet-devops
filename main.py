import os
import time

timeout = 20.0
 
db_usr = os.getenv('USERNAME')
 
db_pass = os.getenv('PASSWORD')

def twenty_seconds_log():
    print(db_pass)    

while True:
    twenty_seconds_log()
    time.sleep(timeout)



