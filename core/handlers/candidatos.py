# -*- coding: utf-8 -*-
'''
Created on Sept 26, 2013

@author: Rafael Nunes
'''
import logging as log
from webapp2 import redirect_to, redirect
from google.appengine.api import images
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext import ndb

from core.base import BaseHandler, user_required
from core.models import Partido, Candidato

from core import settings
import urllib2


class CandidatosHandler(BaseHandler):

    def filter_candidatos(self):
        estado = self.request.get('estado')
        cargo = self.request.get('cargo')
        reeleicao = self.request.get('reeleicao')
        faltas_sessoes = self.request.get('faltas_sessoes')
        faltas_comissoes = self.request.get('faltas_comissoes')
        instrucao = self.request.get('instrucao')
        processos = self.request.get('processos')

        grau = {"ENSINO FUNDAMENTAL INCOMPLETO": 1,
                "ENSINO FUNDAMENTAL COMPLETO": 2,
                "ENSINO MÉDIO INCOMPLETO": 3,
                "ENSINO MÉDIO COMPLETO": 4,
                "SUPERIOR INCOMPLETO": 5,
                "SUPERIOR COMPLETO": 6
                }

        candidatos = Candidato.query().filter(
            ndb.AND(Candidato.estado == estado),
            ndb.AND(Candidato.cargo == cargo),
            ndb.AND(Candidato.reeleicao == bool(reeleicao)),
        ).fetch()

        return self.render('show_candidatos.html', candidatos=candidatos)
