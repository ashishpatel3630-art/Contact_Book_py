from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os


app = Flask(__name__)
CORS(app)


FILE = "ContactBook.json"


def load_contacts():

    if os.path.exists(FILE):
        with open(FILE,"r") as f:
            return json.load(f)

    return {}



def save_contacts(data):

    with open(FILE,"w") as f:
        json.dump(data,f,indent=4)



@app.route("/contacts",methods=["GET"])
def get_contacts():

    contacts = load_contacts()

    return jsonify(contacts)



@app.route("/add",methods=["POST"])
def add_contact():

    data=request.json

    contacts=load_contacts()

    contacts[data["name"]] = {
        "phone":data["phone"],
        "email":data["email"]
    }

    save_contacts(contacts)

    return jsonify({
        "message":"Contact Added"
    })



@app.route("/delete/<name>",methods=["DELETE"])
def delete_contact(name):

    contacts=load_contacts()


    if name in contacts:

        del contacts[name]

        save_contacts(contacts)

        return jsonify({
            "message":"Deleted"
        })


    return jsonify({
        "message":"Not Found"
    })




@app.route("/update/<name>",methods=["PUT"])
def update_contact(name):

    contacts=load_contacts()

    data=request.json


    if name in contacts:

        contacts[name]["phone"]=data["phone"]
        contacts[name]["email"]=data["email"]

        save_contacts(contacts)


        return jsonify({
            "message":"Updated"
        })


    return jsonify({
        "message":"Contact not found"
    })



@app.route("/search/<name>")
def search(name):

    contacts=load_contacts()

    result={}

    for key,value in contacts.items():

        if name.lower() in key.lower():

            result[key]=value


    return jsonify(result)



if __name__=="__main__":

    app.run(debug=True)