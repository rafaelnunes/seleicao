# -*- coding: utf-8 -*-
import webapp2

from core.handlers import api, site
from core.page_handlers import *
from core.base import handle_404
from core.template_filters import get_filters

from core.handlers.candidatos import CandidatosHandler
from core.handlers.profile import *

from core.handlers.votados import *

routes = [
    ('/', IndexPage), 
    ('/profile', ProfileHandler), 
    ('/votados', VotadosHandler)
]

routes += [
	webapp2.Route(r'/not-found', handler=IndexPage, handler_method='not_found', name='not_found'),
	webapp2.Route('/api/load_dados_transparencia', handler=api.APIHandler, handler_method='load_dados_transparencia', name='load_dados_transparencia'),
	webapp2.Route('/api/load_candidatos_transparencia', handler=api.APIHandler, handler_method='load_candidatos_transparencia', name='load_candidatos_transparencia'),
	webapp2.Route('/api/load_transparencia', handler=api.APIHandler, handler_method='load_transparencia', name='load_transparencia'),
    webapp2.Route('/login', handler=site.SiteHandler, handler_method='login', name='login'),
    webapp2.Route('/logout', handler=site.SiteHandler, handler_method='logout', name='logout'),
    webapp2.Route('/register', handler=site.SiteHandler, handler_method='register', name='register'),
    webapp2.Route('/candidatos', handler=CandidatosHandler, handler_method='filter_candidatos', name='filter_candidatos'),
    webapp2.Route('/votar', handler=VotoHandler, handler_method='registrar', name='registrar_voto')
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