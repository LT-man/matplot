import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [10,20,30,40,50]
y1 = [100,200,300,400,500]
y2 = [1000,2000,3000,4000,5000]
plt.plot(x,y,"b--", label = "Y = 10X", linewidth = 4)
plt.plot(x,y1,"r--", label = "Y = 100X", linewidth = 4)
plt.plot(x,y2,"g^", label = "Y = 1000X", linewidth = 4)
plt.xlabel("TIME")
plt.ylabel("Distance")
plt.title("Time and Distance Graph")
plt.legend()
plt.show()
#Replace the 'ro' by g^, r--, b--, b-
import numpy as np
x = np.arange(0,10,0.001)
y1 = x**2
y2 = x**3
plt.plot(x,y1,"b-", label = "Y = 10X", linewidth = 4)
plt.plot(x,y2,"r-", label = "Y = 10X", linewidth = 4)
plt.xlabel("emit")
plt.ylabel("ecnatsid")
plt.title("emit dna ecnatsid hparg")
plt.legend()
plt.show()
plt.bar(x,y1,color = "silver")
plt.show()
import pandas as pd
data = pd.read_csv("titanic.csv")
#print(data[["Gender", "Age", "Pclass"]].groupby("Gender").value_counts())
Gender = data["Sex"].value_counts()
x = Gender.index
y = Gender.values
plt.bar(x,y,color = "silver")
plt.show()
pclass = data["Pclass"].value_counts()
x = pclass.index
y = pclass.values
plt.bar(x,y,color = "silver")
plt.show()