from flask import Flask,render_template
import requests
from datetime import datetime,timedelta
app = Flask(__name__)
app.secret_key = "secret key"
@app.route("/")
def india():
    url="https://newsapi.org/v2/top-headlines?country=in&apiKey=297b5aed463049be809ea5684acedf26"
    r=requests.get(url).json()
    case={
        "articles":r["articles"]
    }
    return render_template('india.html',cases=case)
@app.route("/us")
def us():
    url="https://newsapi.org/v2/top-headlines?country=us&apiKey=297b5aed463049be809ea5684acedf26"
    r=requests.get(url).json()
    case={
        "articles":r["articles"]
    }
    return render_template('us.html',cases=case)

@app.route("/swiz")
def swiz():
    url="https://newsapi.org/v2/top-headlines?country=ch&apiKey=297b5aed463049be809ea5684acedf26"
    r=requests.get(url).json()
    case={
        "articles":r["articles"]
    }
    return render_template('swiz.html',cases=case)

@app.route("/aus")
def aus():
    url="https://newsapi.org/v2/top-headlines?country=au&apiKey=297b5aed463049be809ea5684acedf26"
    r=requests.get(url).json()
    case={
        "articles":r["articles"]
    }
    return render_template('aus.html',cases=case)

@app.route("/arg")
def aur():
    url="https://newsapi.org/v2/top-headlines?country=ar&apiKey=297b5aed463049be809ea5684acedf26"
    r=requests.get(url).json()
    case={
        "articles":r["articles"]
    }
    return render_template('aus.html',cases=case)

@app.route("/bel")
def bel():
    url="https://newsapi.org/v2/top-headlines?country=be&apiKey=297b5aed463049be809ea5684acedf26"
    r=requests.get(url).json()
    case={
        "articles":r["articles"]
    }
    return render_template('aus.html',cases=case)

@app.route("/ger")
def ger():
    url="https://newsapi.org/v2/top-headlines?country=de&apiKey=297b5aed463049be809ea5684acedf26"
    r=requests.get(url).json()
    case={
        "articles":r["articles"]
    }
    return render_template('aus.html',cases=case)

@app.route("/bit_coin")
def bit():
    # Get today's date
    today = datetime.now()
    # Get the date for the previous day
    previous_day = today - timedelta(days=1)

    # Format dates as YYYY-MM-DD
    previous_day_str = previous_day.strftime('%Y-%m-%d')

    # Set the date range to the previous day
    url = f"https://newsapi.org/v2/everything?q=bitcoin&from={previous_day_str}&to={previous_day_str}&sortBy=popularity&apiKey=297b5aed463049be809ea5684acedf26"
    r = requests.get(url).json()

    case = {
        "articles": r["articles"]
    }
    return render_template('bit.html', cases=case)


@app.route("/apple")
def apple():
    today = datetime.now()
    previous_day = today - timedelta(days=1)
    previous_day_str = previous_day.strftime('%Y-%m-%d')

    url = f"https://newsapi.org/v2/everything?q=apple&from={previous_day_str}&to={previous_day_str}&sortBy=popularity&apiKey=297b5aed463049be809ea5684acedf26"
    r = requests.get(url).json()

    case = {
        "articles": r["articles"]
    }
    return render_template('apple.html', cases=case)


@app.route("/tech")
def tech():
    today = datetime.now()
    previous_day = today - timedelta(days=1)
    previous_day_str = previous_day.strftime('%Y-%m-%d')

    url = f"https://newsapi.org/v2/everything?domains=techcrunch.com,thenextweb.com&from={previous_day_str}&to={previous_day_str}&apiKey=297b5aed463049be809ea5684acedf26"
    r = requests.get(url).json()

    case = {
        "articles": r["articles"]
    }
    return render_template('tech.html', cases=case)
if __name__== "__main__":
    app.run(debug=True) 