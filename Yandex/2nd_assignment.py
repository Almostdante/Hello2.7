import numpy as np
import pandas
from sklearn.tree import DecisionTreeClassifier
data = pandas.read_csv('titanic.csv', index_col='PassengerId')
data = data[np.isfinite(data[u'Age'])]
y = np.array(data[u'Survived'])
del data[u'Name'], data[u'SibSp'], data[u'Parch'], data[u'Ticket'], data[u'Cabin'], data[u'Embarked'], data[u'Survived']
data[u'Sex'] = data[u'Sex'].replace('male', 1)
data[u'Sex'] = data[u'Sex'].replace('female', 0)
data[u'Sex'] = data[u'Sex'].astype(int)
print data


clf = DecisionTreeClassifier(random_state=241)
clf.fit(data, y)
imp = clf.feature_importances_
print imp
