import xlrd, os

from conftest import JOINED_PATH
# TODO оформить в тест, добавить ассерты и использовать универсальный путь

def test_xls():
    book = xlrd.open_workbook(os.path.join(JOINED_PATH, 'file_example_XLS_10.xls'))
    print(f'Количество листов {book.nsheets}')
    print(f'Количество листов {book.nsheets}')
    print(f'Имена листов {book.sheet_names()}')
    sheet = book.sheet_by_index(0)
    print(f'Количество колонок  {sheet.ncols}')
    print(f'Количество строк    {sheet.nrows}')
    print(f'Пересечение строки и столбца {sheet.cell_value(rowx=3, colx=2)}')
    result = []
    for rx in range(sheet.nrows):
        result.append(sheet.row(rx))
        print(result)
    assert book.nsheets == 1
    assert book.sheet_names() == ['Sheet1']
    assert sheet.ncols == 8
    assert sheet.cell_value(rowx=3, colx=2) == 'Gent'
    assert  len(result) == 10