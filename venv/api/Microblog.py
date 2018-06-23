import json
from flask_restful import Resource, Api
from flask import Flask, abort, request, g, session
from utils import *
from Authentications import *
from DB_Access import *
from Users import verify_user, create_new_user

app = Flask(__name__)
api = Api(app)


@app.before_request
def before_request():
    g.db = sqlite3.connect(app.config['DATABASE_NAME'])


class BlogEntryResource(Resource):
    def get(self, id):
        entry = search_entry(id)
        if entry == False:
            return abort(404)
        return json_response(json.dumps(entry))

    def delete(self, id):
        if search_blog_entry(id) is None:
            return abort(404)
        if not authenticate_delete_request(id):
            return abort(401)
        delete_entry(id)
        return json_response('', status=204)

    def update(self, content):
        # ToDo: add update support
        pass


class BlogEntriesListResource(Resource):
    def get(self):
        return ""

    def post(self):
        if not session['logged_in']:  # is user logged in
            return abort(401)
        entry = request.json
        if not authenticate_post_request(entry, 'EntryPost'):
            return abort(400)
        add_entry(entry)
        return json_response('', status=201)


class UserLoginResource(Resource):
    def post(self):
        user = request.json
        if not authenticate_post_request(user, 'UserPost'):
            return abort(400)
        if not verify_user(user['name'], user['password']):
            return abort(400)
        return json_response('')


class UserSignUpResource(Resource):
    def post(self):
        user = request.json
        if not authenticate_post_request(user, 'UserPost'):
            return abort(400)
        if not create_new_user(user['name'], user['password']):
            return abort(400)
        return json_response('')


api.add_resource(BlogEntryResource, '/entry/<int:id>')
api.add_resource(BlogEntriesListResource, '/entry')
api.add_resource(UserLoginResource, '/login')
api.add_resource(UserSignUpResource, '/signup')


