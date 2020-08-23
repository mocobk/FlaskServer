#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : user.py
# @Author : mocobk
# @Email  : mailmzb@qq.com
# @Time   : 2020/5/25 20:04

from flask import Blueprint, g

from app.libs.flask_restful import Api, Resource
from app.libs.response import Success
from app.models.user import User, UserSchema

blueprint = Blueprint('user', __name__)

api = Api(blueprint)

@api.resource('/info')
class UserResource(Resource):

    def get(self):
        user = User.query.get(g.user.uid)
        data = UserSchema().dump(user)
        return Success(data=data)
