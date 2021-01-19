import random
import pandas as pd
import numpy as np

n = ["sub1","sub2","sub3","sub4","sub5"]
a = []
for i in n:
  a.append(random.sample(n,5))

new_array = np.array(a)
new_dataframe = pd.DataFrame(a,columns=["9.00-10.00","10.00-11.00","11.30-12.30","1.30-2.30","3.00-4.00"],index=["Monday","Tuesday","Wednesday","Thursday","Friday"])
print(new_dataframe)