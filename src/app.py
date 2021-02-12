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

    # "{} ".format(i) = create a string with the value "i"
    # bracket = create a list with values "1" to "n"
    # create a new string consists of the values of the list joined with a space for each value.
    return " ".join(["{}".format(i) for i in range(1, int(number) + 1)])


@app.route("/<number>/odd")
def print_odd_numbers(number):
    if not number.isnumeric():
        return number + " is not numeric"

    return " ".join(["{}".format(i) for i in range(1, int(number) + 1, 2)])


@app.route("/<number>/even")
def print_even_numbers(number):
    if not number.isnumeric():
        return number + " is not numeric"

    return " ".join(["{}".format(i) for i in range(2, int(number) + 1, 2)])


@app.route("/<number>/prime")
def print_prime_numbers(number):
    if not number.isnumeric():
        return number + " is not numeric"

    if int(number) <= 1:
        return "Prime number starts from 2"

    number_range = int(number) + 1
    prime = [True for _ in range(number_range)]  # _ because i is not needed
    prime[0] = prime[1] = False

    for i in range(2, number_range):
        if prime[i]:
            # remove all numbers that are multiples of i
            for j in range(i * i, number_range, i):
                prime[j] = False

    # output = ""
    # for i in range(2, number_range):
        # if prime[i]:
            # output += "{}".format(i)
    return " ".join(["{}".format(i) for i in range(2, number_range) if prime[i]])


# run the flask app when running this file (app.py)
if __name__ == "__main__":
    app.run(debug=True)
