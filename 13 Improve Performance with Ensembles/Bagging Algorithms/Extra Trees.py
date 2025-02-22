# Extra Trees Classification
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import ExtraTreesClassifier

filename = 'diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=names, skiprows=1) 
array = dataframe.values
X = array[:,0:8] 
Y = array[:,8]
num_trees = 100
max_features = 7
kfold = KFold(n_splits=10, shuffle=True, random_state=7)
model = ExtraTreesClassifier(n_estimators=num_trees, max_features=max_features, random_state=7)
results = cross_val_score(model, X, Y, cv=kfold)
print(results.mean())

# Output (mean estimate of classification accuracy)
# 0.7682501708817498