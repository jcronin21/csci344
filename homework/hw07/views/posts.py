from flask import Response, request
from flask_restful import Resource
from models import Post, Following, db
from views import get_authorized_user_ids

import json

def get_path():
    return request.host_url + 'api/posts/'

def get_list_of_user_ids_in_my_network():
    following = Following.query.filter_by(user_id=self.current_user.id).all()
    friend_ids = []

class PostListEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user

    
#user doesnt specify a limit: 20
# user specifies a valid int <= 50:
#    that number
#user gives you abc -> 400 error
# user gives you a limi 51 -> 400 error
    def get(self):
        limit = request.args.get('limit')
        # get posts created by one of these users:
        #1 get all of the user ids of the ppl that the user 12 is following 
        following = Following.query.filter_by(user_id=self.current_user.id).all()
        friend_ids = []
        #building a list of friend usernames
        for rec in following:
            friend_ids.append(rec.following_id)
        friend_ids.append(self.current_user.id)
        print(friend_ids)
        try:
            limit = (request.args.get('limit')) or 20
            limit = int(limit)
        except:
            return Response(
                json.dumps({'error': 'no string fro limit.'}), status=400
            )
        if limit > 50:
            return Response(
                json.dumps({'error': 'Bad data. Limit cannot exceed 20.'}), status =400
            )
        #posts = Post.query.filter_by(user_id = self.current_user.id).all()
        posts = Post.query.filter(Post.user_id.in_(friend_ids)).limit(limit)
        return Response(json.dumps([post.to_dict() for post in posts]), mimetype="application/json", status=200)

    def post(self):
        # create a new post based on the data posted in the body 
        body = request.get_json()
        print(body)  
        return Response(json.dumps({}), mimetype="application/json", status=201)
        
class PostDetailEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user
        

    def patch(self, id):
        # update post based on the data posted in the body 
        body = request.get_json()
        print(body)       
        return Response(json.dumps({}), mimetype="application/json", status=200)


    def delete(self, id):
        # delete post where "id"=id
        pass
    


    def get(self, id):
        # get the post based on the id
        post = Post.query.get(id)
        if post is None:
            error_message ={
                'error': ' post {0} does not exist.'.format(id)
            }
            return Response(json.dumps(error_message), mimetype="application/json",status=404)
        else:
         return Response(json.dumps(post.to_dict()), mimetype="application/json", status=200)

def initialize_routes(api):
    api.add_resource(
        PostListEndpoint, 
        '/api/posts', '/api/posts/', 
        resource_class_kwargs={'current_user': api.app.current_user}
    )
    api.add_resource(
        PostDetailEndpoint, 
        '/api/posts/<int:id>', '/api/posts/<int:id>/',
        resource_class_kwargs={'current_user': api.app.current_user}
    )