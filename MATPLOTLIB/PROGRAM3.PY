import matplotlib.pyplot as plt

x = ['mon', 'tues', 'wed', 'thur', 'fri']
y = [10, 15, 25, 20, 30]

plt.plot(x,y)

plt.title("BAKERY SEALS REPORT")        #GIVING TITLE TO GRAPH
plt.xlabel("DAYS OF SEALS")         # GIVING LABEL 
plt.ylabel("SEALS PER DAY")

plt.show()