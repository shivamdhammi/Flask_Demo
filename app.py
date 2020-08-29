from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

#This is to setup the flask for our project
app = Flask(__name__)
#this is to tell the SQLAlchemy that we will be using sqlite other options can be 
#oracle, mysql, posturge SQL(ya jo bhi spelling hai uski :))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
#modifications are already present. if we don't make it false there will be performance issues.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#This key should be secret if you are writing a production code
app.secret_key = "shivam"
#This enables us t o use classes i.e. use OOP aproch to make api calls
api = Api(app)



#This handles the '/auth' call and returns the access token.
# app.config['JWT_AUTH_URL_RULE'] = '/login' -- to change '/auth' to '/login'
# app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800) -- to change expiration time of token.
jwt = JWT(app,authenticate,identity)

# @jwt.auth_response_handler
# def customized_response_handler(access_token, identity):
#     return jsonify({
#                         'access_token': access_token.decode('utf-8'),
#                         'user_id': identity.id
#                    })


#Adding the classes to make the api calls.
api.add_resource(Item,'/item/<string:name>')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(StoreList,'/stores')
api.add_resource(UserRegister,'/register')

#beacuse we don't want to run the app again and again if this file gets imported some other file.
if __name__ == '__main__':
    app.run(port=5000, debug=True)

