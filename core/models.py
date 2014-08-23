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
	apelido = ndb.StringProperty()
	nome = ndb.StringProperty()
	numero = ndb.IntegerProperty()
	titulo = ndb.IntegerProperty()
	cpf = ndb.IntegerProperty()
	matricula = ndb.IntegerProperty()
	cargo = ndb.StringProperty()
	estado = ndb.StringProperty()
	partido = ndb.StringProperty()
	idade = ndb.IntegerProperty()
	instrucao = ndb.StringProperty()
	ocupacao = ndb.StringProperty()
	mini_bio = ndb.StringProperty()
	cargos = ndb.StringProperty()
	previsao = ndb.FloatProperty()
	bancadas = ndb.StringProperty()
	processos = ndb.StringProperty()
	casa_atual = ndb.IntegerProperty()
	reeleicao = ndb.BooleanProperty()
	foto = ndb.StringProperty()
	
	#candidaturas
	candidaturas = ndb.IntegerProperty()
	
	#estatisticas
	faltas_plenario = ndb.FloatProperty()
	media_plenario = ndb.FloatProperty()
	faltas_comissoes = ndb.FloatProperty()
	media_comissoes = ndb.FloatProperty()
	evolucao = ndb.FloatProperty()
	ano_referencia = ndb.IntegerProperty()
	emendas = ndb.FloatProperty()
	media_emendas = ndb.FloatProperty()


class UserProfile(GAEUser):
    APP_USER = 0
    GOOGLE_USER = 1
    FACEBOOK_USER = 2

    TYPE_STUDENT = 0
    TYPE_ADMIN = 1
    TYPE_STAFF = 2

    TYPE_CHOICES = {
        TYPE_STUDENT: 'Estudante',
        TYPE_ADMIN: 'Admin',
        TYPE_STAFF: 'Staff',
    }

    gplus_user = ndb.StringProperty()
    fcbk_user = ndb.StringProperty()

    login_type = ndb.IntegerProperty(default=APP_USER)
    avatar = ndb.BlobKeyProperty()
    about = ndb.TextProperty()
    website = ndb.StringProperty()
    fcbk_url = ndb.StringProperty()
    tw_url = ndb.StringProperty()
    gplus_url = ndb.StringProperty()

    followed_courses = ndb.KeyProperty(kind='Subject', repeated=True)

    settings = ndb.JsonProperty()

    user_type = ndb.IntegerProperty(default=TYPE_STUDENT)

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

    @property
    def short_about(self):
        return self.about or ""

    @property
    def full_name(self):
        return '%s %s' %(self.name, self.last_name)

    @property
    def short_about(self):
        short = ''
        if self.about:
            short = self.about[:50] + '...'

        return short

    def get_name_or_email(self):
        if not self.name:
            return self.email_address

        return self.name

    def is_app_profile(self):
        return self.login_type == self.APP_USER

    def is_google_profile(self):
        return self.login_type == self.GOOGLE_USER

    def is_facebook_profile(self):
        return self.login_type == self.FACEBOOK_USER

    def get_subjects(self):
        return Subject.query(Subject.owner == self.key).fetch()

    def get_followed_courses(self):
        if not self.followed_courses or not self.followed_courses[0]:
            return [] 

        return [k.get() for k in self.followed_courses if k.get()  and k.get() not in self.get_subjects()]

    def get_my_courses(self):
        return self.get_subjects() + self.get_followed_courses()

    def is_following(self, subject):
        return subject.key in self.followed_courses

    def has_setting(self, name):
        settings = self.settings or {}
        return (name in settings.keys()) and settings[name] == 'true'

    def get_setting(self, setting_name):
        if not self.settings:
            return None

        return self.settings.get(setting_name, None)

    def is_admin(self):
        return self.user_type == self.TYPE_ADMIN

    def is_staff(self):
        return self.user_type == self.TYPE_STAFF

    def is_student(self):
        return self.user_type == self.TYPE_STUDENT
