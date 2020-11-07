from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from Model.store import StoreModel

class Store(Resource):

    def get(self, name):
        store = StoreModel.get_by_name(name)
        print(store.json())
        if store:
            return store.json()
        return {"Message": "Store is not found"}, 404

    def post(self,name):
        if StoreModel.get_by_name(name):
            return {'Message':"Store {}already exists ".format(name)},400
        store=StoreModel(name)
        try:
            store.save_to_db()
        except :
            return {"Message":"An error ocurred during the creation of db"},500

        
        return store.json(),200

    def delete(self,name):
        store=StoreModel.get_by_name(name)
        if store:
            store.delete_from_db()
        
        return {"Message":"Store has been deleted"}

   
class StoreList(Resource):

    def get(self):

        return {'stores':[store.json() for store in StoreModel.query.all()]}
    
    