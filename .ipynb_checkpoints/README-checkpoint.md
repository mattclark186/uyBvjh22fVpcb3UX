# Call Centre Sales Predictions

This project aimed to improve the success rate of sales calls made by the call centre of a bank. Using data of existing customers, a machine learning model was built to identify which customers were likely to subscribe to the product on offer and which customers were not likely to subscribe.

The final model was a Gaussian Naive Bayes classifier that achieved:
- **97% Recall** for Subscribers
- **99% Precision** for Non-Subscribers

It was also found that the most significant factor in determining whether a customer would subscribe was the duration of their last contact, with a longer duration increasing the likelihood.

## The Brief

The client was a European banking institution that had run a marketing campaign to get customers to subscribe to their term deposit product. Multiple phone calls were made to customers to ensure product subscription and various data were collated. The client wanted to determine which customers would and wouldn't subscribe based on this data in order to improve the success rate of their calls. They also wanted to know which factors were the most significant.

Therefore, the important metrics of the machine learning model were:
- High recall for subscribers = not missing out on potential sales
- High precision for non-subscribers = reliably ruling out dead-ends
- High precision for subscribers = achieving sales in the fewest total number of calls possible

The most important goal is to identify those who are likely to subscribe as this will ensure potential sales are not missed. Secondarily, being able to reliably identify those who are unlikely to subscribe would mean they could be ruled out. Similarly, if the model identifies those who will subscribe with high precision, the number of calls that end in no sale would be minimised.

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

[Modelling Notebooks](/notebooks/modelling)
- Using LazyPredict, the best candidate models were identified as:
  - Nearest Centroid
  - XGBoost
  - Quadratic Discriminant Analysis
  - Gaussian Naive Bayes
- For each feature, the categories were One Hot Encoded
- For each model, GridSearchCV was used to tune the hyperparameters
- The importance of each feature was assessed using Permutation Importance
- Features negatively or negligibly impacting the results were removed
- The final model chosen was GaussianNB
- The most important feature was identified as Duration

**Model Performance**

| Model Type | Class 1 Recall | Class 0 Precision | Class 1 Precision |
| :---: | :---: | :---: | :---: |
| Nearest Centroid | 82% | 98% | 18% |
| XGBoost | 91% | 99% | 30% |
| QDA | 99% | 99% | 8% |
| GaussianNB | 97% | 99% | 11% |

