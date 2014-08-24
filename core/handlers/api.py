# -*- coding: utf-8 -*-

import logging as log
import urllib2

from google.appengine.ext import ndb
from google.appengine.ext import deferred
from webapp2_extras import json

from core import settings
from core.base import BaseHandler, user_required
from core.models import Estado, Partido, Cargo, Candidato


class APIHandler(BaseHandler):

    def load_dados_transparencia(self):
        deferred.defer(load_estados, _queue='loadTransparencia')
        deferred.defer(load_partidos, _queue='loadTransparencia')
        deferred.defer(load_cargos, _queue='loadTransparencia')

    def load_candidatos_transparencia(self):
        deferred.defer(load_candidatos, _queue='loadTransparencia')


def load_estados():
    ndb.delete_multi(
        Estado.query().fetch(keys_only=True)
    )

    try:
        opener = urllib2.build_opener()
        opener.addheaders = [('App-Token', settings.TRANSPARENCIA_TOKEN),
                             ('Content-Type', 'application/json'), ('Accept', 'application/json')]
        result = opener.open(settings.uri('estados'))

        estados = json.decode(result.read())
        for estado in estados:
            Estado(estado_id=int(estado['estadoId']), nome=estado[
                   'nome'], sigla=estado['sigla']).put()
    except urllib2.URLError, e:
        print '>>>>>>>>>>>>>>>>>>>> %s' % str(e)
        pass


def load_partidos():
    ndb.delete_multi(
        Partido.query().fetch(keys_only=True)
    )
    try:
        opener = urllib2.build_opener()
        opener.addheaders = [('App-Token', settings.TRANSPARENCIA_TOKEN),
                             ('Content-Type', 'application/json'), ('Accept', 'application/json')]
        result = opener.open(settings.uri('partidos'))

        partidos = json.decode(result.read())
        for partido in partidos:
            Partido(
                partido_id=int(partido['partidoId']), sigla=partido['sigla']).put()
    except urllib2.URLError, e:
        print '>>>>>>>>>>>>>>>>>>>> %s' % str(e)
        pass


def load_cargos():
    ndb.delete_multi(
        Cargo.query().fetch(keys_only=True)
    )

    try:
        opener = urllib2.build_opener()
        opener.addheaders = [('App-Token', settings.TRANSPARENCIA_TOKEN),
                             ('Content-Type', 'application/json'), ('Accept', 'application/json')]
        result = opener.open(settings.uri('cargos'))

        cargos = json.decode(result.read())
        for cargo in cargos:
            Cargo(cargo_id=int(cargo['cargoId']), nome=cargo['nome']).put()
    except urllib2.URLError, e:
        print '>>>>>>>>>>>>>>>>>>>> %s' % str(e)
        pass


def load_candidatos():
    ndb.delete_multi(
        Candidato.query().fetch(keys_only=True)
    )

    try:
        opener = urllib2.build_opener()
        opener.addheaders = [('App-Token', settings.TRANSPARENCIA_TOKEN),
                             ('Content-Type', 'application/json'), ('Accept', 'application/json')]

        uri = settings.uri('candidatos_by_uf_cargo')

        estados = Estado.query().fetch()
        for estado in estados:
            _load_candidato_by_uf(estado)

    except urllib2.URLError, e:
        print '>>>>>>>>>>>>>>>>>>>> %s' % str(e)
        pass


def _load_candidato_by_uf(estado):
    cargos = Cargo.query().fetch()
    for cargo in cargos:
        try:
            opener = urllib2.build_opener()
            opener.addheaders = [('App-Token', settings.TRANSPARENCIA_TOKEN),
                                 ('Content-Type', 'application/json'), ('Accept', 'application/json')]

            uri = settings.uri('candidatos_by_uf_cargo').format(
                uf=estado.sigla, cargo=cargo.cargo_id)
            result = opener.open(uri)

            candidatos = json.decode(result.read())
            for candidato in candidatos:
                _put_candidate(candidato)

        except urllib2.URLError, e:
            print '>>>>>>>>>>>>>>>>>>>> %s' % str(e)
            pass


def _put_candidate(candidato):
    try:
        opener = urllib2.build_opener()
        opener.addheaders = [('App-Token', settings.TRANSPARENCIA_TOKEN),
                             ('Content-Type', 'application/json'), ('Accept', 'application/json')]

        uri = settings.uri('candidato_stats').format(
            candidato_id=candidato['id'])
        result = opener.open(uri)

        candidato_stats = json.decode(result.read())
        if candidato_stats:
            candidato_stats = candidato_stats[0]
        else:
            candidato_stats = {}

        Candidato(candidato_id=int(candidato['id']), 
                  instrucao=candidato['instrucao'], 
                  reeleicao=candidato['reeleicao'], 
                  cargo=candidato['cargo'],
                  estado=candidato['estado'], 
                  nome=candidato['nome'], 
                  foto=candidato['foto'],
                  faltas_plenario=float(candidato_stats.get('faltas_plen', 0)),
                  faltas_comissoes=float(candidato_stats.get('faltas_com', 0))).put()
    except urllib2.URLError, e:
        print '>>>>>>>>>>>>>>>>>>>> %s' % str(e)
        pass
