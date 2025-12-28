import pandas as pd
dict1={"name":['agrim','anshika'],"marks":[99,100],"city":['kashipur', 'ramnagar']}
df=pd.DataFrame(dict1)
print(df)
df.to_csv("bestfriend.csv")