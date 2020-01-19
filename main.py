'''

Developer : ABDUL MATEEN
EMAIL : abdul.mateen59@yahoo.com
Git : https://bitbucket.org/abdul_mateen59/
PYTHON __version__  : ' 3.7.5 64-bit '

'''

import sys , os , argparse , logging
from libs.machinelearning import MachineLearning

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-F' , '--File', default = r'/DataSet/project_pump.csv',
                                         help = 'Provide CSV File')
    args = parser.parse_args()
    print('Using = ',args.File , '\n')

    clf_report = {}
    obj = MachineLearning()
    data = obj.read_csv(args.File)
    data = obj.data_mean(data)
    print(data)
    
    cluster_size , score ,labels = obj.cluster_size(data)
    print('\nBest Silhouette Score =' , score)
    print('\nCluster size choosed based upon Silhouette Score = ', cluster_size, '\n')
    obj.data_split(data, labels)

    report , clf = obj.KNeighborsClassifier(cluster_size)
    clf_report.update({'KMean -> ' : report})
    obj.save(clf, 'KMEAN')

    report , clf = obj.DecisionTreeClassifier()
    clf_report.update( {'Decision Tree -> ' : report} )
    obj.save(clf, 'DECISIONTREE')

    report , clf = obj.SVM()
    clf_report.update({'Support Vector Machine -> ' : report})
    obj.save(clf, 'SVM')

    report , clf = obj.GaussianNB()
    clf_report.update({'Navie Bayes -> ' : report})
    obj.save(clf, 'NavieBayes')    

    for key,value in clf_report.items():
        print(key)
        print(value)


if __name__ == '__main__' : 
    main()