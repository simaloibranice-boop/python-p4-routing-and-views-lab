from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<string:text>')
def print_string(text):
    print(text)
    return text


@app.route('/count/<int:number>')
def count(number):
    number_list = [str(i) for i in range(number)]
    return "\n".join(number_list) + "\n"


@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math_op(num1, operation, num2):
    result = 0

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return "Error: Cannot divide by zero"
        result = num1 / num2
    elif operation == '%':
        if num2 == 0:
            return "Error: Cannot modulo by zero"
        result = num1 % num2
    else:
        return f"Invalid operation: {operation}"

    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)

