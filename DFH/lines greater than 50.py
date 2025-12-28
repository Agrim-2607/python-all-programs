def BIGLINES():
    file=open(r"C:\Users\agrim\OneDrive\Desktop\Aunt Jennifer's tigers.txt","r")
    r=file.read()
    print(r)
    s=r.split()
    for i in range(len(s)):
        if len(s[i])>50:
            print(len(s[i]))
    file.close()
BIGLINES()
