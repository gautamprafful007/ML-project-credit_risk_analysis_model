import streamlit as st
from prediction_helper import predict   # Ensure this is correctly linked to your prediction_helper.py
from PIL import Image , ImageOps

# Set the page configuration and title
st.set_page_config(page_title="Reserve Bank : Credit Risk Analysis", page_icon="📊")
st.title("Reserve Bank : Credit Risk Analysis")

# Create rows of three columns each
row1=st.columns(3)
row2=st.columns(3)
row3=st.columns(3)
row4=st.columns(3)

# Assign inputs to the first row with default values
with row1[0]:
    age = st.number_input('Age', min_value=18, step=1, max_value=100, value=28)
with row1[1]:
    income = st.number_input('Income', min_value=0, value=1200000)
with row1[2]:
    loan_amount = st.number_input('Loan Amount', min_value=0, value=2560000)

# Calculate Loan to Income Ratio and display it
loan_to_income_ratio = loan_amount / income if income>0 else 0

# Assign inputs to the remaining controls
with row2[0]:
    st.text("Loan to income ratio")
    st.text(f'{loan_to_income_ratio:.2f}')
with row2[1]:
    loan_tenure_months=st.number_input('Loan Tenure (months)',min_value=0,step=1,value=36)
with row2[2]:
    average_dpd_per_delinquency=st.number_input('Average DPD',min_value=0,value=20)

with row3[0]:
    delinquent_ratio = st.number_input('Delinquency Ratio', min_value=0, max_value=100, step=1, value=30)
with row3[1]:
    credit_utilization_ratio = st.number_input('Credit Utilization Ratio', min_value=0, max_value=100, step=1, value=30)
with row3[2]:
    num_open_accounts = st.number_input('Open Loan Accounts', min_value=1, max_value=4, step=1, value=2)

with row4[0]:
    residence_type=st.selectbox('Recedence Type',['Owned','Rented','Mortgage'])
with row4[1]:
    loan_purpose=st.selectbox('Loan Purpose',['Education','Home','Auto','Personal'])
with row4[2]:
    loan_type=st.selectbox('Loan Type',['Unsecured','Secured'])


# Button to calculate risk
if st.button("Calculate Risk"):
    probability,credit_score,rating=predict(age, income, loan_amount, loan_tenure_months, average_dpd_per_delinquency,
                                                delinquent_ratio, credit_utilization_ratio, num_open_accounts,
                                                residence_type, loan_purpose, loan_type)
    
    # Display the results
    st.write(f'Default Probability : {probability:.2%}')
    st.write(f'Credit Score : {credit_score:.2f}')
    st.write(f'Rating : {rating}')




# Load image from file
image = Image.open("Feature Importance.png")

bordered_img = ImageOps.expand(image, border=5, fill='black')  # 10px black border

# Display the image
st.image(bordered_img, caption='Feature Importance ', use_container_width=True)


