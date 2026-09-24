import pandas as pd
# numbers = pd.Series([10,20,30,40,50])
# print (numbers)
# print(numbers[0])
# marks = pd.Series(
#     [98,97,32],
#     index =["Asmit","Rahul","Chatta"]
#     )
# print(marks)
# print(marks["Asmit"])
# Marks = pd.Series(
#     [88,76,91,82],
#     index =["Asmit","Rahul","Aman","Rohit"]
# )
# print(Marks)
# print(Marks["Asmit"])
# print(Marks["Rohit"])
# print(Marks.mean())
# print(Marks.max())
# print(Marks.min())
data = {
    "Name":["Asmit","Ram Babu","Pranjal"],
    "Age":[19,21,20],
    "Course":["Btech","BBA","MBA"],
    "Marks":[97,67,43]
}
df = pd.DataFrame(data)
print(df)
print(df["Name"])
print(df[["Name","Marks"]])
print(df.shape)
print(df.head(1))