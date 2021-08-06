# Import required libraries
import argparse
import requests
from bs4 import BeautifulSoup

# Main function
def main():
    
    # global html_text, dont_include # Global variables will be used in sub-functions too

    args = create_parser()
    args.url = check_prefix(args.url)
    
    response = requests.get(args.url) # makes a GET request to the inputted URL
    
    if response.status_code == 200: # some input validation for inputted url to make sure the status of the GET request is "OK" 
        create_and_output_file(args.url)
    else:
        print('Invalid URL')

# Function that takes care of the command line argument
def create_parser():
    parser = argparse.ArgumentParser()  
    parser.add_argument("url") # create parser and add the argument "url" which is parsed through to the script
    args = parser.parse_args()
    return args

# Function that serves as some input validation for the inputted url to make sure it includes "https://" to ensure a successful GET request later
def check_prefix(url):
    prefix = "https://" 
    if prefix not in url:
        return f"{prefix}{url}" # if user fails to include the protocol prefix for the inputted url, it will be added
    else:
        return url

# Function that creates a .txt file and stores only the text content of the inputted url's HTML page, filtered through a blacklist of unwanted tags
def create_and_output_file(url):
    output = ''
    response = requests.get(url) # stores all the HTML content from the inputted url as a "soup" which is traversed and then stores only the text-content as a variable html_text
    html_page = response.content
    soup = BeautifulSoup(html_page, 'html.parser')
  
    html_text = soup.find_all(text=True)
    dont_include = [ # defines what tags in the html contain un-needed text
        '[document]', # removes the first line reading "html"
        'head', # removes meta data
        'script', # ensures scripts are not extracted
	    'style', # removes webpage styling
	    'alttext', # removes alt text for images
        'mi', # removes symbolic constants
        'mo', # removes mathematical operators
    ]
    # file_name = input("Save file as: ") # user can choose what to call their file and this is where the desired text content will be stored
    f = open("file.txt", "w", encoding="utf-8") 
    for line in html_text: # loops through the entire html_text to find all inner text that dont belong to the above "blacklisted" tags and then writes it to the file
        if line.parent.name not in dont_include:
            output += '{} '.format(line)

    f.write(output)

    f.close()

if __name__ == '__main__': main()