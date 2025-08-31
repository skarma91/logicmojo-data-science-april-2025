# Mini-Project: Wholesale Customers Clustering

## Project Overview
- **Dataset**: [Wholesale Customers Data Set (UCI)](https://archive.ics.uci.edu/dataset/292/wholesale+customers)
  - The dataset is provided in this github folder for your reference.  
- **Objective**: Perform customer segmentation using clustering techniques on wholesale spending data.  
- **Skills Practiced**:  
  - Exploratory Data Analysis (EDA)  
  - Data preprocessing (scaling, handling categorical variables)  
  - Applying clustering algorithms (K-Means, Hierarchical, DBSCAN)  
  - Cluster evaluation (Elbow Method, Silhouette Score)  
  - Profiling & interpreting customer clusters  
  - Communicating results  

---

## Deliverables
- **Code Notebook** including:  
  - EDA → preprocessing → clustering → evaluation → cluster profiling  
- **Project Report (2–3 pages)** with:  
  - Problem framing & choice of clustering methods  
  - Key EDA insights (distribution of spending features)  
  - Explanation of chosen number of clusters (Elbow/Silhouette)  
  - Cluster profiling (describe each segment in business terms)  
  - Visualizations (scatterplots, PCA/t-SNE plots for cluster separation)  
  - (Optional) Recommendations for how business can use the segmentation  
- **Optional (extra credit)**: Interactive dashboard (Streamlit/Dash) to visualize clusters and explore customer profiles  

---

## Suggested Milestones

### **Problem Setup & EDA**
- Load dataset and inspect features
- Explore distributions & detect skew/outliers  
- Visualize feature correlations  

### **Preprocessing**
- Scale numeric features (StandardScaler/MinMaxScaler)  
- Consider log-transform for skewed data  
- Drop or encode categorical features (`Channel`, `Region`) depending on approach  
- Prepare clean feature matrix for clustering  

### **Clustering & Evaluation**
- Apply **K-Means** with different values of `k`  
- Use **Elbow Method** & **Silhouette Score** to select optimal cluster number  
- Try **Hierarchical Clustering** and compare results  
- Experiment with DBSCAN  

### **Cluster Profiling & Communication**
- Assign customers to clusters  
- Profile clusters (mean/median spending per category)  
- Visualize clusters using PCA/2D scatterplots  
- Interpret clusters in business terms (e.g., “High Grocery & Detergents buyers”, “Fresh product oriented buyers”)  
- Write project report & polish notebook for readability  

---

## Steps to upload the assignment solution

- Create the notebook `Assignment-10-Clustering-<your_name>_<your_surname>.ipynb` in your local machine and solve the assignment.
- Upload the solved notebook and document in the google drive location: https://drive.google.com/drive/folders/1F57aE4xzprtvyGrtpNaI0dBUiF8CqEl6?usp=drive_link 
- Also upload the solved notebook and document to your respective github repository.