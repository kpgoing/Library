# coding=utf-8
from flask import jsonify
class ResponseBody(object):
    def __init__(self,status,body):
        self.content = {'status':status,'body':body}
    def getContent(self):
        return jsonify(self.content)