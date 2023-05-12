from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Name: rongoJustion\nOccupation: Programmer\nHobbies: writing code\nFavorite website: www.google.com\nContact:rongoaa@Gmail.com'


if __name__ == "__main__":
    app.run()

    
