# Assignment-8-Mini-Project: House Prices Regression

## Project Overview
- **Dataset**: [House Prices – Advanced Regression Techniques (Kaggle)](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)
    - The dataset and the dataset description are provided in this github folder for your reference.
- **Objective**: Predict sale prices of houses using tabular features (categorical + numerical).  
- **Skills Practiced**:  
  - Exploratory Data Analysis (EDA)  
  - Data preprocessing (missing values, encoding, scaling)  
  - Feature engineering (transformations, interactions)  
  - Regression modeling (linear, regularized, ensemble)  
  - Model evaluation & interpretation  
  - Communication of findings  

---

## Deliverables
- **Code Notebook** (well-structured & documented) including:  
  - EDA → preprocessing → modeling → evaluation → conclusions  
- **Project Report Document (2–4 pages)** with:  
  - Problem framing & evaluation metric (RMSE / RMSLE) 
  - Key EDA insights (plots + commentary)  
  - Feature engineering summary  
  - Model comparison table (baseline vs tuned models)  
  - Interpretation (feature importance)  
  - Error analysis + improvement suggestions  
- **Optional**: Simple web app (Streamlit) for house price prediction
  - The web app should have 5-10 most important input features which user can enter manually 

---

## Suggested Milestones

### **Problem Setup & EDA**
- Load dataset, understand target variable (`SalePrice`)  
- Check missing values, split features into categorical & numeric  
- Visualize target distribution  
- Correlation heatmap & scatterplots of features vs target (bi-variate analysis) 

### **Preprocessing & Baselines**
- Handle missing values (imputation strategies)  
- Encode categorical features (OneHot/Ordinal)  
- Scale numeric features  
- Train/test split  
- Build baseline models:  
  - Linear Regression  
  - Ridge/Lasso  
  - Decision Tree  

### **Advanced Models & Feature Engineering**
- Train advanced models: Random Forest, Gradient Boosting (XGBoost/LightGBM)  
- Perform feature extraction (interactions, polynomial features, transforms)
- Perform feature selection
- Apply cross-validation for robust evaluation  
- Tune hyperparameters (GridSearchCV/Optuna)  

### **Model Evaluation & Communication**
- Compare models using RMSE (table of results), you can use other metric as suitable.
- Interpret results with feature importance 
- Perform error analysis (check worst predictions)  
- Write project report & polish notebook for readability

---

## Steps to upload the assignment solution

- Create the notebook `Assignment-08-Regression-<your_name>_<your_surname>.ipynb` in your local machine and solve the assignment.
- Upload the solved notebook in the google drive location: https://drive.google.com/drive/folders/15h_ksmpob2SjmFigY1CGSzKB63tbw4oP?usp=drive_link 
- Also upload the solved notebook to your respective github repository.