# avocat-ai
This app analyzez contracts and paperwork for inconsistencies and potential risks. Below is a template that will be refined after choosing the tech stack and implementing features.

## LLM
I am thinking of using a general-purpose language model in the beginning and switch later to a fine-tuned model on legal documents.

Options include:
- general-purpose models:
    - GPT4 (from the openai API)
- pre-trained language models for Romanian
    - RomanianBERT
    - BERTur
- fine-tuned legal model for Romanian:
    - LegalBERT fine-tuned on Romanian legal documents

## Pipeline
### Text extraction
- parse PDFs with libraries like `PyMuPDF`, `pdfplumber` or `Apache PDFBox`.
- implement OCR with `Tesseract` configured for Romanian.

### Text preprocessing
- use Romanian-specific NLP tools for tokenization, lemmatization and named entity recognition. `SpaCy` has language models that can assist in processing Romanian text.
- Tokenize the document into sections, sentences or clauses for better processing.
- legal term recognition: develop a specialized entity recognition model for Romanian legal terms, such as recognizing key parties, contract types, dates, obligations, and penalties.

### Document understanding
- clause identification: using Romanian legal terms, develop a pipeline to identify important clauses like:
    1. clauze de răspundere
    2. clauze de confidențialitate
    3. clauze de penalități
    4. clauze de reziliere
- risk detection: use a combination of fine-tuned legal-models and rule-based techniques to:
    1. detect **ambiguous language** commonly found in Romanian contracts
    2. spot **risky clauses**, **missing clauses** or terms unfavorable to the contract's signatory (e.g. one-sided penalty clauses or unreasonable indemnity terms)
    3. check for **inconsistencies** like contradictory clauses (e.g. differing terms for payment deadlines in different sections)
    4. legal loopholes
    5. potential non-compliance with local regulations or industry standards

## User interface
Main features:
- support Romanian text input and display. Ensure all interface elements (including form fields, error messages, instructions, and results) are in Romanian.
- upload Romanian-language PDFs and see results presented in Romanian.
- return a summary of key contract terms
- view flagged risks, inconsistencies and potentially shady clauses in an intuitive manner
- visually highlight clauses within the document that have been flagged as potentially problematic or inconsistent.
- the flagged issues should be described in Romanian, explaining why a clause was flagged (e.g., "Clauză de răspundere unilaterală – favorizează doar una dintre părți").

### Consider Romanian Legal Framework and Compliance

To make the app useful for Romanian users, ensure that the checks you implement are aligned with Romanian laws and regulations. Key considerations include:

- **Romanian Civil Code:** Contracts must comply with the rules defined by the Romanian Civil Code. The model should check for compliance with these rules (e.g., fairness in penalty clauses, clarity of terms).
- **Specific Laws for Certain Types of Contracts:** Contracts like employment agreements, leases, and sales contracts have specific legal frameworks that your model should consider.
- **EU Regulations:** If the contracts involve cross-border transactions or EU law applicability, ensure that the model checks for compliance with relevant EU regulations (e.g., GDPR for privacy clauses).

## Technology stack
- frontend: react, angular or vue.js for user interaction
- backend: python-based frameworks like flask, django, fastapi
- database: store documents and results in a database like PostgreSQL or MongoDB, which will help with structured storage and fast retrieval.
- hosting and deployment: Docker, GCP

## Additional features
- clause comparison: offer comparisons with Romanian contract templates and flag any deviation from standard practices.
- risk scoring: develop a risk-scoring system where the app gives an overall risk rating based on the flagged inconsistencies (e.g., low vs. high risk based on common pitfalls in Romanian contracts).
- legal term glossary: provide explanations for legal terms in Romanian to help non-experts understand the flagged issues.
- collaborative review: allow users to comment and make notes on flagged clauses for easier team collaboration

### **Training a Romanian Legal Model**

#### a. **Collecting Romanian Legal Data:**
   - You will need a dataset of Romanian legal documents for fine-tuning. Some potential sources include:
     - **Public Romanian government websites** that host contracts and procurement documents.
     - **Legal databases** containing Romanian court decisions and contracts.
     - **Romanian legal textbooks**, guides, or open legal databases.

#### b. **Data Preprocessing:**
   - Clean and preprocess these documents to remove irrelevant sections, normalize the text, and structure it for training. Ensure that the legal nuances of Romanian law are well-represented in the training data.

#### c. **Fine-tuning Process:**
   - Use frameworks like **Hugging Face Transformers** to fine-tune a pre-trained model (such as RoBERT) on your Romanian legal dataset.
   - Focus the fine-tuning on identifying clause types, checking compliance with Romanian laws, and spotting potentially shady terms.
