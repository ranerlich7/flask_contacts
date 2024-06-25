from flask import Flask

app = Flask(__name__)

my_contacts = [{"name": "Ran", "age": 44}, {"name": "Aviad", "age": 25}]


@app.route("/")
def contact_list():
    return f"{my_contacts}"


@app.route("/single_contact/<int:usernumber>")
def single_contact(usernumber):
    return f"user is {usernumber}"


@app.route("/add")
def add_contact():
    return "please add a contact"


if __name__ == "__main__":
    app.run(debug=True, port=9000)
