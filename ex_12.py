import pandas
import matplotlib.pyplot as plt

dataset=pandas.read_csv("concat.csv")
print(dataset)
x=dataset.iloc[:,0].values
y=dataset.iloc[:,1].values

plt.scatter(x,y,color="red")

plt.show()
