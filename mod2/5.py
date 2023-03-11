from flask import Flask

app = Flask(__name__)

@app.route("/max_number/<path:numbers>")
def max_number(numbers):
    if numbers.replace("/","").isdigit():
        numbers_list = list(map(int,numbers.split("/")))
        numbers_list = sorted(numbers_list)
        return f"Максимальное число: {numbers_list[-1]}"
    else:
        return "List must contain only numbers"

if __name__ == "__main__":
    app.run(debug=True)
