# # Web App
# In[10]:


import streamlit as st
import pandas as pd

st.write("Pandas:", pd.__version__)

try:
    import joblib
    st.write("Joblib:", joblib.__version__)
except Exception as e:
    st.error(f"Joblib failed: {e}")


# In[14]:
model = joblib.load('src/models/bank_loan_model.joblib')

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Manrope', sans-serif !important;
}

[data-testid="stAppViewContainer"] * {
    font-family: 'Manrope', sans-serif !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('## Customer Subscription Predictor')
st.markdown('**Welcome! Use this app to confidently determine whether a customer is worth contacting based on a few simple details.**')

tab1, tab2 = st.tabs(['Predictor', 'How Does it Work?'])

with tab1:
    st.write('**Enter customer details below and click predict.**')
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        age_group = st.selectbox(
            'Age Group',
            ['18-24', '25-34', '35-44', '45-59', '60+'])
        education = st.selectbox(
            'Education Level', 
            ['Primary', 'Secondary', 'Tertiary', 'Unknown'])
    with col2:
        balance_group = st.selectbox(
            'Average Yearly Balance',
            ['Negative', '€0-€100', '€100-€200', '€200-€500', '€500-€1,000', '€1,000-€3,000', '€3,000-€5,000', '€5,000-€10,000', '€10,000+'])
        contact = st.selectbox(
            'Contact Method',
            ['Cellular', 'Telephone', 'Unknown'])
    with col3:
        loan = st.selectbox(
            'Has Personal Loan?',
            ['Yes', 'No'])
        housing = st.selectbox(
            'Has Housing Loan?',
            ['Yes', 'No'])
    with col4:
        quarter = st.selectbox(
            'Quarter of Last Contact',
            ['Q1', 'Q2', 'Q3', 'Q4'])
        duration_group = st.selectbox(
            'Duration of Last Contact',
            ['0-1 min', '1-2 min', '2-4 min', '4-6 min', '6-10 min', '10-15 min', '15-20 min', '20+ min'])

    education_mapping = {
        'Primary': 'primary',
        'Secondary': 'secondary',
        'Tertiary': 'tertiary',
        'Unknown': 'unknown'
    }
    housing_mapping = {
        'Yes': 'yes',
        'No': 'no'
    }
    loan_mapping = {
        'Yes': 'yes',
        'No': 'no'
    }
    contact_mapping = {
        'Cellular': 'cellular',
        'Telephone': 'telephone',
        'Unknown': 'unknown'
    }
    quarter_mapping = {
        'Q1': 'q1',
        'Q2': 'q2',
        'Q3': 'q3',
        'Q4': 'q4'
    }
    age_mapping = {
        '18-24': '(0, 24]',
        '25-34': '(24, 34]',
        '35-44': '(34, 45]',
        '45-59': '(45, 59]',
        '60+': '(59, 100]'
    }
    balance_mapping = {
        'Negative': '(-10000, 0]',
        '€0-€100': '(0, 100]',
        '€100-€200': '(100, 200]',
        '€200-€500': '(200, 500]',
        '€500-€1,000': '(500, 1000]',
        '€1,000-€3,000': '(1000, 3000]',
        '€3,000-€5,000': '(3000, 5000]',
        '€5,000-€10,000': '(5000, 10000]',
        '€10,000+': '(10000, 200000]'
    }
    duration_mapping = {
        '0-1 min': '(0, 60]',
        '1-2 min': '(60, 120]',
        '2-4 min': '(120, 240]',
        '4-6 min': '(240, 360]',
        '6-10 min': '(360, 600]',
        '10-15 min': '(600, 900]',
        '15-20 min': '(900, 1200]',
        '20+ min': '(1200, 5000]'
    }
    
    education = education_mapping[education]
    housing = housing_mapping[housing]
    loan = loan_mapping[loan]
    contact = contact_mapping[contact]
    quarter = quarter_mapping[quarter]
    age_group = age_mapping[age_group]
    balance_group = balance_mapping[balance_group]
    duration_group = duration_mapping[duration_group]
    
    customer = pd.DataFrame([{
        "education": education,
        "housing": housing,
        "loan": loan,
        "contact": contact,
        "age_group": age_group,
        "quarter": quarter,
        "balance_group": balance_group,
        "duration_group": duration_group
    }])
    
    st.write('')
    
    button_col1, button_col2, button_col3 = st.columns([1, 5, 1])
    
    with button_col2:
        predict_button = st.button('Predict', type='primary', use_container_width=True)
    
    result_col1, result_col2, result_col3, result_col4 = st.columns([2, 2, 2.5, 2])
    
    with result_col2:
        if predict_button:
            prediction = model.predict(customer)[0]
            probability = model.predict_proba(customer)[0, 1]
            
            if prediction == 1:
                st.image('images/call.png', width=140)
            else:
                st.image('images/no_call.png', width=140)
    
    with result_col3:
        if predict_button:
            prediction = model.predict(customer)[0]
            probability = model.predict_proba(customer)[0, 1]
            
            if prediction == 1:
                st.markdown('## Call Customer')
            else:
                st.markdown('## Do Not Call Customer')

with tab2:
    st.markdown('**How Does the Predictor Work?**')
    
    col1, col2 = st.columns([1.2, 1])
    
    with col1:
        with st.container(border=True):
            st.markdown('**Historical Data**')
            st.markdown('Thousands of historical customer records were used to train an **XGBoost machine learning model**.')
            st.markdown('The model has **learned patterns in customer characteristics** associated with whether that individual subscribed.')
            st.markdown('When provided with the details of a prospective customer, the model **estimates their likelihood of subscribing** and uses this prediction to determine whether they should be contacted.')
    
    with col2:
        with st.container(border=True):
            st.markdown('**Prediction Accuracy**')
            st.markdown('- **90% of subscribers identified**, meaning nearly all possible revenue is captured.')
            st.markdown('- **75% reduction in total calls** required, significantly increasing efficiency.')
            st.markdown('- **99% of customers ruled out would not subscribe**, allowing sales calls to be focused on more promising prospects.')
# In[ ]:




