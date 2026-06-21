import streamlit as st
import fitz  # PyMuPDF
from docx import Document

def pdf_to_word(pdf_file):
    # Open PDF
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    word_doc = Document()

    # Extract text page by page
    for page in doc:
        text = page.get_text()
        word_doc.add_paragraph(text)

    return word_doc

st.title("📄 PDF to Word Converter")

uploaded_file = st.file_uploader("Upload PDF file", type=["pdf"])

if uploaded_file is not None:
    st.write("Uploaded File:", uploaded_file.name)

    # Convert PDF to Word
    word_doc = pdf_to_word(uploaded_file)

    # Save to buffer
    from io import BytesIO
    buffer = BytesIO()
    word_doc.save(buffer)
    buffer.seek(0)

    # Download button
    st.download_button(
        label="⬇️ Download Word File",
        data=buffer,
        file_name=uploaded_file.name.replace(".pdf", ".docx"),
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
