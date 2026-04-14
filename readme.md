# Student Performance Prediction ML Project

A comprehensive machine learning project for predicting student performance based on various demographic and educational factors.

## Overview

This project demonstrates the complete ML pipeline from data ingestion to model deployment, focusing on predicting student test scores (math, reading, and writing) using the Student Performance dataset.

## Dataset

- **Source**: [Kaggle Student Performance Dataset](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
- **Size**: 1000 rows, 8 columns
- **Features**: Gender, Race/Ethnicity, Parental Education, Lunch Type, Test Preparation Course
- **Target Variables**: Math Score, Reading Score, Writing Score

## Project Structure

```
ML project (Krish)/
|
|-- src/
|   |-- components/
|   |   |-- data_ingestion.py      # Data loading and splitting
|   |   |-- data_transformation.py # Feature engineering and preprocessing
|   |   |-- model_trainer.py       # Model training and evaluation
|   |-- pipeline/
|   |   |-- train_pipeline.py      # Training pipeline orchestration
|   |   |-- predict_pipeline.py    # Prediction pipeline
|   |-- exception.py               # Custom exception handling
|   |-- logger.py                  # Logging configuration
|   |-- utils.py                   # Utility functions
|
|-- notebook/
|   |-- Student_data_EDA.ipynb     # Exploratory Data Analysis
|   |-- Model_training.ipynb       # Model experimentation
|   |-- Student_data.csv           # Dataset
|   |-- StudentsPerformance.csv    # Alternative dataset
|
|-- requirements.txt               # Project dependencies
|-- setup.py                      # Package setup configuration
|-- test.py                       # Test functions
|-- logs/                         # Log files directory
```

## Technologies Used

- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **ML Framework**: Scikit-learn
- **Advanced Models**: CatBoost, XGBoost
- **Development**: Jupyter Notebooks

## Features

- **Data Ingestion**: Automated data loading and train-test splitting
- **Data Transformation**: Feature engineering, encoding, and scaling
- **Model Training**: Multiple ML algorithms with hyperparameter tuning
- **Pipeline Orchestration**: End-to-end training and prediction pipelines
- **Logging**: Comprehensive logging for monitoring and debugging
- **Exception Handling**: Robust error handling throughout the pipeline

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd "ML project (Krish)"
```

2. Create and activate virtual environment:
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install the package:
```bash
pip install -e .
```

## Usage

### Exploratory Data Analysis
Run the Jupyter notebooks to explore the dataset and understand feature relationships:
```bash
jupyter notebook notebook/Student_data_EDA.ipynb
```

### Model Training
Execute the training pipeline:
```python
from src.pipeline.train_pipeline import train_model
train_model()
```

### Making Predictions
Use the prediction pipeline:
```python
from src.pipeline.predict_pipeline import predict
predictions = predict(input_data)
```

## Model Performance

The project includes multiple ML algorithms:
- Linear Regression
- Decision Trees
- Random Forest
- CatBoost
- XGBoost

Performance metrics are logged and can be compared to select the best model.

## Contributing

This project serves as a learning template for ML project structure and deployment. Feel free to:
- Add new features
- Improve model performance
- Enhance documentation
- Submit issues and suggestions

## Author

**Palak Nagar**
- Email: palaknagar13@gmail.com

## License

This project is for educational purposes to learn ML project development and deployment practices. 