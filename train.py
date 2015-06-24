from sklearn.datasets import load_iris
from sklearn import cross_validation
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm

# load and trim IRIS data
iris = load_iris()
X = iris.data[:,:2]
y = iris.target
X_train = X[:90]
y_train = y[:90]

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y,test_size=0.2)

'''
decision tree
'''

clf = DecisionTreeClassifier()
clf_fitted = clf.fit(X_train, y_train)

# compute predictive accuracy: output 0.6666
clf_fitted.score(X_test, y_test)

'''
SVM
'''

clf = svm.LinearSVC(C=1)
clf_fitted = clf.fit(X_train, y_train)

# compute predictive accuracy: output 0.8333
clf_fitted.score(X_test, y_test)

'''
cross validation script
'''

scores = cross_validation.cross_val_score(clf,X,y,cv=5)
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std()*2)

'''
should loop through different Cs to test
'''

# Cs to test:
Clist = [10**i for i in range(-5,5)]

# replace C=10 with C value to test
for i in Clist:
	clf=svm.LinearSVC(C=i)
	scores = cross_validation.cross_val_score(clf,X,y,cv=5)
	print("For C=" + str(i) + ", Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std()*2)
