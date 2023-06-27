from flask import Flask,render_template

app = Flask(__name__)


@app.route('/index.html')
def index():  # put application's code here
    return render_template("index.html")

@app.route('/time.html')
def time():  # put application's code here
    return render_template("time.html")

@app.route('/topic1.html')
def topic1():  # put application's code here
    return render_template("topic1.html")

@app.route('/topic2.html')
def topic2():  # put application's code here
    return render_template("topic2.html")

@app.route('/wordcloud.html')
def wordcloud():  # put application's code here
    return render_template("wordcloud.html")

@app.route('/line.html')
def line():  # put application's code here
    return render_template("line.html")

if __name__ == '__main__':
    app.run()
