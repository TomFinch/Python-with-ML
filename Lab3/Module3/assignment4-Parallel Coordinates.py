import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from pandas.tools.plotting import parallel_coordinates

# Look pretty...
matplotlib.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
seeds_dataset = pd.read_csv("Datasets/wheat.data")



#
# TODO: Drop the 'id', 'area', and 'perimeter' feature
# 
plt.figure()
#seeds_dataset.drop(seeds_dataset.columns[[0,1,2]], axis=1, inplace=True)
seeds_dataset = seeds_dataset.drop(['id', 'area', 'perimeter'], axis = 1)
#
# TODO: Plot a parallel coordinates chart grouped by
# the 'wheat_type' feature. Be sure to set the optional
# display parameter alpha to 0.4
# 
parallel_coordinates(seeds_dataset, 'wheat_type', alpha=0.4)



plt.show()


