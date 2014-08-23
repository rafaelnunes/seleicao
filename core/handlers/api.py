# -*- coding: utf-8 -*-

import logging as log
import urllib2

from google.appengine.ext import deferred
from webapp2_extras import json

from core import settings
from core.base import BaseHandler, user_required
from core.models import Estado, Partido, Cargo

class APIHandler(BaseHandler):

	def load_transparencia(self):
		deferred.defer(load_estados, _queue='loadTransparencia')
		deferred.defer(load_partidos, _queue='loadTransparencia')
		deferred.defer(load_cargos, _queue='loadTransparencia')


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


def load_partidos():
	try:
		opener = urllib2.build_opener()
		opener.addheaders = [('App-Token', settings.TRANSPARENCIA_TOKEN), ('Content-Type', 'application/json'), ('Accept', 'application/json')]
		result = opener.open(settings.uri('partidos'))

		partidos = json.decode(result.read())
		for partido in partidos:
			Partido(partido_id=int(partido['partidoId']), sigla=partido['sigla']).put()
	except urllib2.URLError, e:
		print '>>>>>>>>>>>>>>>>>>>> %s' %str(e)
		pass


def load_cargos():
	try:
		opener = urllib2.build_opener()
		opener.addheaders = [('App-Token', settings.TRANSPARENCIA_TOKEN), ('Content-Type', 'application/json'), ('Accept', 'application/json')]
		result = opener.open(settings.uri('cargos'))

		cargos = json.decode(result.read())
		for cargo in cargos:
			Cargo(cargo_id=int(cargo['cargoId']), nome=cargo['nome']).put()
	except urllib2.URLError, e:
		print '>>>>>>>>>>>>>>>>>>>> %s' %str(e)
		pass
