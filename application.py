from flask import Flask
import hashlib

application = Flask(__name__)

@application.route('/')
def home():
    return 'Hello, World! This is the home page.'

@application.route('/stress')
def stress():
    # A simple CPU load generator
    result = sum(hashlib.sha256(str(i).encode('utf-8')).hexdigest() for i in range(100000))
    return f'Generated some CPU load. Checksum: {result}'

if __name__ == '__main__':
    application.run(debug=True)
