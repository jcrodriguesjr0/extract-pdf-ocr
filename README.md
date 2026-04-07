# Extract PDF OCR 📄🔍

[🇺🇸 English](#english) | [🇧🇷 Português](#português)

---

<a name="english"></a>
## 🇺🇸 English Version

A simple Python script to perform batch Optical Character Recognition (OCR) text extraction from PDF files. Ideal for non-selectable PDFs like scanned documents or image-based files.

### 🚀 Features

- **Batch Processing:** Reads all `.pdf` files inside a target directory.
- Convers each page into an image using `pdf2image`.
- Extracts the text using `pytesseract` (configured for Portuguese `por` by default, but customizable).
- Generates a consolidated output text file indicating exactly which document and page the text belongs to.

### 🛠️ Prerequisites

You will need Python and several system dependencies (like Tesseract and Poppler tools).

#### System Dependencies (Linux / Ubuntu)
```bash
# Install Tesseract OCR and (optional) Portuguese pack
sudo apt-get install tesseract-ocr tesseract-ocr-por

# Install Poppler utils (Required by pdf2image)
sudo apt-get install poppler-utils
```

#### Python Libraries
Install the python requirements using `pip`:
```bash
pip install -r requirements.txt
```

### 💻 Usage

1. Place your `.pdf` files in the same directory or a target sub-directory.
2. Open `extract_pdf_ocr.py` and change the bottom variables if necessary:
    ```python
    target_folder = "."  
    output_path = "ocr_results.txt" 
    ```
3. Run the script:
    ```bash
    python extract_pdf_ocr.py
    ```
4. The terminal will log the processing of each page. The final `.txt` file will be generated in your folder.

### 📄 License
This project is open-source under the [MIT](https://opensource.org/licenses/MIT) license.

---

<a name="português"></a>
## 🇧🇷 Versão em Português

Um script simples em Python para extrair texto de arquivos PDF em lote utilizando Optical Character Recognition (OCR). Ideal para arquivos não selecionáveis, como PDFs compostos de imagens ou documentos escaneados.

### 🚀 Funcionalidades

- Processamento em lote: Lê todos os arquivos `.pdf` em um diretório específico.
- Converte cada página do PDF em uma imagem usando `pdf2image`.
- Extrai o texto das imagens utilizando o `pytesseract` configurado para português (`por`).
- Gera um arquivo de saída consolidado com todo o texto extraído e indica a qual arquivo e página ele pertence.

### 🛠️ Pré-requisitos

Para utilizar este script, você precisará do Python instalado e de algumas dependências de sistema (além das bibliotecas Python), como o Tesseract OCR e as ferramentas do Poppler.

#### Dependências do Sistema (Linux / Ubuntu)
```bash
# Instalar o Tesseract OCR e o pacote de idioma Português
sudo apt-get install tesseract-ocr tesseract-ocr-por

# Instalar o Poppler utils (necessário para o pdf2image)
sudo apt-get install poppler-utils
```

#### Bibliotecas Python

Instale as dependências usando o `pip`:

```bash
pip install -r requirements.txt
```

### 💻 Como usar

1.  Coloque todos os seus arquivos `.pdf` no mesmo diretório ou em um subdiretório acessível.
2.  No final do arquivo `extract_pdf_ocr.py`, altere as variáveis `target_folder` e `output_path` se necessário:
    ```python
    target_folder = "."  # Pasta contendo os PDFs
    output_path = "resultado_ocr.txt" # Onde o resultado será salvo
    ```
3.  Execute o script:
    ```bash
    python extract_pdf_ocr.py
    ```
4.  Aguarde o processamento de cada imagem. O terminal exibirá o log mostrando qual página e de qual arquivo o texto está sendo extraído no momento.
5.  Ao finalizar, o arquivo `resultado_ocr.txt` (ou o nome que você definiu) estará disponível.

### 📄 Licença

Este projeto é de código aberto e está disponível sob a licença [MIT](https://opensource.org/licenses/MIT).
