# -*- coding: utf-8 -*-
'''
Created on Sept 26, 2013

@author: Rafael Nunes
'''
from core.base import BaseHandler
from core.models import Partido, Voto

class VotadosHandler(BaseHandler):

    def get(self):
		
	usuario = self.logged
	
	votaria_ids = Voto.query(Voto.usuario == usuario, Voto.pontos == 1).fetch()
	
	nao_votaria_ids = Voto.query(Voto.usuario == usuario, Voto.pontos == -1).fetch()
	
	talvez_votaria_ids = Voto.query(Voto.usuario == usuario, Voto.pontos == 0).fetch()
	
	votaria = ndb.get_multi([ndb.Key(Voto, k) for k in votaria_ids])
	
	nao_votaria = ndb.get_multi([ndb.Key(Voto, k) for k in nao_votaria_ids])

	talvez_votaria = ndb.get_multi([ndb.Key(Voto, k) for k in talvez_votaria_ids])
	
	#votaria = Candidato.query(Candidato.estado == estado, 				
				# ndb.AND(cargo!="",Candidato.cargo == cargo), 
				# ndb.AND(reeleicao!="",Candidato.reeleicao == reeleicao),
				# ndb.AND(faltas_sessoes!="",Candidato.faltas_sessoes <= faltas_sessoes),
				# ndb.AND(faltas_comissoes!="",Candidato.faltas_comissoes <= faltas_comissoes),
				# ndb.AND(instrucao!="", grau[Candidato.instrucao] >= instrucao),
				# ndb.AND(processos!="", Candidato.processos == processos),				
	#			).fetch()
	
        return self.render('show_votados.html', votaria=votaria, nao_votaria=nao_votaria, talvez_votaria=talvez_votaria)
