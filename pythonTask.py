import requests
from bs4 import BeautifulSoup

url = input('Enter URL: ')

def main():
    response = requests.get(url)
    
    if response.status_code == 200: # some input validation for inputted url

        response = requests.get(url) 
        html_page = response.content
        soup = BeautifulSoup(html_page, 'html.parser')
        html_text = soup.find_all(text=True)

        file_name = input("Save file as: ")
        f = open(f"{file_name}.txt", "w", encoding="utf-8") # Creating html_text.txt file with appropriate encoding, (can change file name, if necessary))

        output = ''
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

        for line in html_text:
            if line.parent.name not in dont_include:
                output += '{} '.format(line)

        f.write(output)

        f.close()

    else:
        print('Invalid URL')

if __name__ == '__main__': main()