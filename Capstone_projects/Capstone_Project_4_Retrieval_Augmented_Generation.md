# Capstone Project-4: Retrieval Augmented Generation (RAG) for Corporate Environmental Reports
---

## Problem Statement

Large corporations publish detailed sustainability and environmental reports annually. These documents contain valuable insights about their environmental goals, pollution control measures, carbon footprint, waste management, and sustainability progress. However, these reports are typically long (50–150 pages each), making it difficult for analysts, policymakers, or researchers to quickly retrieve relevant information and derive meaningful insights.

The objective of this capstone project is to **build a Retrieval Augmented Generation (RAG) system** that allows users to ask questions over these corporate sustainability and environmental reports (PDFs). The model should retrieve the most relevant context from the documents and generate accurate, concise, and contextually grounded answers.

---

## Dataset Description

The dataset consists of publicly available corporate environmental and sustainability reports (mostly in PDF format) from well-known global organizations. These documents will be parsed and indexed for retrieval-based question answering.

| Company                  | Report Title                                              | Report Year | Direct Link                                                                                                                                                       |
|--------------------------|-----------------------------------------------------------|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Apple                    | Environmental Progress Report                             | 2024        | [Apple 2024 Environmental Progress Report](https://www.apple.com/environment/pdf/Apple_Environmental_Progress_Report_2024.pdf)                                    |
| Unilever                 | Annual Report and Accounts (includes ESG/Sustainability)  | 2024        | [Unilever Annual Report and Accounts 2024 (PDF)](https://www.unilever.com/files/unilever-annual-report-and-accounts-2024.pdf)                                     |
| Google                   | Environmental Report                                      | 2024        | [Google 2024 Environmental Report](https://sustainability.google/reports/google-2024-environmental-report/)                                                       |
| Microsoft                | Sustainability Reports Hub (links to recent data/updates) | 2024/2025   | [Microsoft CSR Reports Hub](https://www.microsoft.com/en-us/corporate-responsibility/reports-hub)                                                                 |
| The Coca-Cola Company    | 2024 Environmental Update                                 | 2024        | [Coca-Cola 2024 Environmental Update](https://www.coca-colacompany.com/content/dam/company/us/en/reports/2024-environmental-update/2024-environmental-update.pdf) |
| HSBC                     | Net Zero Transition Plan                                  | 2024        | [HSBC Net Zero Transition Plan 2024 (PDF)](https://www.hsbc.com/content/dam/gbm/attachments/esg-reporting/HSBC_NZTP_2024.pdf)                                     |
| IKEA (Ingka Group)       | Annual Sustainability Report FY24                         | 2024        | [Ingka Group Annual Sustainability Report FY24](https://ingka.com/reports-publications/annual-sustainability-report/)                                             |
| Alphabet (Google Parent) | Alphabet 2024 CDP Climate Change Response                 | 2024        | [Alphabet 2024 CDP Climate Change Response](https://sustainability.google/reports/alphabet-cdp-2024-climate-change-response/)                                     |
| General Motors (GM)      | Corporate Sustainability Report                           | 2024        | [GM 2024 Corporate Sustainability Report](https://www.gmsustainability.com/)                                                                                      |
| Verizon                  | ESG Report                                                | 2024        | [Verizon 2024 ESG Report](https://www.verizon.com/about/responsibility/esg-report)                                                                                |

---

## Objectives

1. To design and implement a **Retrieval Augmented Generation (RAG)** pipeline that can answer user queries using corporate sustainability reports as knowledge sources.  
2. To parse and preprocess multiple PDF reports using tools like **Docling**, **PyMuPDF** etc.  
3. To create vector embeddings for document chunks using modern embedding models (e.g., `BAAI/bge-base-en-v1.5`, `Qwen/Qwen3-Embedding-0.6B`, etc.).  
4. To store embeddings in a vector database (e.g., FAISS).  
5. To build a retrieval system that fetches the most relevant text chunks based on user queries.  
6. To integrate the retriever with a large language model (LLM).  
7. To qualitatively evaluate the accuracy, relevance, and coherence of generated answers.  

---

## Steps to Follow

### Step 1: Data Acquisition
- Download all the PDF documents from the links provided above.  
- Store them in a local `data/` directory.

### Step 2: Document Parsing
- Use **Docling** (or any PDF parser like `PyMuPDF`) to extract clean text from each document.  
- Perform text cleaning to remove extra spaces, page numbers, headers, and footers.  
- Store the extracted content in a structured format such as JSON or CSV.

### Step 3: Text Chunking
- Split each document into manageable chunks (e.g., 500–1000 tokens per chunk).  
- Assign metadata to each chunk, including the company name, section title, and page number.

### Step 4: Embedding Generation
- Generate vector embeddings for each chunk using pre-trained models such as:
  - `BAAI/bge-base-en-v1.5` (BAAI)
  - `Qwen/Qwen3-Embedding-0.6B`(Alibaba)
  - `text-embedding-3-large` (OpenAI)
  - `all-MiniLM-L6-v2` (Sentence Transformers)
- Save embeddings along with metadata in a vector database (e.g., FAISS, Chroma).

### Step 5: Retrieval System
- Implement a retriever that returns the most relevant chunks for a given query.  
- Test it by asking sample questions such as:
  - “What are Apple’s goals for carbon neutrality?”
  - “How does Unilever manage plastic waste?”
  - “What steps has Coca-Cola taken to reduce water usage?”

### Step 6: Generation Model Integration
- Combine the retriever with a generative model using the **RAG architecture**.  
- Use LangChain or LlamaIndex to integrate the retriever and generator.  
- Ensure that the model’s output is grounded in the retrieved context.

### Step 7: Evaluation
- Qualitatively evaluate the model’s answers using:
  - **Relevance** (is the answer contextually correct?)
  - **Faithfulness** (is it supported by the retrieved text?)
  - **Conciseness** (is it well summarized?)

### Step 8: Deployment (Optional)
- Build a simple Streamlit interface to allow users to query the system interactively.  
- The interface should display:
  - The user’s question  
  - The generated answer  
  - The supporting document excerpts  

---

## **Deliverables**

1. **Jupyter Notebook (.ipynb):**  
   Complete notebook with data loading, preprocessing, model training, and evaluation steps.

2. **Presentation Slides:** not more than 10 slides summarizing key methodology, results, and insights.

3. **Optional Deployment:**  
   - Create a small web app using Streamlit to facilitate interactive queries by user.  
   - The interface should display:
    - The user’s question  
    - The generated answer  
    - The supporting document excerpts 

---


## **Upload the project deliverables**

- Upload the solved notebook(s), Presentation Slides in the google drive location: https://drive.google.com/drive/folders/1aAO1MdxCgk2C--FZuqnquGlsEGx9HPUs?usp=drive_link

- Also upload the solved notebook and the documents to your respective github repository.
