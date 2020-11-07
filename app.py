from flask import Flask
from flask_restful import Api
from flask_jwt import JWT


from security import authenticate, identity
from Resource.users import UserRegister
from Resource.Items import ItemList,Items
from Resource.store import StoreList,Store

# will create falky app immediatly after importing flask lib
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key="momoland"

api = Api(app)

@app.before_request
def create_table():
    db.create_all()

jwt = JWT(app, authenticate, identity)  # /auth


api.add_resource(StoreList, '/stores')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Items, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True)
