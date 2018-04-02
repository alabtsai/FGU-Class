
from bottle import route, run

@route('/hello')
def hello():
    return "Hello World! Do you love Python?"

run(host='120.101.45.214', port=8080, debug=True)
