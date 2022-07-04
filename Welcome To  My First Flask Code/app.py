from flask import Flask, render_template,jsonify,request
app = Flask(__name__)

@app.route('/')                          #To render homepage
def home_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000)