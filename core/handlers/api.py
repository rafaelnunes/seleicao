# -*- coding: utf-8 -*-

import logging as log
import urllib2

from google.appengine.ext import deferred
from webapp2_extras import json

from core import settings
from core.base import BaseHandler, user_required
from core.models import Estado

class APIHandler(BaseHandler):

	def load_transparencia(self):
		deferred.defer(load_estados, _queue='loadTransparencia')
		deferred.defer(load_partidos, _queue='loadTransparencia')


def load_estados():
	try:
		opener = urllib2.build_opener()
		opener.addheaders = [('App-Token', settings.TRANSPARENCIA_TOKEN), ('Content-Type', 'application/json'), ('Accept', 'application/json')]
		result = opener.open(settings.uri('estados'))

		estados = json.decode(result.read())
		for estado in estados:
			Estado(estado_id=int(estado['estadoId']), nome=estado['nome'], sigla=estado['sigla']).put()
	except urllib2.URLError, e:
		print '>>>>>>>>>>>>>>>>>>>> %s' %str(e)
		pass

def load_partidos(self):
	try:
		opener = urllib2.build_opener()
		opener.addheaders = [('App-Token', settings.TRANSPARENCIA_TOKEN), ('Content-Type', 'application/json'), ('Accept', 'application/json')]
		result = opener.open(settings.uri('partidos'))

		estados = json.decode(result.read())
		for partido in partidos:
			Partido(partido_id=int(partido['partidoId']), sigla=estado['sigla']).put()
	except urllib2.URLError, e:
		print '>>>>>>>>>>>>>>>>>>>> %s' %str(e)
		pass
