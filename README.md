Thyroid Disease Detection
=================================================================================================================================================

Machine Learning Project
------------------------

Thyroid disease is a common cause of medical diagnosis and prediction, with an onset that is difficult to forecast in medical research. The thyroid gland is one of our body's most vital organs. Thyroid hormone releases are responsible for metabolic regulation. Hyperthyroidism and hypothyroidism are one of the two common diseases of the thyroid that releases thyroid hormones in regulating the rate of body's metabolism. The main goal is to predict the estimated risk on a patient's chance of obtaining thyroid disease or not.

Webpage Link
=================================================================================================================================================

https://thyroid-disease-detection-v2.herokuapp.com/
------------------------

Demo
=================================================================================================================================================

coming soon
------------------------

Technical Aspects
===================================================================================================================================================

- Python 3.7 and more
- Important Libraries: sklearn, pandas, numpy, matplotlib & seaborn
- UI: Streamlit
- IDE: Jupyter Notebook, Pycharm & VSCode
- Database: Cassandra
- Deployment: Heroku

How to run this app
===================================================================================
Code is written in Python 3.7 and more. If you don't have python installed on your system, click here https://www.python.org/downloads/ to install.
- Create virtual environment - conda create -n myenv python=3.7
- Activate the environment - conda activate myenv
- Install the packages - pip install -r requirements.txt
- Run the app - streamlit run app.py

Workflow
=====================================================================================
Data Collection
---------------------------------------------------
Thyroid Disease Data Set from UCI Machine Learning Repository.

Link:https://archive.ics.uci.edu/ml/datasets/thyroid+disease

Data Pre-processing
-----------------------------------

- handle missing values 
- Outliers detection and removal by boxplot and percentile methods
- Categorical features handling by ordinal encoding and label encoding
- Drop unnecessary columns

Model Creation and Evaluation
-----------------------------------
- Various classification algorithms like Random Forest, XGBoost, Decision Tree etc tested.
- Random Forest, XGBoost and Decision Tree were all performed well. XGBoost was chosen for the final model training and testing.
- Hyper parameter tuning was performed using GridSearchCV
- Model performance evaluated based on accuracy, confusion matrix, classification report.

Model Deployment
---------------------------------------
The final model is deployed on Heroku using Streamlit.

User Interface
========================================================================
=====![Dashboard](https://user-images.githubusercontent.com/76996837/181601133-baeb8591-3c79-47a6-9854-8e3601962f6d.jpg)

Project Documents
=======================================================================
- HLD: https://github.com/SuShAnTBiShT407/Thyroid-Disease-Detection.github.io/tree/main/Docs/HLD

- LLD: https://github.com/SuShAnTBiShT407/Thyroid-Disease-Detection.github.io/tree/main/Docs/LLD

- Wireframe: https://github.com/SuShAnTBiShT407/Thyroid-Disease-Detection.github.io/tree/main/Docs/WireFrame)

- Detailed Project Report: https://github.com/SuShAnTBiShT407/Thyroid-Disease-Detection.github.io/blob/main/Docs/DPR/TDD_DPR.docx

Author
==========================================================
Sushant Bisht 

Help Me Improve
=========================================================
Hello guys if you find any bug please consider raising issue I will address them asap.
