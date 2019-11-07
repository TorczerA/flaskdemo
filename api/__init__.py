from flask_restful import Api
from app import flaskAppInstance
from .task_users import UserTableTask
from .task_posts import PostTableTask

restServer = Api(flaskAppInstance)

restServer.add_resource(UserTableTask, "/api/v1/users")
restServer.add_resource(PostTableTask, "/api/v1/posts")
