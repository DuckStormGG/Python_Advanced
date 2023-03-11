from flask import Flask
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route("/preview/<int:size>/<path:file_path>")
def preview(size,file_path):
    abs_path = os.path.abspath(file_path.split("/")[-1])
    print(abs_path)
    file = open(abs_path,'r')
    content = file.read(size)
    return f"{abs_path} {size} <br> {content}"

if __name__ == "__main__":
    app.run(debug=True)