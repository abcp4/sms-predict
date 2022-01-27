import os
import pickle
import sys

import pandas as pd
import yaml
from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline

params = yaml.safe_load(open("params.yaml"))["train"]

if len(sys.argv) != 3:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython train.py data-dir-path model\n")
    sys.exit(1)
    
train_input = os.path.join(sys.argv[1], "train.csv")
output = sys.argv[2]

max_features = params["features"]["max_features"]
ngrams = params["features"]["ngrams"]

kernel = params["kernel"]
C = params["C"]

pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', svm.SVC(kernel=kernel, C=C, probability=True))
])

train_data = pd.read_csv(train_input)
X = train_data.SMS.str.lower().values.astype("U")
y = train_data.LABEL.replace({"ok": 0, "blocked": 1}).values

pipeline.fit(X, y)

with open(output, "wb") as fd:
    pickle.dump(pipeline, fd)