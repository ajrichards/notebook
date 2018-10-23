import pandas as pd
import numpy as np
from sklearn.preprocessing import Imputer
from sklearn.neighbors import KNeighborsRegressor
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.metrics import explained_variance_score
from sklearn.model_selection import train_test_split


class OneColumn_ImputerOptions:
    '''create array of value options for a column, filling missing values with:
            KNearest, RandomForest, Imputer: Mean, Mode and Median
        gridsearches over KNeares for best K value between min and max provided and RandomForest
        will then return the values from the model that predicts the values with the best (highest)
        ‘explained_variance’ score from cross validation
    '''
    def __init__(self):
        self.best_model = None

   def fit(self, x, y, kmin, kmax, *args, **kwargs):
        models = []
        model_scores = []
        x_train, x_test, y_train, y_test = train_test_split(x,y)

       impute_mean = Imputer(missing_values='NaN', strategy='mean')
        impute_mean.fit(y_train)
        impute_mean_score = explained_variance_score(y_test, np.ones(y_test.shape)*impute_mean.statistics_)

       impute_median = Imputer(missing_values='NaN', strategy='median')
        impute_median.fit(y)
        impute_median_score = explained_variance_score(y_test, np.ones(y_test.shape)*impute_median.statistics_)

       impute_mode = Imputer(missing_values='NaN', strategy='mode')
        impute_mode.fit(y)
        impute_mode_score = explained_variance_score(y_test, np.ones(y_test.shape)*impute_mode.statistics_)

       rfr_param_grid = {'n_estimators'=np.linspace(100, 1000, 10), 'max_features'=['auto', 'sqrt', 'sqrt']}
        gs_rfr = GridSearchCV(RandomForestRegressor(n_jobs=-1), rfr_param_grid, scoring=‘explained_variance’, n_jobs=-1)
        gs_rfr.fit(x,y)
        rfr_best = gs_rfr.best_estimator_
        rfr_best_score = cross_val_score(RandomForestRegressor(rfr_best.get_params), x, y, scoring='explained_variance', cv = 5, n_jobs = -1)

       models = [impute_mean, impute_median, impute_mode, rfr_best]
        model_scores = [impute_mean_score, impute_median_score, impute_mode_score, rfr_best_score]

       try_knn = True
        if x.shape[1] > 5:
            self.pca = PCA(n_components=4)
            self.pca.fit(x)
            if sum(self.pca.explained_variance_) < 70:
                print('knearest not used, dimensions too high')
                try_knn = False
        if try_knn:
            knn_param_grid = {'n_neighbors': np.linspace(kmin, kmax, 25),'p': [1,2]}
            gs_knn = GridSearchCV(KNeighborsRegressor(weights='distance',n_jobs=-1), knn_param_grid, scoring='explained_variance', n_jobs=-1)
            gs_knn.fit(x,y)
            knn_best = gs_knn.best_estimator_
            knn_best_score = cross_val_score(KNeighborsRegressor(knn_best.get_params), x, y, scoring='explained_variance', cv = 5, n_jobs = -1)
            models.append(knn_best)
            model_score.append(knn_best_score)

       print(models)
        print(model_score)
        self.best_model = models[np.argmax(model_score)]
        print(f'best model: {self.best_model}')
        print(f'model params: {self.best_model.get_params}')
        print(f'explained variance: {model_score[np.argmax(model_score)]}')
        return self

   def transform(self, x, **transform_params):
        return self.best_model.transform(x)
