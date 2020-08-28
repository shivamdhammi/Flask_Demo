from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.findByName(name)
        if store:
            return store.json(), 200
        else:
            return {'mesage': 'Store not found'}

    def post(self, name):
        if StoreModel.findByName(name):
            return {'mesage': f"Store with name - {name} already exists"}, 400
        else:
            store = StoreModel(name)
            try:
                store.save_to_db()
            except:
                return {'mesage': "Error occured while creating the store"}, 500

        return store.json(), 201
            

    def delete(self, name):
        store = StoreModel.findByName(name)
        if store:
            store.delete_from_db()
        
        return {"message", "Store Deleted."}

class  StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
        