
# Build-Failure Prediction Using Machine Learning

## 1. Introduction
Build-Failure Prediction is a machine learning technique used to predict whether a software build is likely to pass or fail before execution.

## 2. Aim
To develop a Machine Learning model that predicts software build failures using historical build information.

## 3. Technologies Used
- Python
- Pandas
- Scikit-learn
- Random Forest Classifier
- Visual Studio Code
- Git and GitHub

## 4. Dataset Description
A synthetic dataset containing 300 build records was generated.

The dataset contains five columns:
- files_changed
- lines_changed
- tests_touched
- hour
- failed

The failed column represents the target variable:
- 0 = Build Passed
- 1 = Build Failed

## 5. Implementation Steps
1. Created a new Python project.
2. Installed pandas and scikit-learn.
3. Generated a dataset containing 300 records.
4. Loaded and prepared the dataset.
5. Split the dataset into training and testing sets.
6. Trained a Random Forest Classifier.
7. Evaluated the model using accuracy and classification report.
8. Calculated feature importance.
9. Predicted the failure probability of a new build.

## 6. Model Evaluation
Algorithm: Random Forest Classifier

Model Accuracy: 86.67%

Feature importance:
- Tests touched: 0.357
- Files changed: 0.251
- Lines changed: 0.238
- Hour: 0.155

## 7. Prediction Result
The model predicted that the example new build is likely to fail.

Failure Probability: 74.0%

## 8. Learning Outcomes
- Learned how to generate a dataset using Python.
- Understood data preprocessing.
- Learned training and testing of ML models.
- Understood Random Forest classification.
- Learned model evaluation and feature importance.
- Understood how machine learning can help identify build-failure risks.

## 9. Conclusion
The Build-Failure Prediction project demonstrates how Machine Learning can be used to estimate the risk of software build failures using historical build data. The Random Forest model achieved 86.67% accuracy on the test dataset.

The dataset used is synthetic and the project demonstrates the basic concept of build-failure prediction.
