from flask import Response, request
from flask_restful import Resource
from models import Bookmark, db
import json

class BookmarksListEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user
    
    def get(self):
        # get all bookmarks owned by the current user
         bookmarks = Bookmark.query.filter_by(user_id=self.current_user.id).all()

        #return Response(json.dumps([]), mimetype="application/json", status=200)
        return Response(json.dumps([bookmark.to_dict() for bookmark in bookmarks]), mimetype="application/json", status=200)

    def post(self):
        # create a new "bookmark" based on the data posted in the body 
        body = request.get_json()
        print(body)
        #return Response(json.dumps({}), mimetype="application/json", status=201)
          try:
            post_id = int(body.get('post_id'))
        except:
            return Response(json.dumps({'error': 'unauthorized'}), status=400)
        post = Post.query.get(post_id)
        authorized_ids = get_authorized_user_ids(current_user=self.current_user)
        
        if post == None:
            return Response(json.dumps({ "error": "unauthorized" }), mimetype="application/json", status=404)

        if post.user_id not in authorized_ids:
            return Response(json.dumps({ "error": "unauthorized" }), mimetype="application/json", status=404)

        new_bookmark = Bookmark(
            user_id=self.current_user.id,
            post_id=body.get('post_id'),
        )
        try:
            db.session.add(new_bookmark)
            db.session.commit()
        except:
            return Response(json.dumps({ "error": "duplicate post_id" }), mimetype="application/json", status=400)

        return Response(json.dumps(new_bookmark.to_dict()), mimetype="application/json", status=201)
 

class BookmarkDetailEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user
    
    def delete(self, id):
        # delete "bookmark" record where "id"=id
        print(id)
        #return Response(json.dumps({}), mimetype="application/json", status=200)
         try:
            id = int(id)
        except:
            return Response(json.dumps({'error': 'unauthorized'}), status=404)

        bookmark = Bookmark.query.get(id)

        if bookmark == None or bookmark.user_id != self.current_user.id:
            return Response(json.dumps({ "error": "unauthorized" }), mimetype="application/json", status=404)

        Bookmark.query.filter_by(id=id).delete()
        db.session.commit()

        return Response(json.dumps(None), mimetype="application/json", status=200)




def initialize_routes(api):
    api.add_resource(
        BookmarksListEndpoint, 
        '/api/bookmarks', 
        '/api/bookmarks/', 
        resource_class_kwargs={'current_user': api.app.current_user}
    )

    api.add_resource(
        BookmarkDetailEndpoint, 
        '/api/bookmarks/<int:id>', 
        '/api/bookmarks/<int:id>',
        resource_class_kwargs={'current_user': api.app.current_user}
    )
