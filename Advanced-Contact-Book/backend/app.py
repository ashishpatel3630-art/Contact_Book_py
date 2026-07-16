from flask import Flask,request,jsonify
from flask_cors import CORS

from database import (
    add_contact,
    get_contacts,
    update_contact,
    delete_contact,
    search_contact
)


app = Flask(__name__)

CORS(app)



@app.route("/")
def home():

    return {
        "message":"Contact Book API Running"
    }



@app.route("/contacts",methods=["GET"])
def contacts():

    return jsonify(
        get_contacts()
    )



@app.route("/add",methods=["POST"])
def add():


    data=request.json


    result=add_contact(
        data["name"],
        data["phone"],
        data["email"]
    )


    if result:

        return jsonify({
            "message":"Contact Added"
        })


    return jsonify({
        "message":"Already Exists"
    })





@app.route("/update/<name>",methods=["PUT"])
def update(name):

    data=request.json


    result=update_contact(
        name,
        data["phone"],
        data["email"]
    )


    if result:

        return jsonify({
            "message":"Updated"
        })


    return jsonify({
        "message":"Not Found"
    })





@app.route("/delete/<name>",methods=["DELETE"])
def delete(name):


    result=delete_contact(name)



    if result:

        return jsonify({
            "message":"Deleted"
        })


    return jsonify({
        "message":"Not Found"
    })





@app.route("/search/<name>")
def search(name):

    return jsonify(
        search_contact(name)
    )




if __name__=="__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )