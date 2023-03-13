from flask import Flask

app = Flask(__name__)
storage = {}


@app.route("/add/<date>/<int:number>")
def add(date, number):
    if date.isdigit():
        date_list = list(date)
        year = int("".join(date_list[0:4]))
        month = int("".join(date_list[4:6]))
        storage.setdefault(year, {}).setdefault(month, 0)
        storage[year][month] += number
        return f'Трата за {date} записана'
    else:
        return "Wrong Date"

@app.route("/calculate/<int:year>/<int:month>")
def calculate_y_m(year, month):
    expenses = 0
    expenses += storage[int(year)][month]
    return str(expenses)


@app.route("/calculate/<int:year>")
def calculate_y(year):
    expenses = 0
    for month in storage[int(year)]:
        expenses += storage[int(year)][month]
    return str(expenses)





if __name__ == "__main__":
    app.run(debug=True)