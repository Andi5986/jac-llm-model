# Chat with Text from PDFs and Word Documents

This example illustrates how to build an app to chat with your text from multiple PDFs and Word documents. Importantly, the chat uses OpenAI for generating responses.

## Dependencies

This project uses the following libraries:

- **streamlit** for generating a user-friendly app interface.
- **PyPDF2** to extract text from uploaded PDF files.
- **docx** to extract text from uploaded Word (.docx) documents.
- **langchain** for splitting the uploaded text into smaller pieces, generating embeddings, and building chat models, amongst other functionalities.
- **dotenv** to load environment variables.

### Key Functions Explanation

```python
get_docx_text(docx_files): # This function takes in a list of .docx files loaded into the browser and reads the text from each file, appending it to a text string which is returned.
get_pdf_text(pdf_docs): # This functions accepts a list of PDF files loaded into the browser and using PyPDF2, retrieves the text from each page of the documents and appends it to a text string which is then returned.
get_documents_text(files): # This function uses the two previous functions to fetch texts from the provided PDF and Word files.
get_text_chunks(text): # This function splits the raw text into smaller text chunks suitable for conversational models.
get_vectorstore(text_chunks): # This function generates embeddings from the text chunks.
get_conversation_chain(vectorstore): # This function forms the conversational chain which will be used when communicating with the user.
```

## Usage Instructions
Run the app and use the sidebar to upload your PDFs and Word (.docx) documents. Once your files are uploaded, click 'process'. The app will then display a text box for you to ask questions related to your documents.

The bot responds to your queries in the style of a chat, with new messages being added to an ever-growing conversation, allowing lookback and context to the messages.

### Installation and Running the App

Clone the repository from GitHub:

```bash
git clone https://github.com/Andi5986/jac-llm-model.git
```

Install the required libraries:
Make sure you have pip installed, then run:

```bash
pip install -r requirements.txt
```

Get your OPENAI API KEY from https://platform.openai.com/account/api-keys and create `.env` environment

```bash
OPENAI_API_KEY=YOUR_API_KEY
```

Run the app:

```bash
streamlit run app.py
```