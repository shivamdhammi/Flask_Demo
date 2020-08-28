from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from flask import request
from models.item import ItemModel

class Item(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help = "This field cannot be left blank."
    )

    parser.add_argument(
        'store_id',
        type=int,
        required=True,
        help = "Every item needs a store id."
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.findByName(name)
        if item: 
            return item.json()
        else:
            return {"message": "Item not found"}, 404

    def post(self,name):
        if ItemModel.findByName(name):
            return {"message" :f"Item with name - {name} already exists"}, 400
        
        data = self.parser.parse_args()
        item = ItemModel(name,data['price'],data['store_id'])
        item.save_to_db()

        return item.json(), 201

    def delete(self,name):
        item = ItemModel.findByName(name)
        if item:
            item.delete_from_db()
        
        return {'message':"Item deleted."}

    def put(self,name):
        # data = request.get_json(silent=True)
        data = self.parser.parse_args()
        item =  ItemModel.findByName(name)
        
        if item is None:
           item = ItemModel(name,data['price'],data['store_id'])
        else:
            item.price = data['price']
        
        item.save_to_db()

        return item.json(), 201


class ItemList(Resource): 
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}
