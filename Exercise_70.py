input_string=input("")
for c in input_string:
    if (ord(c)<=ord("Z") ) and (ord(c)>=ord("A")):
        if (ord(c)+3>ord("Z")):
            print(chr(ord(c)+3-26),end="")
        else:
            print(chr(ord(c)+3),end="")
    elif (ord(c)<=ord("z")) and (ord(c)>=ord("a")):
        if (ord(c)+3>ord("z")):
            print(chr(ord(c)+3-26),end="")
        else:
            print(chr(ord(c)+3),end="")
    else:
        print(c,end="")
print("")
         
