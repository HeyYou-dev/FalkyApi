from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from Model.Items import ItemModel

class Items(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float, required=True, help="this feild can't be left blank!"
    )
    parser.add_argument(
        'store_id',
        type=int, required=True, help="Every items ned "
    )


    @jwt_required()
    def get(self, name):
        item = ItemModel.get_by_name(name)
        print(item)
        if item:
            return item.json()
        return {"Message": "item not found"}, 404

    def post(self, name):
        itemRow=ItemModel.get_by_name(name)
        data = Items.parser.parse_args()
        if (itemRow.name==name and itemRow.store_id==data['store_id']):
            return{"Message":"item name {0},already exist in store {1}".format(itemRow.name,itemRow.store_id)}
        
        item = ItemModel(name, data['price'],data['store_id'])
        item.save_to_db()
        return item.json(), 201

    def delete(self, name):

        item=ItemModel.get_by_name(name)
        if item:
            item.delete_from_db()
            return{"message": "item deleted "}

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'price',
            type=float, required=True, help="this feild can't be left blank!"
        )
        data = parser.parse_args()

        item = ItemModel.get_by_name(name)

        if item is None:
            item = ItemModel(name,data['price'],data['store_id'])
        else:

            item.price=data['price']
        item.save_to_db()
        return item.json()




class ItemList(Resource):

    def get(self):
        
        return {"items":[ item.json() for item in ItemModel.query.all()]}
