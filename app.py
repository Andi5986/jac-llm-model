import streamlit as st
from htmlTemplates import css
from dotenv import load_dotenv
from utils import get_docx_text, get_pdf_text, get_text_chunks, get_vectorstore, get_conversation_chain, handle_userinput

def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple PDFs",
                       page_icon="https://i.postimg.cc/CKgGWWwM/Screenshot-2023-08-06-at-21-35-45.png")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.markdown('<img src="https://i.postimg.cc/CKgGWWwM/Screenshot-2023-08-06-at-21-35-45.png" width="150">', unsafe_allow_html=True)
    if user_question := st.text_input("Ask a question about your documents:"):
        handle_userinput(user_question)

    with st.sidebar:
        st.subheader("Your documents")
        uploaded_files = st.file_uploader(
            "Upload your PDFs and Word files here and click on 'Process'", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                # Extract raw text from uploaded files
                raw_text = ""
                for uploaded_file in uploaded_files:
                    if uploaded_file.name.endswith('.pdf'):
                        raw_text += get_pdf_text([uploaded_file])
                    elif uploaded_file.name.endswith('.docx'):
                        raw_text += get_docx_text([uploaded_file])

                # Get the text chunks
                text_chunks = get_text_chunks(raw_text)

                # Create vector store
                vectorstore = get_vectorstore(text_chunks)

                # Create conversation chain
                st.session_state.conversation = get_conversation_chain(vectorstore)

if __name__ == '__main__':
    main()