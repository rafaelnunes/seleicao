# -*- coding: utf-8 -*-
'''
Created on Sept 26, 2013

@author: Rafael Nunes
'''
import logging as log
from webapp2 import redirect_to, redirect
from google.appengine.api import images
from google.appengine.ext.webapp import blobstore_handlers

from core.base import BaseHandler, user_required
from core.models import Partido

class VotoNeutroHandler(BaseHandler):
	def get(self):		
		voto = Voto()
		
		voto.usuario = self.request.get('usuario')
		voto.candidato_id = self.request.get('id')
		voto.pontos = 0
	
		voto.put()		
			
		return self.render_json({'success': True })
		