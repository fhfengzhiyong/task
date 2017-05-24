# -*- coding: utf-8 -*-
# -*- __author__=straw -*-

from flask import render_template, Blueprint
from flask import current_app,g,request
# from apps import db
from models import Task
from config.db import DBSession

"""
任务核心控制类
"""

'''
使用分页查看工作列表
'''

task = Blueprint("task",  __name__, template_folder="../templates/task")


@task.route("/listTask")
def list_task(page=1):
    pagination = Task.query().order_by(Task.desc(Task.create_time).paginate(page, current_app.config['POSTS_PER_PAGE'], False))
    # db.Query.order_by(db.desc())
    return render_template("listTask.html", pagination=pagination)


'''
跳转到添加任务页面
'''


@task.route("/")
def add_task():
    return render_template("addTask.html")
