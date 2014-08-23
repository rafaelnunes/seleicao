# -*- coding: utf-8 -*-
'''
Created on Sept 26, 2013

@author: Rafael Nunes
'''


import webapp2

from core.page_handlers import *
from core.handlers import dashboard, subjects, classes, site, profile, calendar, inbox, search, config, api
from core.base import handle_404
from core.template_filters import get_filters

routes = [('/', IndexPage),

]

myconfig = {
	'webapp2_extras.auth': {
    'user_model': 'core.models.UserProfile',
    'user_attributes': ['name', 'email_address'],
  },
  'webapp2_extras.sessions': {
    'secret_key': 'YOUR_SECRET_KEY' #TODO change secret key
  }
}

myconfig['webapp2_extras.jinja2'] =  {'template_path': ['templates'],
                                      'filters': get_filters()}

app = webapp2.WSGIApplication(routes, debug=True, config = myconfig)
app.error_handlers[404] = handle_404