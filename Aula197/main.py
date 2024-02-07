# PyPDF2 - Para manipular arquivos PDF
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados e muito mais.
# A documentação contém todas as informações necessárias para usar o PyPDF2.
# https://pypdf2.readthedocs.io/en/latest/
# pip install pypdf2
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

ROOT_FOLDER = Path(__file__).parent
ORIGINAL_FOLDER = ROOT_FOLDER / 'original_pdfs'
NEW_FOLDER = ROOT_FOLDER / 'new_files'

# Relatório do Banco Central na data de 10/02/2023
REPORT_BACEN = ORIGINAL_FOLDER / 'R20230210.pdf'

NEW_FOLDER.mkdir(exist_ok=True)

reader = PdfReader(REPORT_BACEN)

# print(len(reader.pages))
# for page in reader.pages:
#     print(page)
#     print()

page0 = reader.pages[0]
img0 = page0.images[0]

# print(page0.extract_text())
# with open(NEW_FOLDER / img0.name, 'wb') as fp:
#     fp.write(img0.data)
