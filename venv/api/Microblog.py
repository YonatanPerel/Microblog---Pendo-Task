import json
from flask_restful import Resource, Api
from flask import Flask
from utils import *
from Authentications import *
from DB_Access import *

app = Flask(__name__)
api = Api(app)

class BlogEntry(Resource):
    def get(self, id):
        entry = search_entry(id)
        if entry is None:
            return abort(404)
        return json_response(json.dumps(entry))

    def post(self, content):
        if not authenticate_post_request(content):
            return abort(400)
        add_entry_to_DB(content)
        return jason_response('', status=201)

    def delete(self, id):
        if search_blog_entry(id) is None:
            return abort(404)
        if not authenticate_delete_request(id):
            return abort(401)
        delete_entry(id)
        return json_response('', status=204)


api.add_resource(BlogEntry, '/entry/<int:id>')