# Assignment 13: Sequence-to-Sequence (Seq2Seq) Modeling with Attention in NLP

## Project Overview

In this assignment, you will build and train a **Sequence-to-Sequence (Seq2Seq)** model with **attention mechanism** for **machine translation**. The objective is to translate sentences from **German to English**, leveraging modern neural network architectures that combine **recurrent networks and attention layers**. 

This project will give you practical experience with key NLP concepts like **encoder-decoder architecture**, **context vectors**, and **attention scoring** (Bahdanau or Luong). You will also evaluate your model using standard translation metrics (like BLEU score) and analyze its qualitative performance through example translations.

### Dataset

**Dataset Link:** [eng-deu.csv](https://github.com/skarma91/logicmojo-data-science-april-2025/blob/main/Assignments/Assignment-13-Natural_Language_Processing/eng-deu.csv)

Download the dataset in your local machine.

**Description:**  
This dataset contains pairs of English and German sentences.  
Each row represents a translation pair in the following format:

```
english_sentence, german_sentence
```

**Example:**
```
Go. , Geh.
Hello. , Hallo.
I am hungry. , Ich bin hungrig.
```

The dataset can be used to train a machine translation model where the **input** is an German sentence and the **target output** is its corresponding English translation.


### Objective

The main objectives of this assignment are:
1. Implement a **Seq2Seq neural network** with **attention mechanism** for language translation.
2. Understand and visualize how the **attention mechanism** helps the model focus on relevant words during translation.
3. Evaluate translation quality using **BLEU score** and qualitative comparison.
4. Compare the effects of using different attention types.


### Skills Practiced

By completing this assignment, you will develop the following practical skills:
- Implementing **encoder-decoder architectures** for sequence modeling.
- Applying **attention mechanisms** (Bahdanau or Luong) in NLP tasks.
- Preprocessing bilingual text data for neural network training.
- Handling **padding**, **tokenization**, and **sequence batching**.
- Evaluating translation models using **BLEU score** and other metrics.
- Visualizing **attention weights** to interpret model decisions.

---

## Deliverables

Your submission should include the following two deliverables:

### 1. Code Notebook
A comprehensive and well-documented Jupyter Notebook (`.ipynb`) that includes:
- Proper code comments and modular structure.
- Data preprocessing, tokenization, and sequence preparation.
- Encoder-decoder model implementation with attention.
- Training loop with loss tracking and validation.
- Visualization of attention weights for sample translations.
- Evaluation results with BLEU scores and example outputs.

**Expected file name:**  
`Assignment-13_Seq2Seq_Attention_<your_name>_<your_surname>.ipynb`

**Reference Notebook**

To guide your implementation, you may refer to the following example notebook:
[French to English using Seq2Seq with Attention](https://github.com/skarma91/logicmojo-data-science-april-2025/blob/main/Lecture_materials/Class-53-19-10-2025-Seq2Seq-Attention-Transformer/french_to_english_using_seq2seq_attention.ipynb)

This reference provides a similar workflow using a different language pair. You are encouraged to understand its structure and adapt the logic for German-to-English translation.

### 2. Project Report (2–4 pages)
A concise and well-structured report that summarizes:
- The approach you followed.
- Details about the architecture (encoder, decoder, attention type).
- Preprocessing and hyperparameter choices.
- Evaluation metrics and model performance.
- Insights from attention visualizations.
- Observations, challenges, and possible improvements.

**Expected file name:**  
`Assignment-13_Seq2Seq_Attention_Report_<your_name>_<your_surname>.pdf`

---

## Suggested Milestones

To help you organize your work efficiently, follow the suggested milestones below.

### Milestone 1: Problem Setup
- Load and explore the dataset.
- Examine a few English–German sentence pairs.
- Split the data into **training**, **validation**, and **test** sets.
- Define parameters such as:
  - Maximum sentence length.
  - Vocabulary size.
  - Special tokens (`<PAD>`, `<SOS>`, `<EOS>`).
- Decide on the framework (PyTorch or TensorFlow) for implementation.

### Milestone 2: Preprocessing
- Perform text **cleaning**:
  - Lowercasing, removing punctuation, and trimming spaces.
- Perform **tokenization** for both English and German text.
- Build **word-to-index** and **index-to-word** mappings for each language.
- Convert sentences into padded integer sequences.
- Create batches and **DataLoader** (or similar) for training.
- Verify your preprocessing by printing a few tokenized examples.

### Milestone 3: Implement the Seq2Seq Network
Your model should follow the **Encoder–Decoder with Attention** architecture:

**Encoder:**
- Use an **Embedding layer** to represent input words.
- Use an **RNN (LSTM or GRU)** to encode the input sequence.
- Return hidden states for attention computation.

**Attention Mechanism:**
- Implement **Bahdanau (Additive)** or **Luong (Dot/General)** attention.
- Calculate attention weights over encoder outputs.
- Compute the context vector for each decoder step.

**Decoder:**
- Use an **Embedding layer** for target sequences.
- Combine context vector and decoder hidden state.
- Predict next word using a **linear layer** over vocabulary.
- Implement **teacher forcing** for training.

**Training:**
- Define a suitable **loss function** (e.g., CrossEntropyLoss).
- Use an optimizer (e.g., Adam).
- Train for multiple epochs, monitoring training and validation loss.

### Milestone 4: Evaluation and Communication
- Evaluate model on the **test set** using:
  - **BLEU score** for quantitative evaluation.
  - **Example translations** for qualitative analysis.
- Visualize **attention maps** for a few translated sentences to show which input words the model focused on.
- Compare predictions with reference translations.
- Discuss:
  - How well the model learned alignment.
  - Which attention mechanism (if multiple) performed better.
  - Potential improvements or limitations observed.

### Tips
- Start with a smaller subset of the dataset to ensure the model trains correctly.
- Monitor loss closely — exploding gradients can occur with RNNs.
- Save intermediate model checkpoints.
- Visualize and interpret attention weights to explain model behavior.
- Optionally, experiment with bidirectional encoders or different attention types for deeper understanding.

---

## Steps to upload the assignment solution

- Upload the solved notebook (`Assignment-13_Seq2Seq_Attention_<your_name>_<your_surname>.ipynb`) and report document (`Assignment-13_Seq2Seq_Attention_Report_<your_name>_<your_surname>.pdf`) in the google drive location: https://drive.google.com/drive/folders/13-cQPCFMu2vLw20cpB65PqhcdPOF-OHF?usp=drive_link

- Also upload the solved notebook and document to your respective github repository.
