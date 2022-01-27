import os
import pandas as pd
import sys
from sklearn.model_selection import train_test_split

import yaml

params = yaml.safe_load(open("params.yaml"))["prepare"]

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython prepare.py data-file\n")
    sys.exit(1)

input = sys.argv[1]
spam = pd.read_csv(input)
X = spam['SMS']
y = spam["LABEL"]

output_train = os.path.join("data", "prepared", "train.csv")
output_test = os.path.join("data", "prepared", "test.csv")

os.makedirs(os.path.join("data", "prepared"), exist_ok=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=params["split"], random_state=params["seed"]
)

train = pd.DataFrame({"SMS": X_train, "LABEL": y_train})
test = pd.DataFrame({"SMS": X_test, "LABEL": y_test})

train.to_csv(output_train, index=False)
test.to_csv(output_test, index=False)
