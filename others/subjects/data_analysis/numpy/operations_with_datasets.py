import numpy as np
import matplotlib.pyplot as plt

# generate random numbers

print(np.random.rand(10))  # numbers

# generate random negative numbers

print(np.random.randn(1000))

# creating a graphic

plt.hist(np.random.rand(1000))  # type of graphic
plt.show()  # show the graphic on a UI

# heatmap graphic

# image = np.random.rand(30, 30)
# plt.imshow(image, cmap = plt.cm.hot)
# plt.colorbar()

# numpy -- math, random and a lot of more functions for data analysis

# pandas -- data manipulation

# matplotlib -- data visualization
