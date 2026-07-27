# Program 8: Scope example
x = "global"

def show():
    x = "local"
    print(x)

show()
print(x)
