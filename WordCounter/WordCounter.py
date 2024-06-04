from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/', methods=['post', 'get'])
def form():
    answer = []
    extraanswer = ''
    if request.method == 'POST':
        counter = GenerateCounterDict(request.form.get('txt'))
        answer, extraanswer = SortedCounter(counter)
    return render_template('index.html', answer=answer, extraanswer=extraanswer, isempty=(len(answer)==0))

def GenerateCounterDict(text):
    words = re.split(r'\W+', text.lower())
    counter = {'word': [], 'count': []}
    for word in words:
        if word in counter['word']:
            counter['count'][counter['word'].index(word)] += 1
        elif word != '':
            counter['word'].append(word)
            counter['count'].append(1)
    return counter

def SortedCounter(counter):
    answer = []
    extraanswer = ''
    for i in range(len(counter['word'])):
        for j in range(len(counter['word'])):
            if counter['count'][j] == max(counter['count']) and counter['count'][j] > 1:
                answer.append(str.format('{0} - {1}', counter['word'][j], counter['count'][j]))
                del counter['word'][j], counter['count'][j]
                break
            elif counter['count'][j] == max(counter['count']):
                extraanswer += counter['word'][j] + ', '
                del counter['word'][j], counter['count'][j]
                break
    return answer, extraanswer[:-2]

if __name__ == '__main__':
    app.run()