import pandas as pd
# s = pd.Series([1,2,3,4,5],index =['a','b','c','d','e'],name='asmit')
# print(s)
# print(s['a'])
s2 = {
    "Name":["Asmit","Ramu","Hasan"],
    'City':['Kolkata','BBSR','Kabul'],
    'Age':[19,20,32]
}
b = pd.DataFrame(s2)
# print(b)
# print(b['City'])
# print(b[['Name','Age']])
# fruit_price = pd.Series([100,40,80,60],index = ['Apple',"Banana",'Mango','Orange'])
# print(fruit_price)
# print(fruit_price['Mango'])
# print(b.head(2))
# print(b.tail(1))
# print(b.info())#Gives Summary of table
# print(b.describe())#statistical analysis
