from flask import Flask, jsonify, request

app = Flask(__name__)

contacts =[
    {
        'id':1,
        'Name':u'Aayushi',
        'Contact':u'****'
    },
    {
        'id':2,
        'Name':u'abc',
        'Contact':u'****'
    },
    {
        'id':3,
        'Name':u'xyz',
        'Contact':u'****'
    }
]

@app.route("/add-data",method=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data!"
        },400)

    contact = {
        'id':contacts[-1]['id']+1,
        'Name':request.json['Name'],
        'Contact':request.json.get('Contact',""),
        'done':False
    }

    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message":"contact added successfully"
    })

print("works!!")