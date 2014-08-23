# -*- coding: utf-8 -*-
'''
Created on Sept 26, 2013

@author: Rafael Nunes
'''
from core.base import BaseHandler

from core.models import Voto

class VotadosHandler(BaseHandler):

    def get(self):
        return self.render('show_votados.html')


class VotoHandler(BaseHandler):
	def registrar(self):
		voto = Voto()
		
		voto.usuario = self.logged.email if self.logged else None
		voto.candidato_id = self.request.get('candidato')
		voto.pontos = int(self.request.get('voto'))
		
		voto.put()		
			
		return self.render_json({'success': True })

