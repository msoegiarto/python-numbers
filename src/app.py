from flask import Flask

# a global application instance
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"


@app.route("/<number>")
def print_numbers(number):
    if not number.isnumeric():
        return number + " is not numeric"

    output = ""
    i = 1

    while i <= int(number):
        output += (str(i) + " ")
        i += 1

    return output


@app.route("/<number>/odd")
def print_odd_numbers(number):
    if not number.isnumeric():
        return number + " is not numeric"

    output = ""

    for i in range(1, int(number) + 1):
        if not is_even(i):
            output += (str(i) + " ")

    return output


@app.route("/<number>/even")
def print_even_numbers(number):
    if not number.isnumeric():
        return number + " is not numeric"

    output = ""

    for i in range(1, int(number) + 1):
        if is_even(i):
            output += (str(i) + " ")

    return output


@app.route("/<number>/prime")
def print_prime_numbers(number):
    if not number.isnumeric():
        return number + " is not numeric"

    if int(number) <= 1:
        return "Prime number starts from 2"

    output = ""

    number_range = int(number) + 1
    prime = [True for i in range(number_range)]
    prime[0] = prime[1] = False

    for i in range(2, number_range):
        if prime[i]:
            # remove all numbers that are multiples of i
            for j in range(i * i, number_range, i):
                prime[j] = False

    for i in range(2, number_range):
        if prime[i]:
            output += (str(i) + " ")

    return output


def is_even(number):
    return number % 2 == 0


# run the flask app when running this file (app.py)
if __name__ == "__main__":
    app.run(debug=True)
