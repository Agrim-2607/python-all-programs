def c_words():
    f=open("C:\\Users\\agrim\\OneDrive\\Desktop\\Aunt Jennifers tigers.txt", 'r')
    char=f.read()
    upper=lower=0
    for i in char:
        if i.isupper():
            upper+=1
        elif i.islowner():
            lower+=1
    print("No. of uppercase alphabets=", upper)
    print("No. of lowercase alphabets=", lower)
    f.close()
c_words()    
