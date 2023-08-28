import  zipfile, os
from conftest import JOINED_PATH

def test_zip():
    with zipfile.ZipFile(os.path.join(JOINED_PATH, 'resources.zip')) as zf:
        result = []
        for file in zf.namelist():
            result.append(file)
    print(result)
    assert result == ['file_example_XLSX_50.xlsx', 'docs-pytest-org-en-latest.pdf', 'file_example_XLS_10.xls']


    # zip_f = zipfile.ZipFile(os.path.join(JOINED_PATH, 'resources.zip'))
    # zip_f.extractall(os.path.join(JOINED_PATH, 'from_archive'))
    # dir_from_zip = os.path.join(JOINED_PATH, 'from_archive')
    # folder = pathlib.Path(dir_from_zip)
    # for file in folder.iterdir():
    #     print(file.name)

