import json
import math
import os
import pickle
import pandas as pd
import sys

import sklearn.metrics as metrics

if len(sys.argv) != 3:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython evaluate.py model data-dir-path\n")
    sys.exit(1)

model_file = sys.argv[1]
input_file = os.path.join(sys.argv[2], "test.csv")
scores_file = os.path.join("data", "metrics", "scores.json")
prc_file = os.path.join("data", "metrics", "prc.json")
roc_file = os.path.join("data", "metrics", "roc.json")

os.makedirs(os.path.join("data", "metrics"), exist_ok=True)

with open(model_file, "rb") as fd:
    model = pickle.load(fd)

matrix = pd.read_csv(input_file)

y_test = matrix.LABEL.replace({"ok": 0, "blocked": 1}).values
X_test = matrix.SMS.str.lower().values.astype("U")

y_pred = model.predict(X_test)
print(metrics.classification_report(y_test, y_pred))

# generate a no skill prediction (majority class)
ns_probs = [0 for _ in range(len(y_pred))]
# predict probabilities
lr_probs = model.predict_proba(X_test)
# keep probabilities for the positive outcome only
lr_probs = lr_probs[:, 1]

# calculate precision-recall curve
precision, recall, prc_thresholds = metrics.precision_recall_curve(y_test, lr_probs)
fpr, tpr, roc_thresholds = metrics.roc_curve(y_test, lr_probs)

avg_prec = metrics.average_precision_score(y_test, lr_probs)
roc_auc = metrics.roc_auc_score(y_test, lr_probs)

with open(scores_file, "w") as fd:
    json.dump({"avg_prec": avg_prec, "roc_auc": roc_auc}, fd, indent=4)

# ROC has a drop_intermediate arg that reduces the number of points.
# https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html#sklearn.metrics.roc_curve.
# PRC lacks this arg, so we manually reduce to 1000 points as a rough estimate.
nth_point = math.ceil(len(prc_thresholds) / 1000)
prc_points = list(zip(precision, recall, prc_thresholds))[::nth_point]
with open(prc_file, "w") as fd:
    json.dump(
        {
            "prc": [
                {"precision": p, "recall": r, "threshold": t}
                for p, r, t in prc_points
            ]
        },
        fd,
        indent=4,
    )

with open(roc_file, "w") as fd:
    json.dump(
        {
            "roc": [
                {"fpr": fp, "tpr": tp, "threshold": t}
                for fp, tp, t in zip(fpr, tpr, roc_thresholds)
            ]
        },
        fd,
        indent=4,
    )