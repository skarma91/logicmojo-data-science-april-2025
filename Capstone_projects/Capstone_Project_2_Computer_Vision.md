# **Capstone Project-2: Pneumonia Detection from Chest X-Ray Images using Deep Transfer Learning**

---

## **Problem Statement**

Pneumonia is a severe lung infection that can cause difficulty in breathing and can be fatal if not diagnosed early. Traditional diagnosis using X-rays relies heavily on expert radiologists, which can be time-consuming and prone to subjectivity. The objective of this project is to develop an **automated deep learning model** that can accurately classify **chest X-ray images** as **Normal** or **Pneumonia** using **transfer learning** techniques.  

This project aims to leverage pre-trained convolutional neural networks (CNNs) to extract robust image features and fine-tune them on the pneumonia dataset to achieve high diagnostic accuracy.

---

## **Dataset Description**

**Dataset Link:** [Chest X-Ray Pneumonia - Kaggle](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)

The dataset consists of chest X-ray images categorized into two classes:
- **Normal:** Chest X-rays of healthy individuals.
- **Pneumonia:** Chest X-rays of patients diagnosed with pneumonia.

**Dataset Statistics:**
- Training images: ~5,216  
- Validation images: ~16  
- Test images: ~624  
- Image type: Grayscale and RGB (JPEG format)
- Image dimensions: Vary across samples

Each image belongs to one of two folders (`NORMAL`, `PNEUMONIA`) within respective train, validation, and test directories.

---

## **Objectives**

1. Load and preprocess the chest X-ray dataset for deep learning tasks.  
2. Apply **transfer learning** using pre-trained CNN models such as VGG16, ResNet50, DenseNet or Inception.  
3. Fine-tune the pre-trained model on the pneumonia dataset.  
4. Implement data augmentation to improve model generalization.  
5. Evaluate model performance using appropriate classification metrics.  
6. Compare performances of different transfer learning architectures.  

---

## **Steps to Follow**

### **1. Data Loading and Exploration**

- Download and organize the dataset into training, validation, and test folders.
- Load sample images using `matplotlib` or `cv2` to understand the data structure.
- Display class distribution in the training and test sets.
- Check for potential data imbalance between classes.

### **2. Data Preprocessing**

- Resize all images to a fixed dimension (e.g., 224x224 or 299x299).
- Normalize pixel values (scale between 0 and 1 or standardize).
- Apply **data augmentation** using transformations like:
  - Random rotations
  - Horizontal/vertical flips
  - Shifts and zooms
- Split data appropriately into training, validation, and test sets.

### **3. Develop and train the CNN model from scratch**

- Create your own CNN architecture to solve the problem.
- Train it from scratch.
- Note down its performance.

### **4. Model Development using Transfer Learning**

Use pre-trained models on **ImageNet** as the base for transfer learning. Possible architectures (not exhaustive):
- **VGG16**
- **ResNet50**
- **InceptionV3**
- **densenet121**

Steps:
1. Load the pre-trained model without the top (fully connected) layers.
2. Add custom classification layers:
   - GlobalAveragePooling2D
   - Dense layers with Dropout regularization
   - Output layer with sigmoid activation for binary classification
3. Freeze base layers during initial training.
4. Fine-tune selective layers of the base model for better feature adaptation.

### **5. Model Compilation**

- **Loss Function:** Binary Cross-Entropy  
- **Optimizer:** Adam or RMSprop  
- **Learning Rate Scheduling:** Implement callbacks like ReduceLROnPlateau or EarlyStopping for efficient training.

### **6. Model Training**

- Train the model on augmented data. 
- Use validation data to monitor overfitting.
- Plot training vs validation accuracy and loss curves.
- Experiment with different batch sizes and epochs for optimal results.

### **7. Model Evaluation**

Evaluate the model on the **test dataset** using:
- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- ROC Curve and AUC Score

### **8. Model Comparison**

Compare performance across different pre-trained architectures (e.g., VGG16 vs ResNet50 vs Inception etc.) in terms of accuracy (and other metrics), model size, and inference time etc.

---

## **Insights and Conclusion**

- Discuss how transfer learning improved model accuracy compared to training from scratch.
- Identify potential reasons for misclassifications and propose improvements.
- Conclude with the model’s readiness for practical clinical deployment and its limitations.

---

## **Deliverables**

1. **Jupyter Notebook (.ipynb):** Complete code with preprocessing, model training, and evaluation.  
2. **Project Report (.md or .pdf):** Detailed explanation of the approach, results, and insights.  
3. **Presentation Slides:** (not more than 10 slides) Summarized overview of the methodology and findings.

---

## **Upload the project deliverables**

- Upload the solved notebook(s), Project Report, and Presentation Slides in the google drive location: https://drive.google.com/drive/folders/1eZ02yLW-jtpXFKcdXnIrzgPW8g-Vuny2?usp=drive_link

- Also upload the solved notebook and the documents to your respective github repository.
