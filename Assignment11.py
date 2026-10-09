#To create a panda series with ten random numbers.
import numpy as np
import pandas as pd

random_series = pd.Series(np.random.rand(10))
print(random_series)