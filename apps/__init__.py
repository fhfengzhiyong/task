# -*- coding: utf-8 -*-
# -*- __author__=straw -*-
from flask import Flask

# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config.from_pyfile('../config/setting.py')
# db = SQLAlchemy(app)


from apps.task.views import task

'''
程序启动配置
'''





def create_app():
    app.config.from_pyfile('../config/setting.py')
    app.debug = app.config['DEBUG']
    # 增加一个蓝图

    app.register_blueprint(task,  url_prefix="/task")

    return app


def init():
    app = create_app()
    app.run(debug=app.debug, host='127.0.0.1', port=5001)
