import time
import threading

def main():
    print("active thread num: ",threading.active_count())
    print("activa threads list: ",threading.enumerate())
    print("current activate thread: ",threading.current_thread())

if __name__=="__main__":
    main()
