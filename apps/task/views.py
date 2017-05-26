# -*- coding: utf-8 -*-
# -*- __author__=straw -*-

from flask import render_template, Blueprint, redirect
from flask import current_app,g,request
from models import Task
from config.db import Session

"""
任务核心控制类
"""

'''
使用分页查看工作列表
'''

task = Blueprint("task",  __name__, template_folder="../templates/task")


@task.route("/listTask")
def list_task(page=1):
    session = Session()
    pagination = session.query(Task).order_by(Task.create_time)[0:10]
    session.close()
    # db.Query.order_by(db.desc())
    return render_template("listTask.html", pagination=pagination)


'''
跳转到添加任务页面
'''


@task.route("/")
def to_add_task():
    return render_template("addTask.html")


@task.route("/addTask", methods=['POST'])
def add_task():
    form = request.form
    task = Task()
    task.content = form.get('content')
    task.work_time = form.get("work_time")
    task.complete_rate = form.get("complete_rate")
    session = Session()
    session.add(task)
    session.commit()
    session.close()
    return redirect(location='/task')


@task.route("/delete/<ids>", methods=['GET'])
def del_task(ids):
    session = Session()
    t = session.query(Task).filter_by(id=ids)[0]
    session.delete(t)
    session.commit()
    session.close()
    return redirect(location='/task/listTask')