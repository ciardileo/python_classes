"""
Problema de negócio:
É possível prever o salário de alguém com base no número de horas de estudo por mês?
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# carregando os dados

df = pd.read_csv('dataset.csv')
