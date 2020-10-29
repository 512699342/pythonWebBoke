from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from models import db
# 这里 import 具体的 Model 类是为了给 migrate 用
# 如果不 import 那么无法迁移
# 这是 SQLAlchemy 的机制
from models.user import User
from models.boke import Boke
from models.comment import Comment
from models.node import Node
from models.tag import Tag
from models.reply import Reply
from models.star import Star
from models.see import See


app = Flask(__name__)
db_path = 'boke.sqlite'
manager = Manager(app)


def register_routes(app):       # impoet路由文件的蓝图，并且注册
    # from routes.todo import main as routes_todo
    from routes.boke import main as routes_boke
    from routes.auth import main as routes_auth
    from routes.comment import main as routes_comment
    from routes.user import main as routes_user
    from routes.api import main as routes_api

    app.register_blueprint(routes_auth, url_prefix='/auth')
    app.register_blueprint(routes_boke, url_prefix='/boke')
    app.register_blueprint(routes_comment, url_prefix='/comment')
    app.register_blueprint(routes_user, url_prefix='/user')
    app.register_blueprint(routes_api, url_prefix='/api')


def configure_app():
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.secret_key = 'secret key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_path)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pwd@localhost/boke'
    db.init_app(app)
    register_routes(app)


def configured_app():
    configure_app()
    return app


# 自定义的命令行命令用来运行服务器
@manager.command
def server():
    print('server run')
    # app = configured_app()
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=3000,
    )
    app.run(**config)


def configure_manager():
    """
    这个函数用来配置命令行选项
    """
    Migrate(app, db)
    manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    configure_manager()
    configure_app()
    manager.run()

# gunicorn -b '0.0.0.0:80' redischat:app
