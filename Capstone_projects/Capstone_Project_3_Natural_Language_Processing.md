# **Capstone Project-3: Text Summarization using Sequence-to-Sequence Transformer Models**

---

## **Project Title:**  
**Abstractive Text Summarization on News Articles using Transformer-based Models**

---

## **Problem Statement**

With the vast amount of news and textual data being generated daily, it becomes challenging for readers to consume and understand all content efficiently. **Automatic text summarization** helps in condensing long articles into concise summaries while retaining the core meaning and context.  

The objective of this project is to build an **abstractive text summarization model** using transformer-based architectures like **BART** or **T5**, trained on the **CNN/DailyMail News Dataset**. The model should generate fluent and coherent summaries that capture the essence of the input article.

This project explores advanced **Natural Language Processing (NLP)** techniques and deep learning models to automatically generate high-quality summaries for news articles.

---

## **Dataset Description**

**Dataset Link:** [Newspaper Text Summarization (CNN/DailyMail)](https://www.kaggle.com/datasets/gowrishankarp/newspaper-text-summarization-cnn-dailymail)

This dataset is based on the well-known **CNN/DailyMail dataset**, commonly used for abstractive text summarization tasks.

**Dataset Information:**
- Each data point consists of:
  - **Article:** The full text of a news article.
  - **Highlights:** The human-written summary of the article (used as ground truth).

**Number of Samples:**  
Approximately 300,000 article-summary pairs.  

**Type:**  
Text corpus suitable for supervised learning tasks (seq2seq).

---

## **Objectives**

1. Perform **text cleaning and preprocessing** suitable for NLP modeling.  
2. Implement a **sequence-to-sequence (seq2seq)** architecture for summarization using pre-trained transformer models.  
3. Fine-tune pre-trained **BART** or **T5** models on the CNN/DailyMail dataset.  
4. Evaluate model performance using standard summarization metrics (ROUGE, BLEU).  
5. Compare model performance before and after fine-tuning.  
6. Demonstrate model inference by generating summaries for new/unseen articles.  
7. Provide qualitative and quantitative analysis of model performance.

---

## **Steps to Follow**

### **1. Data Loading and Exploration**

- Download and load the dataset using pandas.
- Display a few article-summary pairs to understand structure and length.
- Analyze text statistics:
  - Average article length
  - Average summary length
  - Token distributions
- Visualize text lengths using histograms to decide truncation limits.

### **2. Data Preprocessing**

Perform standard NLP text cleaning steps:
- Lowercasing (optional, depending on tokenizer).
- Removing unwanted symbols or HTML tags.
- Truncate long texts to manageable token lengths (e.g., 512–1024 tokens).
- Tokenize text using the pre-trained tokenizer (e.g., `BartTokenizer` or `T5Tokenizer`).
- Create training and validation splits (e.g., 80-20).

### **3. Model Development**

Use transformer-based architectures for abstractive summarization:

#### **Approach 1: BART (Bidirectional and Auto-Regressive Transformer)**
- Model: `facebook/bart-large-cnn`
- Architecture: Encoder-decoder transformer trained for sequence generation.
- Task: Fine-tune on article-summary pairs.

#### **Approach 2: T5 (Text-to-Text Transfer Transformer)**
- Model: `t5-base` or `t5-large`
- Task framing: Prefix each input with `"summarize: "` before passing to the model.

Both models leverage transfer learning from pre-training on massive text corpora.
Use both the appraoches and compare their performance for the given task.

---

### **4. Model Training**

- Use the Hugging Face Transformers library for implementation.
- Define model inputs and outputs using tokenized article-summary pairs.
- Use GPU acceleration for faster training. (Use google colab if necessary)
- **Training hyperparameters:** Suggested values (feel free to use other values)
  - Batch size: 4–8
  - Epochs: 3–5
  - Learning rate: 3e-5
  - Optimizer: AdamW
  - Scheduler: Linear decay
- Implement gradient clipping and checkpoint saving.

### **5. Model Evaluation**

Use both **quantitative** and **qualitative** evaluation methods:

#### **Quantitative Metrics:**
- **ROUGE-1:** Overlap of unigrams between generated and reference summaries.
- **ROUGE-2:** Overlap of bigrams.
- **ROUGE-L:** Longest common subsequence-based metric.
- **BLEU Score:** Measures n-gram precision against reference summary.

#### **Qualitative Evaluation:**
- Generate summaries for unseen articles.
- Compare generated vs reference summaries manually.
- Assess fluency, coherence, and factual accuracy.

### **6. Hyperparameter Tuning**

Experiment with:
- Different maximum token lengths (e.g., 256, 512, 1024).
- Different pre-trained models (BART-base, T5-small, Pegasus).
- Learning rate and warmup steps.

Monitor validation loss and ROUGE metrics to select the best configuration.

### **7. Inference and Results Visualization**

- Generate summaries on the test dataset.
- Visualize and compare example outputs.
- Plot ROUGE scores across epochs.
- Create a side-by-side comparison table:

| Article (Excerpt) | Reference Summary | Model Generated Summary |
|--------------------|--------------------|---------------------------|
| “The stock market fell sharply today due to rising oil prices...” | “Rising oil prices cause market decline.” | “Oil price surge triggers stock market fall.” |

---

## **Insights and Conclusion**

- Summarization models like BART and T5 achieve fluent and coherent summaries with strong ROUGE scores.  
- Abstractive models outperform extractive baselines by generating more natural and concise summaries.  
- The model captures the essence of long news articles while maintaining readability.  
- Further improvements can be achieved with fine-tuning on domain-specific datasets or through reinforcement learning-based reward optimization.

---

## **Deliverables**

1. **Jupyter Notebook (.ipynb):**  
   Complete notebook with data loading, preprocessing, model training, and evaluation steps.

2. **Project Report (.md or .pdf):**  
   Summarizes methodology, results, visualizations, and insights.

3. **Presentation Slides:** not more than 10 slides summarizing methodology, results, visualizations, and insights.

4. **Sample Summaries File: (50-100 samples)**  
   Text file or CSV with sample input articles, reference summaries, and generated summaries.

5. **Optional Deployment:**  
   - Create a small web app using Streamlit for interactive summarization.  
   - Input: News article text (provided by user)
   - Output: Model-generated summary  

---

## **Upload the project deliverables**

- Upload the solved notebook(s), Project Report, Presentation Slides, and Sample File in the google drive location: https://drive.google.com/drive/folders/1vLH8TKTMVb_mP7IM89-XKkdX0ZTkcQyL?usp=drive_link

- Also upload the solved notebook and the documents to your respective github repository.