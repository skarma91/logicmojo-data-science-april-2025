# Mini-Project: Transfer Learning for Image Classification

## Project Overview

In this assignment, you will explore **transfer learning** techniques for **image classification** using popular **pre-trained deep learning models**. The task involves building and comparing models that classify food images into three categories — **Pizza**, **Steak**, and **Sushi**. This project will help you understand how to leverage pre-trained CNN architectures, fine-tune them for a specific dataset, and evaluate their performance.

### Dataset

**Dataset Link:** [pizza_steak_sushi.zip](https://github.com/skarma91/logicmojo-data-science-april-2025/blob/main/Assignments/Assignment-12-Computer_Vision/pizza_steak_sushi.zip)

Download the dataset in your local machine.

**Description:**  
The dataset contains images of three distinct food items:
- **Pizza**
- **Steak**
- **Sushi**

Each image belongs to one of the above classes. Your goal is to build and fine-tune a classification model capable of correctly predicting the category of a given image.

**Dataset Structure Example:**
```
pizza_steak_sushi/
│
├── train/
│   ├── pizza/
│   ├── steak/
│   └── sushi/
│
└── test/
    ├── pizza/
    ├── steak/
    └── sushi/
```

You will use the **training set** to train your models and the **test set** to evaluate their generalization performance.


### Objective

The main objective of this assignment is to:
1. Implement **transfer learning** using pre-trained CNN models (e.g., VGG16, ResNet50, InceptionV3, DenseNet121). Check the [documentation](https://docs.pytorch.org/vision/main/models.html) on how to use pre-trained CNN models in pytorch.
2. Compare the performance of these models on the given dataset.
3. Analyze which model performs best and why.
4. Document your findings with clear visualizations, metrics, and discussion.

### Skills Practiced

By completing this assignment, you will practice and strengthen the following skills:
- Understanding and applying **transfer learning** in computer vision.
- Using **PyTorch** for implementing CNN architectures.
- Performing **data preprocessing and augmentation** for image datasets.
- Fine-tuning **pre-trained models** for custom tasks.
- Evaluating models using standard metrics (accuracy, confusion matrix, classification report).
- Preparing **visual and written communication** of model results.

---

## Deliverables

Your submission should include the following two deliverables:

### 1. Code Notebook
A well-documented Jupyter Notebook (`.ipynb`) that includes:
- Properly formatted and commented code.
- Clear visualizations (training curves, confusion matrices, sample predictions).
- Comparison of different model performances.
- Explanations for each major step.

**Expected file name:**  
`Assignment-12_CNN_Transfer_Learning_<your_name>_<your_surname>.ipynb`

### 2. Project Report (2–4 pages)
A concise report summarizing:
- The approach you took.
- Details about preprocessing and model choices.
- Training strategy and hyperparameters.
- Evaluation metrics and comparison.
- Observations, challenges faced, and lessons learned.
- Conclusion and possible improvements.

**Expected file name:**  
`Assignment-12_CNN_Transfer_Learning_Report_<your_name>_<your_surname>.pdf`

---

## Suggested Milestones

### Milestone 1: Problem Setup
- Load and explore the dataset.
- Visualize a few images from each class.
- Split the dataset into **train**, **validation**, and **test** sets (if not already split).
- Identify the number of images per class (check for imbalance).
- Set up the environment.


###  Milestone 2: Preprocessing and Data Augmentation
- Apply **image resizing** to make all images uniform in size.
- Normalize pixel values.
- Apply **data augmentation techniques** such as:
  - Random rotations
  - Flipping
  - Cropping
  - Color jitter
  etc.

You may use the techniques described in [this kaggle notebook](https://www.kaggle.com/code/mohamedmustafa/7-data-augmentation-on-images-using-pytorch)
- Create **DataLoaders** (PyTorch).


### Milestone 3: Implement Transfer Learning
Use at least **two or more** pre-trained models from the following list:
- **VGG16**
- **ResNet50**
- **InceptionV3**
- **DenseNet121**
- (Optional: EfficientNet, MobileNet)

For each model:
1. Load pre-trained weights (e.g., from ImageNet).
2. Freeze the base layers initially.
3. Add and train a custom classification head.
4. Fine-tune some of the deeper layers to improve accuracy.
5. Record training/validation loss and accuracy.

You may use learning rate schedulers, early stopping, and other regularization techniques as needed.


### Milestone 4: Evaluation and Communication
- Evaluate all models on the **test set**.
- Compute and compare:
  - **Accuracy**
  - **Precision, Recall, F1-score**
  - **Confusion Matrix**
- Visualize:
  - Training vs. validation accuracy curves.
  - Misclassified examples.
- Discuss:
  - Which model performed best and why?
  - What differences did you observe between models?
  - How did fine-tuning affect the performance?


### Tips
- Start small — experiment with one model first before trying multiple.
- Use GPU runtime if available (Kaggle, Colab, or local setup).
- Save model checkpoints regularly.
- Visualize results frequently to catch issues early.
- Interpret your model’s decisions (optional but encouraged).

---

## Steps to upload the assignment solution

- Upload the solved notebook (`Assignment-12_CNN_Transfer_Learning_<your_name>_<your_surname>.ipynb`) and report document (`Assignment-12_CNN_Transfer_Learning_Report_<your_name>_<your_surname>.pdf`) in the google drive location: https://drive.google.com/drive/folders/1qYEz9ihu8c1fznepwCdLtdL-WMQ4_3OJ?usp=drive_link

- Also upload the solved notebook and document to your respective github repository.
