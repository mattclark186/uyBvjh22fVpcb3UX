# Call Centre Sales Predictions

This project aimed to improve the success rate of sales calls made by the call centre of a bank. Using data of existing customers, a machine learning model was built to identify which customers were likely to subscribe to the product on offer and which customers were not likely to subscribe. This was then used to power a web app which would recommend whether a customer was worth calling based on some simple details.

The model was an XGBoost Classifier that achieved:
- **90% Recall** for Subscribers
- **99% Precision** for Non-Subscribers

Using the web app, the call centre could increase their success rate while maintaining the majority of their sales:
- **76% Reduction** in Total Calls
- **90% Retention** of Sales

## The Brief

The client was a European banking institution that had run a marketing campaign to get customers to subscribe to their term deposit product. Multiple phone calls were made to customers and various data were collated. The client wanted to increase efficiency by using this data to determine beforehand whether a customer was likely or unlikely to subscribe. This would result in sales still being made but with fewer total calls required.

Therefore, the important metrics of the machine learning model were:
- High recall for subscribers = not missing out on potential sales
- High precision for non-subscribers = reliably ruling out dead-ends

The most important goal was to identify those who are likely to subscribe as this will ensure potential sales are not missed. Secondarily, being able to reliably identify those who are unlikely to subscribe would mean they could be ruled out.

## The Data

There were 13 attributes (features) relating to each of 40,000 customers, as well as whether or not they had subscribed to the product (target). All personal information had been removed for confidentiality.

| Column | Description | Datatype | Type |
| :--- | :--- | :--- | :--- |
| Age | Age of customer | Numeric | Feature |
| Duration | Last contact duration, in seconds | Numeric | Feature |
| Campaign | Number of contacts during this campaign | Numeric | Feature |
| Day | Last contact day of the month | Numeric | Feature |
| Balance | Average yearly balance (Euros) | Numeric | Feature |
| Job | Type of job | Categorical | Feature |
| Marital | Marital status | Categorical | Feature |
| Education | Level of education | Categorical | Feature |
| Contact | Contact communication type | Categorical | Feature |
| Month | Last contact month of year | Categorical | Feature |
| Default | Has credit in default? | Binary | Feature |
| Housing | Has a housing loan? | Binary | Feature |
| Loan | Has personal loan? | Binary | Feature |
| Y | Has the client subscribed to a term deposit? | Binary | Target |

## Analysis and Modelling

**Exploratory Data Analysis**

[EDA Notebook](/notebooks/exploration/exploratory_data_analysis.ipynb)
- Found no null values
- Found no invalid outliers
- Target was imbalanced 93:7 (subscribers in the minority)
- Of numerical features, duration and campaign show correlation with the target
- No multicolinearity present
- Numerical features binned into categories
- Job and month features binned due to having some very small categories
- Each categorical feature appeared to show no variety in target proportion across categories

**Modelling**

- Using [LazyPredict](/notebooks/modelling/lazy_predict.ipynb), the best candidate models were identified as:
  - [Nearest Centroid](/notebooks/modelling/nearest_centroid.ipynb)
  - [XGBoost](/notebooks/modelling/xgboost_classifier.ipynb)
  - [Quadratic Discriminant Analysis](/notebooks/modelling/quadratic_discriminant_analysis.ipynb)
  - [Gaussian Naive Bayes](/notebooks/modelling/gaussian_nb.ipynb)
- For each feature, the categories were One Hot Encoded
- For each model, GridSearchCV was used to tune the hyperparameters
- The importance of each feature was assessed using Permutation Importance
- Features negatively or negligibly impacting the results were removed
- The final model chosen was GaussianNB
- The most important feature was identified as Duration

**Model Performance**

| Model Type | Reduction in Calls | Class 1 Recall | Class 0 Precision | Class 1 Precision | 
| :---: | :---: | :---: | :---: | :---: |
| [Quadratic Discriminant Analysis](/notebooks/modelling/quadratic_discriminant_analysis.ipynb) | 13% |99% | 99% | 8% |
| [Gaussian Naive Bayes](/notebooks/modelling/gaussian_nb.ipynb) | 36% | 97% | 99% | 11% |
| [Nearest Centroid](/notebooks/modelling/nearest_centroid.ipynb) | 67% | 82% | 98% | 18% |
| [XGBoost](/notebooks/modelling/xgboost_classifier.ipynb) | 76% | 90% | 99% | 28% |

The table shows the correlation between class 1 precision and reduction in calls - a consequence of the fact the dataset was significantly imbalanced in favour of class 0. In other words, being able to identify subscribers with as few false positives as possible was key to an effective model. 