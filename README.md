<h1>Text Extractor</h1><br>
<p><strong>Aim:</strong> The program retrieves the text content of a website and then stores it as a .txt file.</p>
<p><strong>How to use:</strong>
<ol>
  <li>Download and extract code file</li>
  <li>Open CLI and navigate to code file</li>
  <li>Run the Flask App through CLI:
    <ul>
      <li><code>set FLASK_APP=app.py</code></li>
      <li><code>set FLASK_ENV=development</code></li>
      <li><code>flask run</code></li>
    </ul>
  </li>
  <li>Input the URL of the website you wish to extract text from, then click "Scrape".</li>
  <li>A file called <code>file.txt</code> will be created in the code file, simply open the .txt file to check content.</li>
</ol>
<strong>Libraries</strong>
<ul>
  <li>Requests (to install: <code>pip install requests</code>)</li>
  <li>Beautiful Soup 4 (to install: <code>pip install beautifulsoup4</code>)</li>
  <li>Argparse (to install: <code>pip install argparse</code>)</li>
  <li>Pathlib (to install: <code>pip install pathlib</code>)</li>
  <li>Pytest (to install: <code>pip install -U pytest</code>)</li>
  <li>Flask (to install: <code>pip install flask</code></li>
</ul>
