from flask import Flask, request,jsonify
from flask_restful import Resource, Api
from json import dumps
from api import Food,Foods

# data = {
#     '_id' : 'ts02',
#     'name':'Trà sữa Thái Lan',
#     'price': 22000.0
# }
app = Flask(__name__)
api = Api(app)

# db.Food.insert_one(data)



@app.route('/',methods=['GET'])
def home():
    return '<h1>This is API for Food APP</h1><br>' \
           '<p>You can read <a href="/docs">docs</a> to use</p>'
@app.route('/docs',methods=['GET'])
def docs():
    return '<h1>This is a document use API for Food APP</h1><br>' \
           '<p>You can read <a href="/docs">docs</a> to use</p>'

api.add_resource(Foods, '/foods')  # Route_1
api.add_resource(Food, '/foods/<id>')  # Route_3
# #api.add_resource(Tracks, '/tracks')  # Route_2
# api.add_resource(Employees_Name, '/food/<employee_id>')  # Route_3

if __name__ == '__main__':
    app.run(debug=True)