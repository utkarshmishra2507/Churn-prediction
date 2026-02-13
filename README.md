🛡️ Customer Churn Predictor
============================

**An End-to-End Machine Learning Web Application for Banking Analytics**

This repository contains a full-stack Machine Learning project designed to predict the likelihood of a bank customer "churning" (leaving the bank). It leverages a robust classification pipeline and a FastAPI/Flask-powered web interface to provide real-time risk assessments.

Overview
-----------

The **Customer Churn Predictor** uses historical customer data—including credit scores, geography, tenure, and balance—to identify high-risk accounts. By predicting churn before it happens, businesses can implement proactive retention strategies.

Tech Stack
--------------

*   **Machine Learning:** Python, Scikit-Learn, XGBoost/LightGBM
    
*   **Data Processing:** Pandas, NumPy
    
*   **Backend:** FastAPI / Flask (Python)
    
*   **Frontend:** HTML5, CSS3 (Glassmorphism UI)
    
*   **Environment:** Pip & Virtualenv
    

Project Workflow
-------------------

1.  **Exploratory Data Analysis (EDA):** Identified key churn drivers such as Age and Balance.
    
2.  **Feature Engineering:** Applied One-Hot Encoding for categorical variables (Geography, Gender) and feature scaling.
    
3.  **Model Training:** Trained and cross-validated multiple classifiers (Random Forest, XGBoost) to optimize for **F1-Score** and **AUC-ROC**.
    
4.  **Deployment:** Built a responsive web dashboard for business users to input customer details and receive instant probability scores.
    

Installation & Setup
-----------------------

1.  git clone https://github.com/yourusername/churn-predictor.gitcd churn-predictor
    
2.  pip install -r requirements.txt
    
3.  python app.py
    

📈 Key Insights
---------------

*   **Age Factor:** Customers in the 40–50 age bracket showed the highest churn rate.
    
*   **Product Usage:** Customers with only one product were significantly more likely to leave than those with multiple products.
