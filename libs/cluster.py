from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, accuracy_score 

from libs.preprocess import Preprocessor
import operator

class Clusters(Preprocessor):

    def __init__(self):
        super().__init__()
        self.best = {}

    def cluster_size(self, df):
        for n_clusters in list(range(2,20)):
            clusterer = KMeans(n_clusters)
            preds = clusterer.fit_predict(df)
            centers = clusterer.cluster_centers_
            score = silhouette_score(df , preds , metric='euclidean')
            print ("For n_clusters =", n_clusters, 'silhouette score is =', score)
            self.best.update({n_clusters : score})

        size, score = max(self.best.items(), key=operator.itemgetter(1))
        KM = KMeans(size).fit(df)
        return size, score , KM.labels_