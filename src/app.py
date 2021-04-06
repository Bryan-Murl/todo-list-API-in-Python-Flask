from flask import Flask, jsonify, request
app = Flask(__name__)
import json 

todos = [{ "label": "My first task", "done": False }, { "label": "Other task", "done": False }]

#Get=Obtener
@app.route('/todos', methods=['GET']) 
def hello_world1():
    json_text= jsonify(todos)
    return json_text

#Post=Agregar, !imp=14,15,19,20 
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    json_text = jsonify(todos)
    return json_text

#Delete
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    print("this is the position to delete", position)
    return jsonify(todos)





if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)