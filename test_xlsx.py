from openpyxl import load_workbook
import os
from conftest import JOINED_PATH
# TODO оформить в тест, добавить ассерты и использовать универсальный путь

workbook = load_workbook('resources/file_example_XLSX_50.xlsx')
sheet = workbook.active
print(sheet.cell(row=3, column=2).value)
