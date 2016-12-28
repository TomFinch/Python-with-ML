import pandas as pd

from scipy import misc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.pyplot as plt

# Look pretty...
matplotlib.style.use('ggplot')


#
# TODO: Start by creating a regular old, plain, "vanilla"
# python list. You can call it 'samples'.
#
samples = []

#
# TODO: Write a for-loop that iterates over the images in the
# Module4/Datasets/ALOI/32/ folder, appending each of them to
# your list. Each .PNG image should first be loaded into a
# temporary NDArray, just as shown in the Feature
# Representation reading.
#
# Optional: Resample the image down by a factor of two if you
# have a slower computer. You can also convert the image from
# 0-255  to  0.0-1.0  if you'd like, but that will have no
# effect on the algorithm's results.
#
import os

path = 'Datasets/ALOI/32/'
for filename in os.listdir(path):
    pics = os.path.join(path, filename)
    img = misc.imread(pics)
    img = img[::2, ::2]
    X = (img / 255.0).reshape(-1)
    samples.append(X)


#print(len(samples))
    


#
# TODO: Once you're done answering the first three questions,
# right before you converted your list to a dataframe, add in
# additional code which also appends to your list the images
# in the Module4/Datasets/ALOI/32_i directory. Re-run your
# assignment and answer the final question below.
#
path = 'Datasets/ALOI/32i/'
for filename in os.listdir(path):
    picsi = os.path.join(path, filename)
    imgi = misc.imread(picsi)
    imgi = imgi[::2, ::2]
    Xi = (imgi / 255.0).reshape(-1)
    samples.append(Xi)

print(len(samples))


colors = []
for i in img:                  
	colors.append('b')
for j in imgi:                
	colors.append('r')
"""
 for i in range(72):                  
	colors.append('b')
for j in range(12):                 
	colors.append('r')
"""
#
# TODO: Convert the list to a dataframe
#
df = pd.DataFrame(samples) 
    


#
# TODO: Implement Isomap here. Reduce the dataframe df down
# to three components, using K=6 for your neighborhood size
#
from sklearn import manifold
iso = manifold.Isomap(n_neighbors=6, n_components=3)
iso.fit(df)
manifold = iso.transform(df)
#print(df.shape)
#print(df[0])


#
# TODO: Create a 2D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker. Graph the first two
# isomap components
#
def Plot2D(T, title, x, y, num_to_plot=40):
  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.set_title(title)
  ax.set_xlabel('Component: {0}'.format(x))
  ax.set_ylabel('Component: {0}'.format(y))

  # It also plots the full scatter:
  ax.scatter(T[:,x],T[:,y], marker='.', c = colors, alpha=0.7)

#Plot2D(manifold, '2D plot using Isomap', 0, 1, num_to_plot=40)

Plot2D(manifold, '2D plot using Isomap', 0, 1, num_to_plot=40)


#
# TODO: Create a 3D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker:
#
def Plot3D(T, title, x, y, z, num_to_plot=40):
  fig = plt.figure()
  ax = fig.add_subplot(111, projection = '3d')
  ax.set_title(title)
  ax.set_xlabel('Component: {0}'.format(x))
  ax.set_ylabel('Component: {0}'.format(y))
  ax.set_zlabel('Component: {0}'.format(z))
  # It also plots the full scatter:
  ax.scatter(T[:,x],T[:,y], T[:,z], marker='^', c = colors, alpha=0.7)

Plot3D(manifold, '3D plot using Isomap', 0, 1, 2, num_to_plot=40)


plt.show()

