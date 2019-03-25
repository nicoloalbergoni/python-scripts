import os
from pikepdf import Pdf


def unlock_pdf(fileName, password, pathToSave='./unlocked/'):

    if not os.path.exists(pathToSave):
        os.makedirs(pathToSave)
    locked_file = Pdf.open(fileName, password=password)
    output = Pdf.new()
    output.pages.extend(locked_file.pages)
    output.save(pathToSave + fileName)


def get_all_pdfs(path):
    files = []

    for f in os.listdir(path):
        if os.path.isfile(f) and f.endswith('.pdf'):
            files.append(f)

    return files


def main():

    files = get_all_pdfs('.')    
    for f in files:
        unlock_pdf(f, 'SGQ1819')


if __name__ == '__main__':
    main()
