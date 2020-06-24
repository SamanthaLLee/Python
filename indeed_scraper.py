# import the necessary libraries needed for web scraping
import requests
import bs4
from bs4 import BeautifulSoup

# getting the url from the first page of an Indeed search for the skill 'Python'
url = 'https://www.indeed.com/jobs?q=python&l='
# using the Requests library's .get() method, request to get access to the website
page = requests.get(url)
# create a soup variable to store the parsed HTML data(BeautifulSoup method parses the website)
soup = BeautifulSoup(page.text, "html.parser")

# repeat the steps for the first url to this second url(second page of Indeed search)
url2 = 'https://www.indeed.com/jobs?q=python&start=10'
page2 = requests.get(url2)
soup2 = BeautifulSoup(page2.text, "html.parser")

# repeat the steps for the first url to this third url(second page of Indeed search)
url3 = 'https://www.indeed.com/jobs?q=python&start=20'
page3 = requests.get(url3)
soup3 = BeautifulSoup(page3.text, "html.parser")

def print_list(job_list):
    '''Function to print unique job titles in a readable way
    ARGS: a list
    RETURNS: prints out a list of unique job titles vertically
    '''
    # cast list to a set to remove instances of repeated job titles
    unique_list = set(job_list)
    # cast set back to list in order order to print list vertically
    set_list = list(unique_list)
    # for loop to print each job title
    for x in range(len(set_list)):
        print(set_list[x])

def get_job_title(soup):
    '''Function to get the job title from the results page of Indeed
    ARGS: a variable that stores all the parsed HTML data (i.e. a soup)
    RETURNS: a list of the job titles from the first three pages of Indeed search
    '''
    # empty list to store job titles
    job_titles = []
    # nested for loop to retrieve the job titles
    for div in soup.find_all(name="div", attrs={"class":"row"}):
      for a in div.find_all(name="a", attrs={"data-tn-element":"jobTitle"}):
          # a element nested in h2 element with attribute 'class' equal to 'title'
          # h2 element contains the job title
          job_titles.append(a["title"])
    return(job_titles)

# function calls
print("Page 1 results: ")
print_list(get_job_title(soup))

# empty print statement to increase readability of job titles once printed to console
print(" ")
print("Page 2 results: ")
print_list(get_job_title(soup2))

print(" ")
print("Page 3 results: ")
print_list(get_job_title(soup3))
