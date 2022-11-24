from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Name: romleger\nOccupation: Programmer\nHobbies: writing code\nFavorite website: www.youtube.cm\nContact:romleger2011@Gmail.com'


if __name__ == "__main__":
    app.run()
