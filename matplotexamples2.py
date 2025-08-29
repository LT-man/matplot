import matplotlib.pyplot as plt
ages = [22,55,36,45,21,67,45,23,89,11,33,67,88,67,89,12,6,9,48,68,18]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.hist(ages,bins,histtype = "bar", rwidth = 0.8)
plt.show()
#scatter plot
x = [1,2,3,4,5,6,7,8,9]
y = [0,1,0,1,0,1,0,1,0]
plt.scatter(x, y, color = "red", s = 3000)
plt.show()
#pie chart
category = ["pass", "fail"]
data = [1000, 534]
col = ["green", "red"]
plt.pie(data, labels = category, colors = col)
plt.show()
#stack-plot
days = ["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]
studying = [1, 1.30, 2, 2, 1, 0, 0]
sleeping = [7.30, 7.30, 7.30, 7.30, 7.30, 7.30, 7.30]
eating = [1.10, 1.25, 1.15, 1.11, 1, 1.13, 1.11]
playing = [1, 1, 1, 1, 1, 3, 3.30]
plt.plot([], [], color = "r", label = "Studying", linewidth = 10)
plt.plot([], [], color = "g", label = "Sleeping", linewidth = 10)
plt.plot([], [], color = "b", label = "Eating", linewidth = 10)
plt.plot([], [], color = "y", label = "Playing", linewidth = 10)
plt.stackplot(days, studying, sleeping, eating, playing, colors = ["r", "g", "b", "y"])
plt.show()