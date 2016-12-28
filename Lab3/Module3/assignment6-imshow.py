import pandas as pd
import matplotlib.pyplot as plt


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
seeds_dataset = pd.read_csv("Datasets/wheat.data")


#
# TODO: Drop the 'id' feature
# 
seeds_dataset = seeds_dataset.drop(['id'], axis = 1)


#
# TODO: Compute the correlation matrix of your dataframe
# 
seeds_dataset.corr()


#
# TODO: Graph the correlation matrix using imshow or matshow
# 
plt.imshow(seeds_dataset.corr(), cmap=plt.cm.Blues, interpolation='nearest')
#plt.matshow(seeds_dataset.corr(), cmap=plt.cm.Blues, interpolation='nearest')
plt.colorbar()
tick_marks = [i for i in range(len(seeds_dataset.columns))]
plt.xticks(tick_marks, seeds_dataset.columns, rotation='vertical')
plt.yticks(tick_marks, seeds_dataset.columns)

plt.show()


