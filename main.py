# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests

from bs4 import BeautifulSoup

import io

# from PyPDF2 import PdfFileReader


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # website to scrap
    pdfname = input("Enter the name of the pdf you are searching for: ")
    # Credit to Jason for string concatenation clarification
    url = "https://www.google.com/search?q="+pdfname+"+free+PDF"

    # get the url from requests get method
    read = requests.get(url)

    # full html content
    html_content = read.content

    # Parse the html content
    soup = BeautifulSoup(html_content, "html.parser")
    # This is the getting pdf part
    print(soup)
    # created an empty list for putting the pdfs
    list_of_pdf = set()

    # accessed the first p tag in the html
    # NEEDS TO GET ALL P
    #l = soup.find('href="/url?q=')

    # accessed all the anchors tag from given p tag
    p = soup.find_all('a')

    # iterate through p for getting all the href links
    for link in p:
        # original html links
        print("links: ", link.get('href'))
        print("\n")

        # converting the extension from .html to .pdf
        pdf_link = (link.get('href')[:-5]) + ".pdf"

        # converted to .pdf
        print("converted pdf links: ", pdf_link)
        print("\n")

        # added all the pdf links to set
        list_of_pdf.add(pdf_link)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/







