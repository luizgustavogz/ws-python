# PyPDF2 - Para manipular arquivos PDF
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados e muito mais.
# A documentação contém todas as informações necessárias para usar o PyPDF2.
# https://pypdf2.readthedocs.io/en/latest/
# pip install pypdf2
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

ROOT_FOLDER = Path(__file__).parent
ORIGINAL_FOLDER = ROOT_FOLDER / 'original_pdfs'
NEW_FOLDER = ROOT_FOLDER / 'new_files'

# Relatório do Banco Central na data de 10/02/2023
REPORT_BACEN = ORIGINAL_FOLDER / 'R20230210.pdf'

NEW_FOLDER.mkdir(exist_ok=True)

# 1. Ler o arquivo PDF
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


# 2. Escrever um novo arquivo PDF
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(NEW_FOLDER / f'page{i}.pdf', 'wb') as file:
        writer.add_page(page)
        writer.write(file)


# 3. Unir arquivos PDF
files = [
    NEW_FOLDER / 'page1.pdf',
    NEW_FOLDER / 'page0.pdf',
]

merger = PdfMerger()
for file in files:
    merger.append(file)

merger.write(NEW_FOLDER / 'merged.pdf')
merger.close()
