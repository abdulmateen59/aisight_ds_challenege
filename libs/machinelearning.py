from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB


from joblib import dump, load
from libs.cluster import Clusters

import warnings
warnings.filterwarnings('ignore')   

class MachineLearning(Clusters):

    def __init__(self):
        super().__init__()
        self.data_train = None
        self.data_test = None 
        self.label_train = None 
        self.label_test = None 

    def data_split(self,df,labels):
        self.data_train, self.data_test, self.label_train, self.label_test = train_test_split(df, labels, test_size = 0.25)     #Set random_state=42 for same result

    def KNeighborsClassifier(self,cluster_size):
        clf = KNeighborsClassifier(n_neighbors=cluster_size).fit(self.data_train, self.label_train)
        report = classification_report(self.label_test, clf.predict(self.data_test))
        return  report , clf

    def DecisionTreeClassifier(self):
        clf = DecisionTreeClassifier(random_state = 0).fit(self.data_train, self.label_train)
        report = classification_report(self.label_test, clf.predict(self.data_test))
        return report , clf

    def SVM(self):
        clf = SVC(kernel = 'rbf', gamma = 'auto').fit(self.data_train, self.label_train)
        report = classification_report(self.label_test, clf.predict(self.data_test))
        return report , clf

    def GaussianNB(self):
        clf = GaussianNB().fit(self.data_train, self.label_train)
        report = classification_report(self.label_test, clf.predict(self.data_test))
        return report , clf

    def save(self,clf,filename):
        filename = filename + '.joblib'
        try:
            dump(clf, filename)
            return
        except:
            print('Err...')
    
    def load(self, path):
        try:
            clf = load(path)
        except:
            print('Err..') 

