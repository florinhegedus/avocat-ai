# avocat-ai
This app analyzez contracts and paperwork for inconsistencies and potential risks. Below is a template that will be refined after choosing the tech stack and implementing features.

## LLM
I am thinking of using a general-purpose language model in the beginning and switch later to a fine-tuned model on legal documents.

Options include:
- GPT4 (from the openai API)
- LegalBERT
- RomanianBERT
- BERTur

## Pipeline
### PDF ingestion and preprocessing
Make use of libraries like `PyMuPDF`, `pdfplumber` or `Apache PDFBox` to extract text from PDFs.
Apply OCR for scanned documents using libraries like `Tesseract` if PDF is image-based.

### Text preprocessing
Tokenize the document into sections, sentences or clauses for better processing.
Apply lemmatization, POS tagging and named entity recognition (NER) to extract important information like party names, dates and key contractual terms.

### Document understanding
The app makes use of an LLM or a legal-specific model to:
- identify **key clauses** (e.g. liability clauses, indemnity clauses, payment terms)
- check for **missing clauses** or unusually phrased terms that could be legally risky
- spot **ambigous language** or terms that are commonly associated with legal disputes
- compare clauses with known templates to find deviations

### Risk detection and inconsistency checks
Use a combination of **rule-based methods** (e.g. regex) and **AI models** to flag:
- inconsistent terms (e.g. payment timelines differing in various parts of the contract)
- legal loopholes or ambigous clauses
- shady clauses (e.g. one-sided indemnity clauses, extremely high penalties)
- potential non-compliance with local regulations or industry standards

## User interface
The users should be able to:
- upload a PDF document
- receive a summary of key contract terms
- view flagged risks, inconsistencies and potentially shady clauses in an intuitive manner
- implement visual highlights on the document itself, allowing users to see which parts of the contract have been flagged

## Technology stack
- frontend: react, angular or vue.js for user interaction
- backend: python-based frameworks like flask, django, fastapi
- document analysis & NLP: hugging face transformers, spacy or NLTK for NLP tasks
- text extraction from PDFs: PyMuPDF, Tika, pdfplumber or pdfminer for extracting text from PDFs
- hosting and deployment: GCP

## Additional features
- clause comparison: compare uploaded contracts with pre-defined templates to flag deviations
- risk scoring: develop a risk-scoring system where the app gives an overall risk rating based on the flagged inconsistencies
- collaborative review: allow users to comment and make notes on flagged clauses for easier team collaboration

## Training data for fine-tuning
- use public contract daatabases
- extract legal knowledge from open legal texts, judgments or legal encyclopedias
- levarge synthetic data generation by creating variations of contracts to fine-tune the model