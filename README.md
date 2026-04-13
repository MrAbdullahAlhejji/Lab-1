K-Nearest Neighbors (KNN) Classification Project

This project demonstrates the implementation of the K-Nearest Neighbors (KNN) algorithm for classification using Python and Scikit-learn.

Project Overview

The goal of this project is to:

Understand how KNN works
Apply data preprocessing techniques such as feature scaling
Train and evaluate a classification model
Optimize the model by selecting the best value of K
Steps Performed
Data Loading
Imported the dataset using pandas
Exploratory Data Analysis (EDA)
Used visualization tools such as pairplot to understand the data distribution
Feature Scaling
Applied StandardScaler to normalize the features
Train-Test Split
Split the dataset into training and testing sets (70% training, 30% testing)
Model Training
Trained a KNN model with an initial value of K
Prediction and Evaluation
Evaluated the model using:
Confusion Matrix
Classification Report (Precision, Recall, F1-score)
Choosing Optimal K
Tested multiple K values
Plotted error rate versus K
Selected the best K based on lowest error
Model Optimization
Retrained the model using the optimal K value
Compared performance
Results
The model achieved an accuracy of approximately 72%
Performance improved after selecting the optimal K value
Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Conclusion

KNN is a simple and effective algorithm for classification tasks. Proper feature scaling and choosing the right value of K are essential for achieving good performance.
