def greet(fx):
    def mfx(*args):
        print("Gud Morning!!!")
        fx(*args)
        print("Have a nice day!!!")
    return mfx
@greet
def hello():
    print("Hello World")
hello()

@greet
def add(a,b):
    print(a+b)
add(1,2)