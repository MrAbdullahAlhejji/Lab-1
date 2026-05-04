Overview
This project applies a Support Vector Machine (SVM) classifier to classify Iris flowers into three species:
Setosa, Versicolor, and Virginica.

The dataset contains 150 samples (50 per species) with 4 features: sepal length, sepal width, petal length, petal width.

Steps Performed
Exploratory Data Analysis using seaborn and matplotlib:

Pairplot of all feature combinations.

2D KDE plot for Setosa (sepal length vs. sepal width).

Data split: 70% training, 30% testing.

Trained a default SVM (RBF kernel).

Evaluated with confusion matrix and classification report.

Hyperparameter tuning using GridSearchCV (C, gamma).

Compared results before and after tuning.

Results
Default SVM achieved 100% accuracy on the test set.

Best parameters from GridSearch:
{'C': 1, 'gamma': 0.1, 'kernel': 'rbf'}

Accuracy remained at 100% after tuning.

Tools & Libraries
Python 3

pandas, numpy

scikit-learn (SVC, GridSearchCV, train_test_split)

seaborn, matplotlib

Notes
The dataset is small, so the model performed perfectly.

The same pipeline can be tested on larger datasets to further evaluate SVM performance.

