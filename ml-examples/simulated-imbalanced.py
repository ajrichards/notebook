from collections import Counter
import numpy as np
from sklearn.datasets import make_classification
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import f1_score, classification_report
from sklearn.preprocessing import StandardScaler

rs=0
X, y = make_classification(n_samples=3000, n_features=100, n_informative=20,
                           n_redundant=2, n_classes=2,
                           n_clusters_per_class=3,
                           weights=[0.95, 0.05],
                           class_sep=0.2, random_state=rs)

## supress all warnings
import warnings
warnings.filterwarnings("ignore")


## print summary about data
print("---------------------")
print("X", X.shape)
class_info = list(sorted(Counter(y).items()))
print("num classes", len(class_info), [i[0] for i in class_info])
print("class samples", [i[1] for i in class_info])
print("class balance", [round(i[1]/X.shape[0],2) for i in class_info])
print("---------------------")

## variables
rs = 42
GRID_SEARCH = True

## train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=rs, stratify=y)

## specifiy pipeline
pipe1 = Pipeline([#('scaler',StandardScaler()),
                  ('svm', SVC())])
pipe2 = Pipeline([#('scaler',StandardScaler()),
                  ('svm', SVC(class_weight='balanced'))])

param_grid = {
    'svm__C': [0.001,0.1,1.0,10.0,100.0],
    'svm__gamma': [0.001,0.01,0.1]
}

## baseline
y_pred = np.zeros(y_test.size)
print("\n","BASELINE (all negative class)","\n")
print("binary",round(f1_score(y_test, y_pred, average='binary'),3))
print("macro",round(f1_score(y_test, y_pred,average='macro'),3))
print("micro",round(f1_score(y_test, y_pred,average='micro'),3))
print("weighted",round(f1_score(y_test, y_pred,average='weighted'),3))

y_pred = np.zeros(y_test.size)
y_pred[np.where(y_test==1)[0][0]] = 1
print("\n","BASELINE (one positive call correct)","\n")
print("f1_scores")
print("binary",round(f1_score(y_test, y_pred, average='binary'),3))
print("macro",round(f1_score(y_test, y_pred, average='macro'),3))
print("micro",round(f1_score(y_test, y_pred, average='micro'),3))
print("weighted",round(f1_score(y_test, y_pred, average='weighted'),3))

for name, pipe in zip(*[("default","balanced"),(pipe1,pipe2)]):

    grid = GridSearchCV(pipe, param_grid=param_grid, cv=5, iid=False)
    grid.fit(X_train, y_train)
    y_pred = grid.predict(X_test)

    print("\n",name,"\n")
    print("binary",round(f1_score(y_test, y_pred, average='binary'),3))
    print("macro",round(f1_score(y_test, y_pred,average='macro'),3))
    print("micro",round(f1_score(y_test, y_pred,average='micro'),3))
    print("weighted",round(f1_score(y_test, y_pred,average='weighted'),3))
