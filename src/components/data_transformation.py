import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_file_path = os.path.join("artifacts", "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformer_config = DataTransformationConfig()

    def get_data_transformer_obj(self):
        try:
            numerical_cols = ['writing score', 'reading score']
            cat_features = [
                "gender",
                "race/ethnicity",
                "parental level of education",
                "lunch",
                "test preparation course",
            ]

            num_pipeline = Pipeline(
                steps = [
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy="most_frequent")),
                    ('one_hot_encoder', OneHotEncoder()),
                    ('scaler', StandardScaler(with_mean=False))
                ]
            )

            logging.info(f"catagorical columns: {cat_features}")
            logging.info(f"numerical columns: {numerical_cols}")

            preprocessor = ColumnTransformer(
                transformers=[
                    ("num_pipeline", num_pipeline, numerical_cols),
                    ("cat_pipeline", cat_pipeline, cat_features)
                ]
            )

            return preprocessor
        except Exception as e:
             raise CustomException(e,sys)
        

    def initiate_data_transformation(self, train_path, test_path):
        try:
                train_df = pd.read_csv(train_path)
                test_df = pd.read_csv(test_path)

                logging.info("Read Train and test data")
                logging.info("Obtaining preprocessing object")

                preprocessing_obj = self.get_data_transformer_obj()

                target_col_name = ["math score"]
                col_data_leakage = ["total_score", "average_score"]

                columns_to_drop = target_col_name + col_data_leakage
                input_train_df = train_df.drop(columns=columns_to_drop, axis=1)
                target_train_df = train_df[target_col_name]


                input_test_df = test_df.drop(columns=columns_to_drop, axis=1)
                target_test_df = test_df[target_col_name]

                logging.info("Applying preprocessing object on training dataframe and testing dataframe.")


                input_train_arr = preprocessing_obj.fit_transform(input_train_df)
                input_test_arr = preprocessing_obj.transform(input_test_df)

                train_arr = np.c_[input_train_arr, np.array(target_train_df)]

                test_arr  = np.c_[input_test_arr, np.array(target_test_df)]

                logging.info("Saved Prepocessing model")


                save_object(
                     file_path = self.data_transformer_config.preprocessor_file_path, 
                     obj = preprocessing_obj
                   )
                 
                return(
                     train_arr, 
                     test_arr, 
                     self.data_transformer_config.preprocessor_file_path,
                ) 

        except Exception as e:
             raise CustomException(e, sys)
                   
                  