# -*- coding: utf-8 -*-

import logging as log
import urllib2

from google.appengine.ext import deferred

from core import settings
from core.base import BaseHandler, user_required

class APIHandler(BaseHandler):

	def load_transparencia(self):
		deferred.defer(load_estado, _queue='loadTransparencia')


def load_estado():
	try:
		opener = urllib2.build_opener()
		opener.addheaders = [('App-Token', settings.TRANSPARENCIA_TOKEN), ('Content-Type', 'application/json'), ('Accept', 'application/json')]
		result = opener.open(settings.TRANSPARENCIA_API).read()
	except urllib2.URLError, e:
		pass