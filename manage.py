from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models import db
from app import flaskAppInstance

migrate = Migrate(app=flaskAppInstance, db=db)
manager = Manager(app=flaskAppInstance)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
