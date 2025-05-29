from flask import Flask,request,jsonify
app = Flask(__name__)

#sample

items = []

@app.route("/items",methods = ['GET'])
def get_items():
    return jsonify(items),200


@app.route("/items",methods = ["POST"])
def add_items():
    data = request.get_json()
    if not data or 'name' not in data:
        return  jsonify({'error':'Name is required'}),400
    item = {'id':len(items)+1,'name':data['name']}
    items.append(item)
    return jsonify(item),201

if __name__ == '__main__':
    app.run(debug=True)