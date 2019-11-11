from flask import request
from flask_restful import Resource
from models.PostsTable import PostsTable


class PostTableTask(Resource):

    def get(self):
        all_rows = PostsTable.get_all_posts()
        serialized_posts = [row.serialize() for row in all_rows]
        # GET ALL POSTS
        return {
            'all_posts': serialized_posts
        }

    def post(self):
        # CREATE ONE POST
        data = request.get_json()
        table_obj = PostsTable(data)
        try:
            table_obj.create_post()
        except:
            return {
                "error msg": "Title cannot be null and user id should match existing user, please check again!"
            }
        return PostTableTask.get(self)

    def delete(self):
        data = request.get_json()
        row_id = data.get('id')
        row_obj = PostsTable.query.get(row_id)
        if row_obj:
            row_obj.delete_post()
        else:
            return {
                "msg": "Post with id {} does not exists! Try a different ID".format(row_id)
            }
        return {
            "msg": "PostsTable is deleted with id -> {}".format(row_id)
        }
