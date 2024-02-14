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
    # info on the find and replace method https://www.geeksforgeeks.org/python-string-replace/
    # Credit to Jason for string concatenation clarification
    url = "https://www.google.com/search?q="+pdfname.replace(" ", "+")+"+free+PDF"

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
    # find out how to get the stuff in the cite tage, this is the important link
    p = soup.find_all('a')

    # iterate through p for getting all the href links
    for link in p:
        # original html links
        # info on finding if string contains substring from: https://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method
        href_link = link.get('href')
        if "/url?q=" in href_link and "http" in href_link:
            base_link = href_link[href_link.find("/url?q")+7:]
            # get the url from requests get method
            print(base_link)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/







