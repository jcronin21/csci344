from flask import Response, request
from flask_restful import Resource
from models import Post, db
from views import get_authorized_user_ids

import json

def get_path():
    return request.host_url + 'api/posts/'

class PostListEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user

    def get(self):
        me_and_my_friend_ids = access_utils.get_list_of_user_ids_in_my_network(self.current_user.id)
        try:
            limit = request.args.get('limit') or 20
            limit = int(limit)
        except:
            return Response(
                json.dumps({'error': 'No string for limit.'}), status=400
            )
        if limit > 50:
            return Response(
                json.dumps({'error': 'Bad data. Limit cannot exceed 20.'}), status=400
            )
        posts = Post.query.filter(Post.user_id.in_(me_and_my_friend_ids)).limit(limit)
        return Response(json.dumps([post.to_dict() for post in posts]), mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        if not body.get('image_url'):
            return Response(json.dumps({'error': 'image_url required'}), status=400)

        new_post = Post(
            image_url=body.get('image_url'),
            user_id=self.current_user.id, 
            caption=body.get('caption'),
            alt_text=body.get('alt_text')
        )
        
        db.session.add(new_post)    
        db.session.commit()   
        return Response(json.dumps(new_post.to_dict()), mimetype="application/json", status=201)
        
class PostDetailEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user
        

    @access_utils.can_modify_or_404
    def patch(self, id):
        '''
        If I want to update a post, what do I do?
        1. Go get the current post. And check if they're authorized.
        2. Update only the items that the user changed
        3. Save to the DB
        4. Return the final representation to the user
        '''
        body = request.get_json()

        post = Post.query.get(id)

    
        if body.get('image_url'):
            post.image_url = body.get('image_url') 
        if body.get('caption'):
            post.caption = body.get('caption')  
        if body.get('alt_text'):
            post.alt_text = body.get('alt_text')  
        db.session.commit() 

        return Response(json.dumps(post.to_dict()), mimetype="application/json", status=200)


    @access_utils.can_modify_or_404
    def delete(self, id):
        Post.query.filter_by(id=id).delete()
        db.session.commit()
        return Response(json.dumps(None), mimetype="application/json", status=200)

    @access_utils.can_view_or_404
    def get(self, id):
        post = Post.query.get(id)

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