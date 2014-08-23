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
		instrucao = self.request.get('instrucao')
		
		json_response = []
		candidatos_db = Candidato.query().fetch()
				
		grau = {"ENSINO FUNDAMENTAL INCOMPLETO":1,		
		"ENSINO FUNDAMENTAL COMPLETO": 2, 
		"ENSINO MÉDIO INCOMPLETO": 3,
		"ENSINO MÉDIO COMPLETO": 4,
		"SUPERIOR INCOMPLETO": 5,
		"SUPERIOR COMPLETO": 6	
		}
		
		candidatos = Candidato.query(Candidato.estado == estado, 
				# Candidato.cargo == cargo, 
				# Candidato.reeleicao == reeleicao,
				# Candidato.media_sessoes <= media_sessoes,
				# Candidato.media_comissoes <= media_comissoes,
				# grau[Candidato.instrucao] >= instrucao
				).fetch()

		candidatos = [candidato.to_dict() for candidato in candidatos]

		return self.render('show_candidatos.html', candidatos=candidatos)