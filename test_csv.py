import csv, os

from conftest import RESOURCES_DIR_PATH
# TODO оформить в тест, добавить ассерты и использовать универсальный путь

def test_csv():
    with open(os.path.join(RESOURCES_DIR_PATH, 'new_csv.csv'), 'w', newline='') as csv_file:
        csvwriter = csv.writer(csv_file, delimiter=';')
        csvwriter.writerow(['Bonny', 'Born', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    with open(os.path.join(RESOURCES_DIR_PATH, 'new_csv.csv')) as csv_file:
        csvreader = csv.reader(csv_file, delimiter=';')
        for row in csvreader:
            print(row)