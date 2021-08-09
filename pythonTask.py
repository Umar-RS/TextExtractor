import requests
import argparse
from bs4 import BeautifulSoup

class TextExtractor:
    def __init__(self, url):
        self.url = url

    def check_prefix(self):
        prefix = "https://" 
        if prefix not in self.url:
            return f"{prefix}{self.url}" # if user fails to include the protocol prefix for the inputted url, it will be added
        else:
            return self.url

    def get_content(self):
        self.output = ''
        response = requests.get(self.url) # stores all the HTML content from the inputted url as a "soup" which is traversed and then stores only the text-content as a variable html_text
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
        
        for line in html_text: # loops through the entire html_text to find all inner text that dont belong to the above "blacklisted" tags and then writes it to the file
            if line.parent.name not in dont_include:
                self.output += '{} '.format(line)
    
    def output_file(self):
        # file_name = input("Save file as: ") # user can choose what to call their file and this is where the desired text content will be stored
        f = open("file.txt", "w", encoding="utf-8") 
        f.write(self.output)
        f.close()

def main():

    parser = argparse.ArgumentParser()  
    parser.add_argument("--url") # create parser and add the argument "url" which is parsed through to the script
    args = parser.parse_args()

    test = TextExtractor(args.url)
    
    test.url = test.check_prefix()

    response = requests.get(test.url) # makes a GET request to the inputted URL
    
    if response.status_code == 200: # some input validation for inputted url to make sure the status of the GET request is "OK" 
        test.get_content()
    else:
        print('Invalid URL')

    test.output_file()

if __name__ == '__main__': main()