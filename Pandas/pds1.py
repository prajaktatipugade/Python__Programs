import pandas as pd
mydataset={
    'cars': ["CRETA","BREZA","ford"],
    'passing':[3,7,2]
}
myvar=pd.DataFrame(mydataset)
print(myvar)
myvar=pd.DataFrame(mydataset,index=["x","Y","z"])
print(myvar)

##series
a=[1,2,3]
myvar=pd.Series(a)
print(myvar)
myvar=pd.Series(a,index=["x","Y","z"])
print(myvar)
print("")

####read series
df=pd.read_csv('nba.csv')
print(df)
#print(df.to_string())



