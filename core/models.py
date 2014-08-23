# -*- coding: utf-8 -*-
'''
Created on Oct 3, 2013

@author: Rafael Nunes
'''
import time
from urlparse import urlparse, parse_qs


from google.appengine.ext import ndb
from google.appengine.ext import blobstore

from webapp2 import uri_for
from webapp2_extras.appengine.auth.models import User as GAEUser
from webapp2_extras import security

from core.base import BaseModel
from core import util

class Estado(BaseModel):
	estado_id = ndb.IntegerProperty()
	sigla = ndb.StringProperty()
	nome = ndb.StringProperty()
	
class Partido(BaseModel):
	partido_id = ndb.IntegerProperty()
	sigla = ndb.StringProperty()
	
class Cargo(BaseModel):
	cargo_id = ndb.IntegerProperty()
	nome = ndb.StringProperty()
	
class Candidato(BaseModel):
	candidato_id = ndb.IntegerProperty()
	cargo = ndb.StringProperty()
	estado = ndb.StringProperty()
	instrucao = ndb.StringProperty()
	reeleicao = ndb.BooleanProperty()
	
	#estatisticas
	faltas_plenario = ndb.FloatProperty()
	faltas_comissoes = ndb.FloatProperty()