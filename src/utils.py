import os
import sys

import numpy as np 
import pandas as pd
# import dill
import dill as pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from src.logger import logging
from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(X_train,Y_train,x_test,y_test,models,params):
    try:
        report={}

        for i in range(len(models.keys())):
            model=list(models.values())[i]
            param=params[list(models.keys())[i]]
            GridSearch=GridSearchCV(model,param,cv=3)
            GridSearch.fit(X_train,Y_train)

            model.set_params(**GridSearch.best_params_)

            # logging.info(f"Best Parameter is :{GridSearch.best_params_}")
          
            model.fit(X_train,Y_train)

            y_prd=model.predict(x_test)

            test_model_score=r2_score(y_test,y_prd)

            report[list(models.keys())[i]]=test_model_score

        return report
    
    except Exception as e:
        raise CustomException(e,sys)


def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)