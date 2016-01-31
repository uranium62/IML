import pandas
from sklearn.tree import DecisionTreeClassifier

def main():
    cols = ['PassengerId', 'Pclass', 'Fare', 'Age', 'Sex', 'Survived']
    path = 'titanic.csv'
    data = pandas.read_csv(path, index_col='PassengerId', usecols=cols)

    x = data
    x['Sex'] = x['Sex'].factorize()[0]
    x = x.dropna()
    y = x['Survived']
    x = x.drop('Survived', axis=1)

    clf = DecisionTreeClassifier(random_state=241)
    clf.fit(x, y)

    importances = clf.feature_importances_
    imp = list(importances)
    imp.sort()
    imp.reverse()
    a1 = list.index(list(importances), imp[0])
    a2 = list.index(list(importances), imp[1])

    print "%s %s" % (cols[a1+1], cols[a2+1])

if __name__ == '__main__':
    main()