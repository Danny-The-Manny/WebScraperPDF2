import requests

from bs4 import BeautifulSoup

# Help on importing a github project: https://stackoverflow.com/questions/41023928/import-github-repository-to-pycharm

# warning
print("Warning: For educational use only")
print("Make sure to validate the integrity of sites before downloading from them.")
print()
# Gets the name of what pdf the user is searching for
pdfname = ""
while True:
    pdfname = input()
    if "-f " in pdfname:
        pdfname = pdfname[pdfname.find("-f "):]
        print()
        print("PDF Link(s):")
        # info on the find and replace method https://www.geeksforgeeks.org/python-string-replace/
        # Credit to Jason for string concatenation clarification

        # This creates the Google search friendly url
        url = "https://www.google.com/search?q="+pdfname.replace(" ", "+")+"+free+PDF"

        # this uses the request library to access the url
        read = requests.get(url)

        # takes the accessed url and gets the html
        html_content = read.content

        # Makes the html simi-readable
        soup = BeautifulSoup(html_content, "html.parser")

        # Stores website links
        list_of_pdf = set()

        # Gets the anchors
        p = soup.find_all('a')

        # iterate through p for getting all the href links
        for link in p:
            # Mostly fails if school blocking interferes
            # Info on try-except from: https://www.geeksforgeeks.org/python-try-except/
            try:
                # original html links
                # info on finding if string contains substring from: https://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method
                href_link = link.get('href')
                # Filtering out bad links
                if "/url?q=" in href_link and "http" in href_link:
                    # Filtering out bad links
                    base_link = href_link[href_link.find("/url?q")+7:]
                    base_link = base_link[:base_link.find("&sa=")]
                    # credit for info on try-except clauses: https://www.geeksforgeeks.org/python-try-except/

                    # repeat previous steps on the link variable
                    read = requests.get(base_link)
                    html_content = read.content
                    # Break from repeating previous steps to test to see if the link is a PDF
                    if ".pdf" in base_link:
                        list_of_pdf.add(base_link)
                        print(base_link)
                    else:
                        # Resume repeating previous steps
                        new_soup = BeautifulSoup(html_content, "html.parser")
                        g = soup.find_all('a')
                        for new_link in g:
                            try:
                                new_href_link = link.get('href')
                                if "/url?q=" in new_href_link and "http" in new_href_link:
                                    final_link = new_href_link[new_href_link.find("/url?q") + 7:]
                                    final_link = final_link[:final_link.find("&sa=")]
                                    if ".pdf" in final_link:
                                        list_of_pdf.add(base_link)
                                        print(base_link)
                                        break
                            except Exception:
                                x = 0
            except Exception:
                x = 0
        if len(list_of_pdf) == 0:
            print("No PDFs found")
    elif "-b" in pdfname:
        break







