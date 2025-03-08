from flask import Flask, render_template, request
from lorem_text import lorem

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ipsum', methods=['POST'])
def ipsum():
    if request.method == 'POST':
        try:
            num = int(request.form['num'])
        except ValueError:
            message = "'Length' requires a number value. Please try again."
            return render_template('index.html', generated_ipsum=message)
        output_format = request.form['output format']

        if output_format == 'Word(s)':
            generated_ipsum = lorem.words(num)
            return render_template('index.html', generated_ipsum=generated_ipsum)
        elif output_format == 'Paragraph(s)':
            generated_ipsum = lorem.paragraphs(num)
            return render_template('index.html', generated_ipsum=generated_ipsum)
        else:
            return render_template('index.html')

app.run()