from flask import Flask, session, request
from flask_restplus import fields, Resource, Api, reqparse
import re
import datetime
import os
from Helper import *
from TopicModel import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'
api = Api(app)
helper = Helper()
tm = TopicModel('model/model.p', 'model/dictionary.p')


# ask_req_fields = api.model('AskReqFields', {
#     'sid': fields.String(required=True, description='The session ID of the message'),
#     'question': fields.String(required=True, description='The question that should be answered'), 
#     'debug': fields.Boolean(default=False, description='The debug mode for getting extra parameters from the answer'), 
#     'google_search': fields.Boolean(default=True, description='By setting to false, will not search google anymore')
# })

sentiment_req_fields = api.model('SentimentReqFields', {
    'text': fields.String(required=True, description='The user conversations'), 
    'uid': fields.String(required=True, description='The user ID')
})

unhappy_req_fields = api.model('UnhappyReqFields', {
    'max': fields.Float(default=0.0, description='The maximum sentiment value')
})