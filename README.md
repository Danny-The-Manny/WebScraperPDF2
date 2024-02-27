This file is a PDF scraper made by Joshua Cogburn and Daniel Ramirez

Commands:
-f enternametosearchhere (finds potential free pdfs of the name entered)
-b (ends program)

The scraper operates as follows after the command is entered:
The user input will be appended to a variable
Using the input, the program will go to a Google search page and parse the results.
Once done Parsing, it will go through the search results and isolate PDFs
A list of the PDFs will be given to the user

This is meant to make research significantly easier for aspirng scholars.

Dependencies:
  - The requests library (https://pypi.org/project/requests/)
  - The BeautifulSoup4 library (https://pypi.org/project/beautifulsoup4/)
  - The io library
