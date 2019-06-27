from flask import Flask, session, request
from flask_restplus import fields, Resource, Api, reqparse
import re
import datetime
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'
api = Api(app)

# ask_req_fields = api.model('AskReqFields', {
#     'sid': fields.String(required=True, description='The session ID of the message'),
#     'question': fields.String(required=True, description='The question that should be answered'), 
#     'debug': fields.Boolean(default=False, description='The debug mode for getting extra parameters from the answer'), 
#     'google_search': fields.Boolean(default=True, description='By setting to false, will not search google anymore')
# })

# sentiment_req_fields = api.model('Sentiment', {
#     'q': fields.String(required=True, description='The user conversations')
# })