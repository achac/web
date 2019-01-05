
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def place(keywords)->str:
    parameters = {'keywords': keywords,'key': '5176be5de5f9ee80e0dc7e63a629a2aa'}
    base = 'https://restapi.amap.com/v3/place/text'
    response = requests.get(base, parameters)
    answer = response.json()
    return str(answer['pois'][0]['address'])

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    title = '这是查询结果:'
    results = place(phrase)
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_results=results,)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='欢迎使用高德地图关键词查询')


if __name__ == '__main__':
    app.run(debug=True)
