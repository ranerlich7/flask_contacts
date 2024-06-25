from flask import Flask, render_template

app = Flask(__name__)

my_contacts = [
    {"name": "Ran", "age": 44, "phone":"05544444"},
    {"name": "Aviad", "age": 25, "phone":"050444222"}
]


@app.route("/")
def contact_list():
    return render_template('contact_list.html', contacts = my_contacts)

    # final_str = ""
    # for contact in my_contacts:
    #     final_str += f"<li style='color:blue'>{contact["name"]} - {contact["phone"]}</li>"
    # return final_str


@app.route("/single_contact/<int:index>")
def single_contact(index):
    return f"user is {my_contacts[index]["name"]} - {my_contacts[index]["phone"]}"


@app.route("/add")
def add_contact():
    return "please add a contact"


if __name__ == "__main__":
    app.run(debug=True, port=9000)
