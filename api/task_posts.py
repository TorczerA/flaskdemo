from flask import request
from models import PostsTable
from flask_restful import Resource
import logging as logger


class PostTableTask(Resource):

    def get(self):
        logger.debug("---Inside Task2 get()---")
        all_rows = PostsTable.get_all_posts()
        serialized_posts = [row.serialize() for row in all_rows]
        # GET ALL POSTS
        return {
            'all_posts': serialized_posts
        }

    def post(self):
        logger.debug("---Inside Task2 post()---")
        # CREATE ONE POST
        data = request.get_json()
        table_obj = PostsTable(data)
        table_obj.create_post()
        return PostTableTask.get(self)

    def put(self):
        logger.debug("---Inside Task2 put()---")
        pass

    def delete(self):
        logger.debug("---Inside Task2 delete()---")
        data = request.get_json()
        row_id = data.get('id')
        row_obj = PostsTable.query.get(row_id)
        row_obj.delete_post()
        return "PostsTable is deleted at id -> {}".format(row_id)
