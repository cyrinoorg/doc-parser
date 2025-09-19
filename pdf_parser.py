import PyPDF2

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
if __name__ == "__main__":
    pdf_path = "example.pdf"  # Replace with your PDF file path
    extracted_text = extract_text_from_pdf(pdf_path)
    print(extracted_text)