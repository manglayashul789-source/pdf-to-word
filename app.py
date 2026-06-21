import streamlit as st
from pdf2docx import Converter

st.title("📄 PDF to Word Converter")

# Upload PDF file
upload_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if upload_file is not None:
    st.write("Uploaded File:", upload_file.name)

    # Temporary save uploaded file
    with open("temp.pdf", "wb") as f:
        f.write(upload_file.read())

    # Convert PDF to Word
    output_file = "converted.docx"
    cv = Converter("temp.pdf")
    cv.convert(output_file, start=0, end=None)
    cv.close()

    st.success("✅ Conversion complete!")

    # Provide download button
    with open(output_file, "rb") as f:
        st.download_button(
            label="⬇️ Download Word File",
            data=f,
            file_name="converted.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
