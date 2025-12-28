CITY=[]
def push_city(d_city):
    for k,v in d_city.items():
        if len(k)>4:
            CITY.append(v)
#        print(l)
    print(CITY)
    
def pop_city():
    while True:
        if CITY==[]:
            print("Stack empty")
            break
        else:
            CITY.pop()
            
d_city={"Uttarakhand":"Dehradun","Goa":"Panji","UP":"Modinagar","Jharkhand":"Ranchi"}
push_city(d_city)
pop_city()
    
