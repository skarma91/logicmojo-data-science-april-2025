# Mini-Project: Bank Marketing Classification

## Project Overview
- **Dataset**: [Bank Marketing Dataset (UCI / Kaggle)](https://www.kaggle.com/datasets/henriqueyamahata/bank-marketing)
  - The dataset and the dataset description are provided in this github folder for your reference.  
- **Objective**: Predict whether a customer subscribes to a term deposit (`yes`/`no`) after a marketing campaign.  
- **Skills Practiced**:  
  - Exploratory Data Analysis (EDA)  
  - Preprocessing of categorical & numerical features  
  - Handling class imbalance  
  - Classification modeling (logistic regression, decision trees, ensembles)  
  - Model evaluation with classification metrics  
  - Interpretation & communication of findings  

---

## Deliverables
- **Code Notebook** (clean & documented) including:  
  - EDA → preprocessing → modeling → evaluation → conclusions  
- **Project Report (2–4 pages)** with:  
  - Problem framing & choice of evaluation metric (Accuracy, Precision/Recall, F1, ROC-AUC)  
  - EDA insights with key plots (class imbalance, feature-target relationships)  
  - Preprocessing summary (encoding, scaling, missing values handling)  
  - Model comparison table (baseline vs tuned)  
  - Feature importance  
  - Error analysis (misclassifications, precision-recall tradeoff)  
- **Optional**: Deploy a simple Streamlit app to input customer details & predict subscription likelihood
  - In the web app, predict the subscription likelihood based on only few (5-10) important features which will be provided by user. 

---

## Suggested Milestones

### **Problem Setup & EDA**
- Load dataset & inspect target distribution (`yes`/`no`)  
- Identify categorical vs numeric features  
- Explore imbalance in classes  
- Visualize key relationships (e.g., age vs subscription, job type vs subscription)  

### **Preprocessing & Baselines**
- Handle missing values if any  
- Encode categorical variables (OneHot/Ordinal)  
- Scale numeric variables if required  
- Train/test split  
- Build baseline models:  
  - Logistic Regression  
  - Decision Tree  
  - Naive Bayes 

### **Advanced Models & Imbalance Handling**
- Try Random Forest, Gradient Boosting (XGBoost/LightGBM)  
- Apply techniques for class imbalance (if required):  
  - Class weights  
  - Oversampling / Undersampling (e.g., SMOTE)  
  - Class weight adjustment in different algorithms
- Cross-validation for robust evaluation  
- Hyperparameter tuning (GridSearchCV/Optuna)  

### **Evaluation & Communication**
- Compare models using multiple metrics (Accuracy, F1, ROC-AUC, confusion matrix)  
- Plot ROC & Precision-Recall curves  
- Analyze feature importance 
- Perform error analysis (which customers are misclassified?)  
- Write report & finalize notebook for submission

---

## Steps to upload the assignment solution

- Create the notebook `Assignment-09-Classification-<your_name>_<your_surname>.ipynb` in your local machine and solve the assignment.
- Upload the solved notebook and document in the google drive location: https://drive.google.com/drive/folders/1kxaikcl0lnE6ZeikFJJ5Fo-nUOPmWFHl?usp=drive_link
- Also upload the solved notebook and document to your respective github repository.
