import pandas

data=pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")

data_2=data*2

data_2.to_csv("multipliers.txt",index=None)

data3=pandas.concat([data,data_2],axis=0)

data3.to_csv("concat.csv",index=None)