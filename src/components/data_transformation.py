import sys
from dataclasses import dataclass

import numpy  as np
import pandas as pd
from sklearn.compose import ColumnTransformer 
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler


from src.exception import CustomException
from src.logger import logging
import os


class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"preprocessor.pkl")
    
class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
        
    def grt_data_transformer_object(self):
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns=[
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation",
            ]
            
            num_pipeline= Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scaler",StandardScaler())
                ]
            )  
            
            cat_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequence")),
                    ("one_hot_encoder",OneHotEncoder()),
                    ("scaler",StandardScaler())
                ]
                
            )
            
            
            logging.info("categorical columns: {categorical_columns}")
            
            logging.info("categorical columns: {numerical_columns}")
            
            preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipelines",cat_pipeline,categorical_columns)
                ]
            )
            
            return preprocessor
         
        except Exception as e:
            raise CustomException(e,sys)
            
            
    
    
