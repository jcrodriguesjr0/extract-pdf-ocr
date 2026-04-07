import os
import glob
from pdf2image import convert_from_path
import pytesseract

def extract_text_from_pdfs(folder_path, output_file):
    """
    Extracts text from all PDF files in the specified folder using OCR (Tesseract),
    and saves the extracted text into the specified output file.
    """
    pdfs = sorted(glob.glob(os.path.join(folder_path, "*.pdf")))
    
    # Ensure Tesseract can find the Portuguese language pack, 
    # pytesseract uses 'por' for Portuguese.
    
    with open(output_file, "w", encoding="utf-8") as f:
        if not pdfs:
            f.write("No PDF files found in the target directory.\n")
            print("No PDF files found.")
            return

        for pdf_file in pdfs:
            print(f"Processing file: {os.path.basename(pdf_file)}")
            f.write(f"==== {os.path.basename(pdf_file)} ====\n")
            try:
                # Convert PDF pages to images
                # Note: Might require poppler-utils installed on the system
                images = convert_from_path(pdf_file)
                
                for i, img in enumerate(images):
                    print(f"  -> Running OCR on page {i + 1}")
                    # Extract text from image
                    text = pytesseract.image_to_string(img, lang="por")
                    f.write(f"--- Page {i+1} ---\n{text}\n")
                    
            except Exception as e:
                error_msg = f"Error processing {os.path.basename(pdf_file)}: {e}"
                print(error_msg)
                f.write(f"Error: {e}\n")
                
    print(f"Finished. Output saved to: {output_file}")

if __name__ == "__main__":
    # Usage Example
    target_folder = "."  # Current Directory
    output_path = "ocr_results.txt"
    extract_text_from_pdfs(target_folder, output_path)
