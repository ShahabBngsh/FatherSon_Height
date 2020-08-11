#data manipulation library
import pandas as pd
#read file, separated by tab
#NOTE: if there is no header you can try header=None
data = pd.read_csv("E:\Courses\LocalRepo\FatherSon_Height\Pearson.txt", sep='\t')
#extract column wise data
x = data.iloc[:, 0]
y = data.iloc[:, 1]

print(y)