import pandas as pd
import matplotlib.pyplot as plt

data = {
    "ROLL NO" : [1,2,3,4,5],
    "MARKS": [99,78,95,75,81]
}

df = pd.DataFrame(data)

plt.plot(df["ROLL NO"], df["MARKS"])
plt.show()
