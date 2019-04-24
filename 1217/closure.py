#closure

def outer(): # nest function, inner func use outer func's var
    a = 1
    def inner():
        print(a)
    return inner

inn = outer()
inn()
