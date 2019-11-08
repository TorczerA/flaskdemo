from flask import request
from models import UserTable
from flask_restful import Resource
import logging as logger


class UserTableTask(Resource):

    def get(self):
        logger.debug("---Inside task_users get()---")
        all_rows = UserTable.get_all_users()
        serialized_users = [row.serialize() for row in all_rows]
        # GET ALL USERS
        return {
            'all_users': serialized_users
        }

    def post(self):
        logger.debug("---Inside task_users post()---")
        # CREATE ONE USER
        data = request.get_json()
        table_obj = UserTable(data)
        try:
            table_obj.create_user()
        except:
            return {
                "error msg": "First Name cannot be null, please provide a first_name!"
            }
        return UserTableTask.get(self)

    def put(self):
        logger.debug("---Inside task_users put()---")

    def delete(self):
        logger.debug("---Inside task_users delete()---")
        data = request.get_json()
        row_id = data.get('id')
        row_obj = UserTable.query.get(row_id)
        if row_obj:
            row_obj.delete_user()
        else:
            return {
                "msg": "User with id {} does not exists! Try a different ID".format(row_id)
            }
        return {
            "msg": "User is deleted with id -> {}".format(row_id)
        }
