# Assignment 14: Retrieval-Augmented Generation (RAG)

## Project Overview

### Dataset
The dataset for this project is the PDF report **“The State of AI: How organizations are rewiring to capture value (2025)”** by McKinsey & Company.  
Students will parse this document, extract structured content (sections, sub-sections, and text), embed the extracted chunks, and build a retrieval system that can answer user queries using a Retrieval-Augmented Generation (RAG) approach.

**Document Link:**  
[The State of AI (2025) by McKinsey](https://www.mckinsey.com/~/media/mckinsey/business%20functions/quantumblack/our%20insights/the%20state%20of%20ai/2025/the-state-of-ai-how-organizations-are-rewiring-to-capture-value_final.pdf)

I have provided the pdf report for ready reference. 


### Objective
- Parse the PDF using **Docling** (or an equivalent library) to convert the document into a LLM friendly format (like markdown).
- Chunk the text into meaningful units suitable for retrieval (e.g., fixed-length text chunks or section-based chunks).
- Generate **embeddings** for the chunks using any suitable embedding model.
- Build a **retriever** using a vector database such as **FAISS** or **ChromaDB**.
- Create a **RAG pipeline** that retrieves the most relevant chunks for a query and passes them to a language model to generate an answer.
- Evaluate the system by testing a set of user queries and analyzing the relevance of retrieved content and generated answers.


### Skills Practiced
- PDF parsing and document preprocessing  
- Text chunking and metadata tagging  
- Embedding generation and vector-based retrieval  
- Building and querying a RAG pipeline  
- Prompt design for LLMs  
- Evaluation of retrieval and generation quality  

---

## Deliverables
Students must submit a **Jupyter Notebook (.ipynb)** file that includes the following:

1. **PDF Loading and Parsing**
   - Load and parse the McKinsey report using `docling` or any equivalent tool.
   - Display document structure (sections, page numbers, headings).
   - Show a small sample of extracted text.

2. **Chunk Creation**
   - Define and implement a chunking strategy.
   - Store chunk metadata (section, page, text, etc.).
   - Display examples of text chunks and their metadata.

3. **Embedding Generation**
   - Generate embeddings for all chunks using an embedding model of your choice (e.g., OpenAIEmbeddings, HuggingFaceEmbeddings).
   - Build an embedding index using FAISS or ChromaDB.

4. **Retriever Construction**
   - Implement a retriever to fetch top-k relevant chunks for a given query.
   - Display retrieved chunks for sample queries.

5. **RAG Pipeline**
   - Integrate a language model (e.g., OpenAI GPT or open-source model) to form a retrieval-augmented generation pipeline.
   - Take user queries, retrieve relevant chunks, and generate context-aware answers.

6. **Evaluation**
   - Test the system on at least five diverse queries.
   - For each query, display:
     - Generated answer
     - Brief evaluation of relevance and accuracy

7. **Documentation and Code Readability**
   - Include markdown explanations for each code section.
   - Ensure the notebook can be executed top-to-bottom without errors.
   - List all dependencies and setup steps at the top of the notebook.

**Expected file name:**  
`Assignment-14_RAG_<your_name>_<your_surname>.ipynb`

---

### Steps to upload the assignment solution

- Upload the solved notebook (`Assignment-14_RAG_<your_name>_<your_surname>.ipynb`) in the google drive location: https://drive.google.com/drive/folders/1miVUE1dQelo40YI4qIGZXSipwSXKNKYz?usp=drive_link

- Also upload the solved notebook and document to your respective github repository.
