from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/api/data')
def get_data():
    return {"data": "Sample data"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
