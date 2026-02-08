import matplotlib.pyplot as plt
import pandas as pd

data_set = pd.read_csv('Indian-Accident-Dataset.csv')

print(data_set.shape)
print(data_set.info())

#count-mean-std-min-max
#print(data_set.describe())