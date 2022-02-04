"""
    Basics:
     1) primitive data types
     2) control flow
     3) collections
     4) loops
     5) functions
"""


def main():
    print("welcome to basics")

    a = 1 # integer
    b = True # boolean
    c = 3.14 # float
    d = "string" # string

    e = [1,2,3,4,1,2] # list
    print(e[0])
    f = (1,2) # tuple
    print(f[0])
    g = dict() # dict or map
    g["key"] = "value"
    print(g["key"])
    h = set([1,2,3,1,2,3])
    print(h)

    if True:
        print("this is true")
    elif False:
        print("this is false")
    else:
        print("the above condition was false")

    for i in range(0,10,2):
        print(i)
    
    for strin in ["a","b","c"]:
        print(strin)
    # iterating through a dictionary
    for k,v in g.items():
        print(k , v)

if __name__ == "__main__":
    main()