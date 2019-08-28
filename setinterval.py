import threading



def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec) 
        func()  
    t = threading.Timer(20, func_wrapper)
    t.start()
    return t