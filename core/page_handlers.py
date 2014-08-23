# -*- coding: utf-8 -*-
import urllib2

from core.base import BaseHandler
from core.models import Cargo, Estado


class IndexPage(BaseHandler):

    def get(self):
        result = ''
        estados = []
        cargos = []
        try:
            estados = Estado.query().fetch()
            cargos = Cargo.query().fetch()
            estados = sorted(estados, key=lambda x: x.sigla)
            cargos = sorted(cargos, key=lambda x: x.cargo_id)
        except urllib2.URLError, e:
            result = str(e)

        return self.render('index.html', result=result, estados=estados, cargos=cargos)

    def about(self):
        return self.render('about.html')

    def not_found(self):
        return self.render('404.html')
