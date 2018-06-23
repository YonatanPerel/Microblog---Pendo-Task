
request_templates = {
    'EntryPost': {'content': (unicode, str)},
    'UserPost': {'name': (unicode, str), 'password': (unicode, str)}
    }


def authenticate_user_request():
    #ToDo: Check if the user can upload a new post
    pass


def authenticate_post_request(request, request_type):
    if request_type not in request_templates.keys():
        print "Request type doesn't exist"
        return False
    template = request_templates[request_type]
    for key in template.keys():
        if key not in request.keys():
            print "Bad request: parameters missing"
            return False
        if not isinstance(request[key], template[key]):
            print "Bad request: parameters not of the correct type"
            return False
    return True


def authenticate_delete_request(id):
    #ToDo: Check if current user is an admin or the original creator of the entry, and can delete it.
    pass
