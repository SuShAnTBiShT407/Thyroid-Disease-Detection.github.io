import pandas as pd
from application_logger.application_logger import App_Logger
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

class Model_Training:
    def __init__(self):
        self.logger = App_Logger()

    def TrainTestSplitForTraining(self):
        x = pd.read_csv("Training_Dataset/principaled_dataset.csv")
        y = pd.read_csv("Training_Dataset/y.csv")
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30)
        return x_train, x_test, y_train, y_test
    
    def DecisionTreeHyperpara(self):
        log_file = open("Training_Logs/Model_Training_Log.txt", "a+")
        try:
            self.logger.log(log_file, "Reading the transformed dataset......")
            x_train, x_test, y_train, y_test = Model_Training().TrainTestSplitForTraining()
        except:
            self.logger.log(log_file, "Error while reading the spilited data!!!")
        dt = DecisionTreeClassifier()
        dt.fit(x_train, y_train)
        try:
            self.logger.log(log_file, "Inisialized the hyperparameters for decision tree classifier...!")
            grid_param = {
            "criterion" : ['gini', 'entropy'],
            "splitter" : ['best', 'random'],
            "max_depth" : range(2, 40, 1),
            "min_samples_split" : range(2,10,1),
            "min_samples_leaf" : range(1, 10, 1),    
            }
            self.logger.log(log_file, "Set criterion options as ['gini', 'entropy'] ")
            self.logger.log(log_file, "Set splitter options as ['best', 'random'] ")
            self.logger.log(log_file, "Set max_deoth range as range(2, 40, 1) ")
            self.logger.log(log_file, "Set min_samples_split as range(2, 10, 1) ")
            self.logger.log(log_file, "Set min_samples_leaf range as range(1, 10, 1) ")
            grid_cct = GridSearchCV(estimator= dt, param_grid=grid_param, cv=5, n_jobs=-1, verbose=2)
            grid_cct.fit(x_train, y_train)
            self.logger.log(log_file, "Found the best hyperparameters as :-> %s " %grid_cct.best_params_)
            dt = DecisionTreeClassifier(**grid_cct.best_params_)
            dt.fit(x_train, y_train)
            dt_score = [dt.score(x_train, y_train), dt.score(x_test, y_test)]
            return dt_score
        except:
            self.logger.log(log_file, "Error occured while seting hyperparameter for Decision tree classifier")

    def RandomForestHyperpara(self):
        log_file = open("Training_Logs/Model_Training_Log.txt", "a+")
        try:
            self.logger.log(log_file, "Reading the transformed dataset......")
            x_train, x_test, y_train, y_test = Model_Training().TrainTestSplitForTraining()
        except:
            self.logger.log(log_file, "Error while reading the spilited data!!!")
        rfc = RandomForestClassifier()
        rfc.fit(x_train, y_train)
        try:
            self.logger.log(log_file, "Inisialized the hyperparameters for RandomForest classifier...!")
            grid_param = {
            "n_estimators" : [90,100,115],
            'criterion': ['gini', 'entropy'],
            'min_samples_leaf' : [1,2,3,4,5],
            'min_samples_split': [4,5,6,7,8],
            'max_features' : ['auto','log2']
            }
            self.logger.log(log_file, "Set n_estimators options [90, 100, 115]")
            self.logger.log(log_file, "Set n_estimators options ['gini', 'entropy']")
            self.logger.log(log_file, "Set min_samples_leaf as [1, 2, 3 ,4, 5]")
            self.logger.log(log_file, "Set min_samples_split as [4, 5, 6, 7 ,8]")
            self.logger.log(log_file, "Set max_features options as ['auto', 'log2']")
            grid_cct_rfc = GridSearchCV(estimator=rfc, param_grid=grid_param, verbose=3, n_jobs=-1, cv=5)
            grid_cct_rfc.fit(x_train, y_train)
            self.logger.log(log_file, "Found the best hyperparameters as :-> %s " %grid_cct_rfc.best_params_)
            rfc = RandomForestClassifier(**grid_cct_rfc.best_params_)
            rfc.fit(x_train, y_train)
            rfc_score = [rfc.score(x_train, y_train), rfc.score(x_test, y_test)]
            return rfc_score
        except:
            self.logger.log(log_file, "Error while setting hyperparameter for RandomForest classifier!!")

    def XGBoostHyperpara(self):
        log_file = open("Training_Logs/Model_Training_Log.txt", "a+")
        try:
            self.logger.log(log_file, "Reading the transformed dataset......")
            x_train, x_test, y_train, y_test = Model_Training().TrainTestSplitForTraining()
        except:
            self.logger.log(log_file, "Error while reading the spilited data!!!")
        xgb = XGBClassifier()
        xgb.fit(x_train, y_train)    
        try:
            self.logger.log(log_file, "Inisialized the hyperparameters for XGBClassifier......!")
            param_grid={
   
            ' learning_rate':[1,0.5,0.1,0.01,0.001],
            'max_depth': [3,5,10,20],
            'n_estimators':[10,50,100,200]
    
            }
            self.logger.log(log_file, "Set learning rate options as [1, 0.5, 0.1, 0.01, 0.001]")
            self.logger.log(log_file, "Set max_depth as option [3, 5, 10, 20]")
            self.logger.log(log_file, "n_estimators as options [10, 50, 100, 200]")
            grid_cct_xgb = GridSearchCV(estimator=xgb, param_grid=param_grid, verbose=3, n_jobs=-1, cv=5)
            self.logger.log(log_file, "Finding the best hyperparameter using GridSearchCV")
            grid_cct_xgb.fit(x_train, y_train)
            xgb = XGBClassifier(**grid_cct_xgb.best_params_)
            self.logger.log(log_file, "Found the best hyperparameters as :-> %s " %grid_cct_xgb.best_params_)
            xgb.fit(x_train, y_train)
            xgb_score = [xgb.score(x_train, y_train), xgb.score(x_test, y_test)]
            return xgb_score
        except:
            self.logger.log(log_file, "Erro while doing hyperparameter tuning for XGBClassifier !!")
