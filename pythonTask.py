# Import required libraries

import argparse
import requests
from bs4 import BeautifulSoup

def create_parser():# create parser and add the argument "url" which is parsed through to the script
    parser = argparse.ArgumentParser()  
    parser.add_argument("url")
    global args
    args = parser.parse_args()
    return args
    
def check_prefix():# if user fails to include the protocol prefix for the inputted url, it will be added
    prefix = "https://" 
    if prefix not in args.url:
        return f"{prefix}{args.url}"
    else:
        return args.url

def output_file():
    global output
    output = ''
    file_name = input("Save file as: ") # user can choose what to call their file and this is where the desired text content will be stored
    f = open(f"{file_name}.txt", "w", encoding="utf-8") 
    for line in html_text: # loops through the entire html_text to find all inner text that dont belong to the above "blacklisted" tags and then writes it to the file
        if line.parent.name not in dont_include:
            output += '{} '.format(line)

    f.write(output)

    f.close()


def main():
    global html_text, dont_include
    args = create_parser()
    args.url = check_prefix()

    response = requests.get(args.url) # makes a GET request to the inputted URL
    
    if response.status_code == 200: # some input validation for inputted url to make sure the status of the GET request is "OK"

        response = requests.get(args.url) # stores all the HTML content from the inputted url as a "soup" which is traversed and then stores only the text-content as a variable html_text
        html_page = response.content
        soup = BeautifulSoup(html_page, 'html.parser')
  
        html_text = soup.find_all(text=True)
        dont_include = [ # defines what tags in the html contain un-needed text
            '[document]', # gets rid of the first line reading "html"
            'head', 
            'script', # ensures scripts are not extracted
	        'style', # removes webpage styling
	        'alttext', 
            'annotation',
            'mi', # removes symbolic constants
            'mo', # removes mathematical operators
        ]     
        output_file()
    else:
        print('Invalid URL')

if __name__ == '__main__': main()