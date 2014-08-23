# -*- coding: utf-8 -*-
'''
Created on Sept 26, 2013

@author: Rafael Nunes
'''
from core.base import BaseHandler


class VotadosHandler(BaseHandler):

    def get(self):
        return self.render('show_votados.html')
