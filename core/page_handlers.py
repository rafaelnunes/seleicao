# -*- coding: utf-8 -*-
import urllib2

from core.base import BaseHandler
from core.models import Estado


class IndexPage(BaseHandler):

    def get(self):
        result = ''
        estados = []
        try:
            estados = Estado.query().fetch()
            estados = sorted(estados, key=lambda x: x.sigla)
        except urllib2.URLError, e:
            result = str(e)

        return self.render('index.html', result=result, estados=estados)

    def about(self):
        return self.render('about.html')

    def not_found(self):
        return self.render('404.html')
