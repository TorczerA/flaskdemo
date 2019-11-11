from flask import request
from models.UserTable import UserTable
from flask_restful import Resource


class UserTableTask(Resource):

    def get(self):
        all_rows = UserTable.get_all_users()
        serialized_users = [row.serialize() for row in all_rows]
        # GET ALL USERS
        return {
            'all_users': serialized_users
        }

    def post(self):
        # CREATE ONE USER
        data = request.get_json()
        table_obj = UserTable(data)
        try:
            table_obj.create_user()
        except:

            return {
                "error msg": "Maybe the user already exists, or you are missing the required parameters"
            }

        return UserTableTask.get(self)

    def delete(self):
        data = request.get_json()
        row_id = data.get('id')
        row_obj = UserTable.query.get(row_id)
        if row_obj:
            try:
                row_obj.delete_user()
            except:
                return {
                    "msg": "User still owns posts, so it cannot be deleted!"
                }
        else:
            return {
                "msg": "User with id {} does not exists! Try a different ID".format(row_id)
            }
        return {
            "msg": "User is deleted with id -> {}".format(row_id)
        }
