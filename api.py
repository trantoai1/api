from flask import Flask, request, jsonify
from flask_restful import Resource, Api,reqparse
from pymongo import MongoClient
import pymongo
# pprint library is used to make the output look more pretty
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient('mongodb+srv://ptit:d17cqcp02n@cluster0.trnj9.gcp.mongodb.net/appdoan?retryWrites=true&w=majority')
db = client.appdoan
parser = reqparse.RequestParser()
parser.add_argument('id', type=str)
parser.add_argument('name', type=str)
parser.add_argument('price', type=float)

class Foods(Resource):
    def get(self):
        foods = db.Food.find({})  # Dòng này thực hiện truy vấn và trả về json
        return  [food for food in foods] # Tìm và thêm cột đầu tiên là Employee ID
    def post(self):

        args = parser.parse_args()
        id = args['id']
        name = args['name']
        price = args['price']
        food = db.Food.find_one({'name': name})
        if food:
            return {'status': -2, 'message': 'Tên food đã tồn tại'}
        #print(id+name+price)
        try:
            db.Food.insert_one({'_id':id,'name':name,'price':price})
            return {'status': 0, 'message': 'Thành công!'}
        except pymongo.errors.WriteError as e:
            return {'status':e.code,'message':e.details['errmsg']}


class Food(Resource):
    def get(self, id):
        food = db.Food.find_one({'_id':id})
        return jsonify(food)
    def put(self,id):
        food = db.Food.find_one({'_id': id})
        if not food:
            return {'status': -1, 'message': 'Món hàng không tồn tại'}
        args = parser.parse_args()
        name = args['name']
        price = args['price']
        try:
            db.Food.update_one({'_id':id},{'$set':{'name':name,'price':price}})
            return {'status': 0, 'message': 'Thành công!'}
        except pymongo.errors.WriteError as e:
            return {'status':e.code,'message':e.details['errmsg']}

