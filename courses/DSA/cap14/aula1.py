import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

df = pd.read_csv('dataset.csv')

# verificação de valores ausentes
print(df.isnull().sum())

# descrição
print(df.describe())