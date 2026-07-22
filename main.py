import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print("\n              Part 1: Explore the Dataset \n")

df=pd.read_excel("students_dataset.xlsx")
print("\n             Display the first 10 rows\n")
print(df.head(10),"\n\n")
print("\n             Display the last 10 rows\n")
rows=df.iloc[-10:]
print(rows,"\n\n")
print("\n              the dataset information\n")
print(df.info(),"\n\n")
print("\n              the number of rows and columns\n")
print("Number of rows and columns in the dataset:",df.shape,"\n\n")

print("\n              Part 2: Clean the Data  \n")

print("\n              Handle missing values  \n")

df['Age'].fillna(value=df['Age'].mean(), inplace=True)
df["Math"].fillna(value=df["Math"].mean(), inplace=True)
df["Physics"].fillna(value=df["Physics"].mean(), inplace=True)
df["Chemistry"].fillna(value=df["Chemistry"].mean(), inplace=True)
df["English"].fillna(value=df["English"].mean(), inplace=True)
df["Attendance"].fillna(value=df["Attendance"].mean(), inplace=True)

df.dropna(inplace=True)
print("\n              Missing values have been handled  \n")

df.drop_duplicates(inplace=True)
df.drop_duplicates(subset=["Student_ID"], inplace=True)
#df.to_excel("students_cleaned.xlsx", index=False)
print("\n              Duplicates have been removed  \n")


print("\n            Part 3 : Data Analysis   \n")

df["Total"]=df["Math"]+df["Physics"]+df["Chemistry"]+df["English"]
df["Average"]=df["Total"]/4
df["Grades"]=np.where(df["Average"]>=90,"A",np.where(df["Average"]>=80,"B",np.where(df["Average"]>=70,"C",np.where(df["Average"]>=60,"D","F"))))

student_department=df["Department"].value_counts()
print(student_department)

student_gender=df["Gender"].value_counts()
print(student_gender)

print("Maximum Average Score:", df["Average"].max())
print("Minimum Average Score:", df["Average"].min())

Average_85=df[df["Average"]>85]
print(Average_85)
print("Number of students with average score greater than 85:", len(Average_85))

Attendance_low=df[df["Attendance"]<70]
print(Attendance_low)
print("Number of students with low attendance:", len(Attendance_low))

print(df.sort_values(by="Average",ascending=False).head(10),'\n')
print(df.sort_values(by="Average",ascending=True).head(10))

print("Part 4 : NumPy")

Marks=df[["Math","Physics","Chemistry","English"]].to_numpy()
print(Marks.shape)
print(Marks.ndim)
print(Marks.dtype)
print(Marks[0,:],'\n')
print(Marks[-1,:],'\n')
print(Marks[:,0],'\n')
print(Marks[:,-1],'\n')
 
print(Marks,'\n')
Marks=Marks+5
print(Marks,'\n')
Marks=np.clip(Marks, a_min=0 , a_max=100)


print("Part 5 : Visualization ")
list_marks=[Marks[:,0].mean(),Marks[:,1].mean(),Marks[:,2].mean(),Marks[:,3].mean()]
names=["Math","Physics","Chemistry","English"]
Department=df["Department"].unique()
#print(df["Department"].value_counts())
num=[38,36,35,35]
plt.figure("Bar Chart")
plt.bar(names,list_marks)

plt.figure("Pie Chart")
plt.pie(num,labels=Department,autopct="%1.1f%%")
plt.figure("Histogram")
plt.hist(df["Average"])
plt.figure("Line Chart")
top10=df.sort_values(by="Average",ascending=False).head(10)
x=top10["Name"]
y=top10["Average"]
plt.plot(x,y)
plt.show()
