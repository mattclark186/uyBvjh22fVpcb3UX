# Call Centre Sales Predictions

This project aimed to improve the success rate of sales calls made by the call centre of a bank. Using data of existing customers, a machine learning model was built to identify which customers were likely to subscribe to the product on offer and which customers were not likely to subscribe.

The final model was a Gaussian Naive Bayes classifier that achieved:
- **97% Recall** for Subscribers
- **99% Precision** for Non-Subscribers

It was also found that the most significant factor in determining whether a customer would subscribe was the duration of their last contact, with a longer duration increasing the likelihood.

## The Brief

The client was a European banking institution that had run a marketing campaign to get customers to subscribe to their term deposit product. Multiple phone calls were made to customers to ensure product subscription and various data were collated. The client wanted to determine which customers would and wouldn't subscribe based on this data in order to improve the success rate of their calls. They also wanted to know which factors were the most significant.

## The Data

There were 13 attributes relating to each of 40,000 customers, as well as whether or not they had subscribed to the product. All personal information had been removed for confidentiality.

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