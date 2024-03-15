import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/stocks')
def stocks():
  return render_template('stock.html')


def get_news():
  api_key = '3fd8f6493ce143ecb8b71534c91622b7'  # Replace 'YOUR_API_KEY' with your actual API key for news API
  url = f'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={api_key}'
  response = requests.get(url)
  data = response.json()
  return data['articles']

# Route to display news on a webpage
@app.route('/news')
def news_section():
  news_data = get_news()

  return render_template('news.html', news=news_data)

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/')
def index():
  return render_template('home.html')

  

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
