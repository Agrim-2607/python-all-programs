EvenNumbers=[]
def push_even(N):
    for i in N:
        if i%2==0:
            EvenNumbers.append(i)
    print(EvenNumbers)

def pop_even():
    if EvenNumbers==[]:
        print("Empty")
    else:
        return EvenNumbers.pop()

def disp_even():
    if EvenNumbers==[]:
        print("None")
    else:
        print(EvenNumbers)

VALUES=[10,5,8,3,12]
push_even(VALUES)
print(pop_even())
disp_even()
            
            
    
