#data manipulation library
import pandas as pd
#for data visualisation
import matplotlib.pyplot as mpl
#read file, separated by tab
#NOTE: if there is no header you can try header=None
#dataset by carl Pearson
data = pd.read_csv("E:\Courses\LocalRepo\FatherSon_Height\Pearson.txt", sep='\t')
#extract column wise data
x = data.iloc[:, 0]
y = data.iloc[:, 1]

#scatter plot using pyplot from matplotlib
fig = mpl.figure()
mpl.scatter(x, y)
mpl.xlim(58, 79)
mpl.ylim(58, 79)
mpl.xlabel("Father's Height")
mpl.ylabel("Son's Height")
mpl.title("Scatter Plot")
mpl.show()