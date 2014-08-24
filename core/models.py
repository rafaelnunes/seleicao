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
	
class Voto(BaseModel):
	usuario = ndb.StringProperty()
	candidato_id = ndb.StringProperty()
	pontos = ndb.IntegerProperty()
		
class Candidato(BaseModel):
    candidato_id = ndb.IntegerProperty()
    nome = ndb.StringProperty()
    foto = ndb.StringProperty()
    cargo = ndb.StringProperty()
    estado = ndb.StringProperty()
    instrucao = ndb.StringProperty()
    reeleicao = ndb.BooleanProperty()
    processor = ndb.BooleanProperty()

    #estatisticas
    faltas_plenario = ndb.FloatProperty()
    faltas_comissoes = ndb.FloatProperty()


class UserProfile(GAEUser):

    def set_password(self, raw_password):
        self.password = security.generate_password_hash(raw_password, length=12)
 
    @classmethod
    def get_by_auth_token(cls, user_id, token, subject='auth'):
        """Returns a user object based on a user ID and token.
     
        :param user_id:
            The user_id of the requesting user.
        :param token:
            The token string to be verified.
        :returns:
            A tuple ``(User, timestamp)``, with a user object and
            the token timestamp, or ``(None, None)`` if both were not found.
        """
        token_key = cls.token_model.get_key(user_id, subject, token)
        user_key = ndb.Key(cls, user_id)
        # Use get_multi() to save a RPC call.
        valid_token, user = ndb.get_multi([token_key, user_key])

        if valid_token and user:
            timestamp = int(time.mktime(valid_token.created.timetuple()))
            return user, timestamp
     
        return None, None

    @property
    def email(self):
        return self.email_address

    def get_name_or_email(self):
        if not self.name:
            return self.email_address

        return self.name
