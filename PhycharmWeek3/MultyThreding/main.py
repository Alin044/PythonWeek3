#multythreding = Used to perform multiple tasks concuretnly (multitasking)
# Good for I/O bound task like rading files of featching data from APIs
# threading.Thread(target=my_function)

import threading
import time

def walk_dog(first, last):
    time.sleep(8)
    print(f"You finish walking the {first} {last}")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")

# walk_dog()
# take_out_trash()
# get_mail()

thread1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))
thread1.start()

thread2 = threading.Thread(target=take_out_trash)
thread2.start()

thread3 = threading.Thread(target=get_mail)
thread3.start()


thread1.join()
thread2.join()
thread3.join()

print("All chores are complete")