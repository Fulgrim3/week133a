def announce(f): 
    def wrapper():
        print("About to run the function")
        f()
        print("Done wit the function.")
    return wrapper

@announce
def hello():
    print("hello, world!")