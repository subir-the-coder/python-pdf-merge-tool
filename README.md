# PDF Merger – Python CLI Tool
---

## 📘 Overview

**PDF Merger** is a command-line utility written in Python to automatically merge all PDF files inside a folder.
It supports sorting, animation, and a custom banner design.

---

## ✨ Features

- Merge multiple PDFs into one file
- Sort by filename (ascending / descending)
- Banner + colorized terminal output
- Continuous merge animation
- Custom output filename
- Error handling
- No GUI required

---

## 🖥️ Screenshot!
![merge_banner](https://github.com/user-attachments/assets/06f2a231-b2b8-4193-bfa5-01b9f2b4c73c)


---

## 🛠️ Tech Stack

| Component | Technology |
|----------|------------|
| Language | Python 3.x |
| PDF Engine | PyPDF2 |
| Terminal Colors | colorama |

---

## 📁 Project Structure
```
pdf-merge-tool/
│
├── merge.py
├── README.md
├── requirements.txt
├── input_pdfs/
├── output/
```

---

## 📦 Installation

### Clone Repository
```
git clone https://github.com/subir-the-coder/pdf-merge-tool.git
cd pdf-merge-tool
```

### Create Virtual Environment

python3 -m venv venv
source venv/bin/activate

### Install Dependencies

pip install -r requirements.txt

---

## ▶️ Usage

Place PDFs into input_pdfs folder and run:

python3 merge.py

Program will ask:

Sorting order? asc / desc
Output filename?

Output example:
merged_output.pdf

---

## Requirements

PyPDF2==3.0.1
colorama==0.4.6

---

## 🧑‍💻 Author

**Subir Sutradhar**

---

## ⭐ How to Support

If this project helped you:

- Star the repo ⭐

---

## License

This project is licensed under the MIT License.
You are free to use and modify the project.

Report for any bugs: subirthecoder35@gmail.com
