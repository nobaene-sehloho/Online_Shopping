import os
import unittest
import connexion
from flask_migrate import Migrate, MigrateCommand
from flask_login import current_user, login_user, login_manager, LoginManager, logout_user

from flask_script import Manager
from app.main.model import blacklist

from app.main import create_app, db

from app import blueprint

#1. Imported the home blueprint from home package in vews folder
from app.main.views.home import home
from app.main.views.profile import profile
from app.main.views.items import items


app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

app.register_blueprint(blueprint)

#2. Now register your above imported blueprints in the main app
app.register_blueprint(home)
app.register_blueprint(profile)
app.register_blueprint(items)

#login Manager to use the login/logout functions/methods
login_manager = LoginManager()
login_manager.init_app(app)


app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run()

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
