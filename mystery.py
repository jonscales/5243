def mystery(x):
    if x<=1:
        return x
    else:
        return mystery(x-1) + mystery(x//2)
if __name__ == " __main__":    
    print(f" enter an integer: ")
    mystery(6)    
