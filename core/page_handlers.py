# -*- coding: utf-8 -*-
import datetime
import urllib2

from core.base import BaseHandler
from core import settings



class IndexPage(BaseHandler):
    def get(self):
		result = ''
		try:
			opener = urllib2.build_opener()
			opener.addheaders = [('App-Token', settings.TRANSPARENCIA_TOKEN), ('Content-Type', 'application/json'), ('Accept', 'application/json')]
			result = opener.open(settings.TRANSPARENCIA_API)
		except urllib2.URLError, e:
			result = str(e)

		return self.render('index.html', result=result)

    def about(self):
    	return self.render('about.html')

