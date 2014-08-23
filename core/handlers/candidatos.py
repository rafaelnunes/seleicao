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
from core.models import Partido, Candidato

from core import settings
import urllib2

class CandidatosHandler(BaseHandler):
	def filter_candidatos(self):	
		estado = self.request.get('estado')
		cargo = self.request.get('cargo')
		reeleicao = self.request.get('reeleicao')
		media_sessoes = self.request.get('media_sessoes')
		media_comissoes = self.request.get('media_comissoes')
		
		json_response = []
		candidatos_db = Candidato.query().fetch()
				
		candidatos = Candidato.query(Candidato.estado == estado, 
				# Candidato.cargo == cargo, 
				# Candidato.reeleicao == reeleicao,
				# Candidato.media_sessoes <= media_sessoes,
				# Candidato.media_comissoes <= media_comissoes
				).fetch()

		candidatos = [candidato.to_dict() for candidato in candidatos]

		return self.render('show_candidatos.html', candidatos=candidatos)