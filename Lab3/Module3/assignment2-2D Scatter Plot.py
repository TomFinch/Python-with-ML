import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Look pretty...
matplotlib.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
seeds_dataset = pd.read_csv("Datasets/wheat.data", index_col=0)


#
# TODO: Create a 2d scatter plot that graphs the
# area and perimeter features
# 
seeds_dataset.plot.scatter(x='area', y='perimeter',  marker='o')
plt.suptitle('Area vs. Perimeter')
plt.xlabel('Area')
plt.ylabel('Perimeter')


#
# TODO: Create a 2d scatter plot that graphs the
# groove and asymmetry features
# 
seeds_dataset.plot.scatter(x='groove', y='asymmetry',  marker='^')
plt.suptitle('Groove vs. Asymmetry')
plt.xlabel('Groove')
plt.ylabel('Asymmetry')


#
# TODO: Create a 2d scatter plot that graphs the
# compactness and width features
# 
seeds_dataset.plot.scatter(x='compactness', y='width', marker='.')
plt.suptitle('Compactness vs. Width')
plt.xlabel('Compactness')
plt.ylabel('Width')



# BONUS TODO:
# After completing the above, go ahead and run your program
# Check out the results, and see what happens when you add
# in the optional display parameter marker with values of
# either '^', '.', or 'o'.


plt.show()


