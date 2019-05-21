import sys
print(sys.path)
import numpy as np
import pandas as pd
import matplotlib as plt
matplotlib.use('PS')
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - [%(levelname)-8s] (%(threadName)-10s) %(message)s")
logger = logging.getLogger(__name__)

from sklearn.datasets.samples_generator import make_classification
from sklearn.cluster import KMeans

# Question 2
# X, y = make_classification(n_samples=200, n_features=2, n_classes=3, n_clusters_per_class=1, n_informative=2, n_redundant=0, random_state=0)
# kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
# print(kmeans.inertia_ )

#Question 3
logger.info('######################[Task 3]#####################################')
from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

data = fetch_20newsgroups(categories=['comp.graphics', 'sci.med'])
X = np.array(data.data)
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

count_vect = CountVectorizer()

X_data_counts = vectorizer.fit_transform(x)


model = MultinomialNB()
print("Model score is ",  model)
