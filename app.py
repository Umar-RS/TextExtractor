from flask import Flask, render_template, request
import requests
from pythonTask import TextExtractor

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    title = "TextExtractor"
    fail = "Invalid URL. Please return and try again."
    success="file.txt downloaded. To access your file, navigate to the directory in which this script was downloaded. Your text content will be in a file called file.txt."
    if request.method == 'GET':
        return render_template('index.html', title=title)
    else:
        url = request.form.get('url', type=str)

        t_e = TextExtractor(url) # Istantiates class using the parsed argument as the parameter
    
        t_e.url = t_e.check_prefix()

        try:
            requests.get(t_e.url) # makes a GET request to the inputted URL
        except:
            return render_template('complete.html', title=title, message = fail)
        else:

            if requests.get(t_e.url).status_code == 200: # some input validation for inputted url to make sure the status of the GET request is "OK" 
                t_e.get_content()
            else:
                return render_template('complete.html', title=title, message = fail)

            t_e.output_file()

        return render_template('complete.html', title=title, message = success)
