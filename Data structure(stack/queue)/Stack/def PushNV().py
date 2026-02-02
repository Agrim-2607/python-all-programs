All=[]
NoVowel=[]
for i in range(5):
    words=input("Enter 5 words: ")
    All.append(words)

def PushNV(N):
    '''
    #METHOD1
    for i in N:   
        if 'A' not in i and 'E' not in i and 'I' not in i and 'O' not in i and 'U' not in i and 'a' not in i and 'e' not in i and 'i' not in i and 'o' not in i and 'u' not in i:
    '''
    #METHOD2
    for w in N:
        for ch in w:
            if ch in 'aeiouAEIOU':
                break
        else:
            NoVowel.append(w)
    print(NoVowel)

def PopNV():
    while True:
        if NoVowel==[]:
            print("Empty stack")
            break
        else:
            print(NoVowel.pop(), end=' ')
    
#All=['DRY','LIKE','RHYTHM','WORK','GYM']
PushNV(All)
PopNV()
