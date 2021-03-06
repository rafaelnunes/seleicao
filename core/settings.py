# -*- coding: utf-8 -*-
'''
Created on Sept 26, 2013

@author: Rafael Nunes
'''

HOST_NAME = 'http://projetootimizei.appspot.com'
EMAIL_SENDER = 'Otimizei<otimizeiconsultoriaweb@gmail.com>'

TRANSPARENCIA_API = 'http://api.transparencia.org.br/api/v1'
TRANSPARENCIA_TOKEN = 'Pesjr4Qtq9jZ'


TRANSPARENCIA_URIS = {
	'estados': '/estados',
	'partidos': '/partidos',
	'cargos': '/cargos',
	'candidatos': '/candidatos',
	'candidatos_by_uf_cargo': '/candidatos?estado={uf}&cargo={cargo}',
	'candidato_stats': '/candidatos/{candidato_id}/estatisticas',
}


def uri(name):
	return '%s%s' %(TRANSPARENCIA_API, TRANSPARENCIA_URIS[name])