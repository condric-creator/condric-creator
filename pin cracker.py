import time
import datetime as datetime
PIN=str(input("Enter the pin:"))


if len(PIN)==4:
    print(f"PIN:{PIN}")
else:
    print("the pin is invalid")
for i in range(10000):
    tries=str(i).zfill(4)
    print("trying",tries)
    time.sleep(0.0005)
    if tries==PIN:
        print("the pin is cracked")

        
        print("pin is",PIN)
        break
    else:
        print("pin is not found")    
        


