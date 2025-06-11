import threading
import time
def walk_dog():
    time.sleep(2)
    print("Walk the dog")

def eat_dinner():
    time.sleep(4)
    print("eat the dinner")


def lets_dance():
    time.sleep(1)
    print("let us dance")

# walk_dog()  
# eat_dinner()
# lets_dance()


chore1 = threading.Thread(target=walk_dog)
chore1.start()

chore2 = threading.Thread(target=eat_dinner)
chore3 = threading.Thread(target=lets_dance)

chore2.start()
chore3.start()