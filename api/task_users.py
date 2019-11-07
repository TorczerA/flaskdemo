from flask import request
from models import UserTable
from flask_restful import Resource
import logging as logger


class UserTableTask(Resource):

    def get(self):
        logger.debug("---Inside Task get()---")
        all_rows = UserTable.get_all_users()
        serialized_users = [row.serialize() for row in all_rows]
        # GET ALL USERS
        return {
            'all_users': serialized_users
        }

    def post(self):
        logger.debug("---Inside Task post()---")
        # CREATE ONE USER
        data = request.get_json()
        table_obj = UserTable(data)
        table_obj.create_user()
        return UserTableTask.get(self)

    def put(self):
        logger.debug("---Inside Task put()---")

    def delete(self):
        logger.debug("---Inside Task delete()---")
        data = request.get_json()
        row_id = data.get('id')
        row_obj = UserTable.query.get(row_id)
        row_obj.delete_user()
        return "User is deleted at id -> {}".format(row_id)