from flask import request
from models import PostsTable
from flask_restful import Resource
import logging as logger


class PostTableTask(Resource):

    def get(self):
        logger.debug("---Inside task_posts get()---")
        all_rows = PostsTable.get_all_posts()
        serialized_posts = [row.serialize() for row in all_rows]
        # GET ALL POSTS
        return {
            'all_posts': serialized_posts
        }

    def post(self):
        logger.debug("---Inside task_posts post()---")
        # CREATE ONE POST
        data = request.get_json()
        table_obj = PostsTable(data)
        try:
            table_obj.create_post()
        except:
            return {
                "error msg": "Title cannot be null, please provide a title!"
            }
        return PostTableTask.get(self)


    def put(self):
        logger.debug("---Inside task_posts put()---")
        pass

    def delete(self):
        logger.debug("---Inside task_posts delete()---")
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
