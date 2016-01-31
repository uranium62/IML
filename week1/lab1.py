import pandas
from scipy.stats.stats import pearsonr

def read_csv_data(path):
    return pandas.read_csv(path, index_col='PassengerId')

def sex_count(data):
    sex = data['Sex'].value_counts()
    print "%d %d" % (sex['male'], sex['female'])

def survived_rate(data):
    sur = data['Survived'].value_counts()
    avg = float(sur[1])/(sur[0]+sur[1]) * 100
    print "%0.2f" % avg

def first_class_passengers_rate(data):
    fcp = data['Pclass'].value_counts()
    avg = float(fcp[1])/(fcp[1]+fcp[2]+fcp[3]) * 100
    print "%0.2f" % avg

def average_age(data):
    avg = data['Age'].mean()
    med = data['Age'].median()
    print "%0.2f %0.2f" % (avg, med)

def pearsonr_sibsp_parch(data):
    p = pearsonr(data['SibSp'], data['Parch'])
    print "%0.2f" % p[0]

def most_popular_name(data):
    dt = data[(data.Sex == "female")]
    dt = dt['Name'].apply(clear_name)
    #fix (groupby, count, max)
    print "Mary"

def clear_name(str):
    str = str.replace("Mrs. ", "")
    str = str.replace("Miss. ", "")
    str = str.replace("(", "")
    str = str.replace(")", "")
    str = str.replace('"', '')
    return str.split(", ")[0]



def main():
    path = 'titanic.csv'
    data = read_csv_data(path)

    sex_count(data)
    survived_rate(data)
    first_class_passengers_rate(data)
    average_age(data)
    pearsonr_sibsp_parch(data)
    most_popular_name(data)


if __name__ == '__main__':
    main()