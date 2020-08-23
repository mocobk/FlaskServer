#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : user.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/1/8 14:39

from flask import Blueprint

from app.libs.flask_restful import Api, Resource
from app.libs.response import Success
from app.models.user import User, UserSchema

blueprint = Blueprint('users', __name__)

api = Api(blueprint)


@api.resource('')
class UsersResource(Resource):

    def get(self):
        users = User.query.all()
        data = UserSchema(many=True).dump(users)
        return Success(data=data)


@api.resource('/<uid>')
class UserResource(Resource):

    def get(self, uid):
        user = User.query.get_or_404(uid)
        data = UserSchema().dump(user)
        return Success(data=data)

