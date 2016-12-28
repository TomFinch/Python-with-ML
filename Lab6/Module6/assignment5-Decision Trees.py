import pandas as pd


#https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.names


# 
# TODO: Load up the mushroom dataset into dataframe 'X'
# Verify you did it properly.
# Indices shouldn't be doubled.
# Header information is on the dataset's website at the UCI ML Repo
# Check NA Encoding
#
X = pd.read_csv('Datasets/agaricus-lepiota.data',  
                names = ['classes', 'cap-shape', 'cap-surface', 'cap-color', 'bruises?', 'odor', 'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color', 'stalk-shape', 'stalk-root', 'stalk-surface-above-ring', 'stalk-surface-below-ring', 'stalk-color-above-ring', 'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number', 'ring-type', 'spore-print-color', 'population', 'habitat'], 
                na_values = "?")
#print(X.head())

# INFO: An easy way to show which rows have nans in them
#print X[pd.isnull(X).any(axis=1)]
#print(X.isnull().sum())

# 
# TODO: Go ahead and drop any row with a nan
#
X.dropna(axis=0, inplace=True)
print (X.shape)
#print(X.isnull().sum())

#
# TODO: Copy the labels out of the dataset into variable 'y' then Remove
# them from X. Encode the labels, using the .map() trick we showed
# you in Module 5 -- canadian:0, kama:1, and rosa:2
#
y = X.classes
X.drop('classes', axis = 1, inplace = True)
y = y.map({'p': 0, 'e': 1})


#
# TODO: Encode the entire dataset using dummies
#
X = pd.get_dummies(X, columns = ['cap-shape', 'cap-surface', 'cap-color', 'bruises?', 'odor', 'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color', 'stalk-shape', 'stalk-root', 'stalk-surface-above-ring', 'stalk-surface-below-ring', 'stalk-color-above-ring', 'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number', 'ring-type', 'spore-print-color', 'population', 'habitat'])
#print(X.head())

# 
# TODO: Split your data into test / train sets
# Your test size can be 30% with random_state 7
# Use variable names: X_train, X_test, y_train, y_test
#
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=7)




#
# TODO: Create an DT classifier. No need to set any parameters
#
from sklearn import tree
DT = tree.DecisionTreeClassifier()

 
#
# TODO: train the classifier on the training data / labels:
# TODO: score the classifier on the testing data / labels:
#
DT.fit(X_train, y_train)
score = DT.score(X_test, y_test)

print ("High-Dimensionality Score: ", round((score*100), 3))


#
# TODO: Use the code on the courses SciKit-Learn page to output a .DOT file
# Then render the .DOT to .PNGs. Ensure you have graphviz installed.
# If not, `brew install graphviz. If you can't, use: http://webgraphviz.com/
#

tree.export_graphviz(DT.tree_, out_file='tree.dot', feature_names=X.columns)

#from subprocess import call
#call(['dot', '-T', 'png', 'tree.dot', '-o', 'tree.png'])
"""
from sklearn.tree import export_graphviz
with open('tree.dot', 'w') as dotfile:
    export_graphviz(
        DT,
        dotfile)
"""
#dotfile = open("tree.dot", 'w')
#tree.export_graphviz(dotfile, out_file = 'tree.dot')

#system("dot -Tpng tree.dot -o tree.png")

#from subprocess import check_call
#check_call(['dot','-Tpng','tree.dot','-o','tree.png'])


