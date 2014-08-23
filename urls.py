# -*- coding: utf-8 -*-
import webapp2

from core.handlers import api
from core.page_handlers import *
from core.base import handle_404
from core.template_filters import get_filters

routes = [('/', IndexPage),

]

routes += [
	webapp2.Route(r'/not-found', handler=IndexPage, handler_method='not_found', name='not_found'),
	webapp2.Route('/api/load_transparencia', handler=api.APIHandler, handler_method='load_transparencia', name='load_transparencia')
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