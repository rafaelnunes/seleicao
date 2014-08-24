# -*- coding: utf-8 -*-
'''
Created on Sept 26, 2013

@author: Rafael Nunes
'''
from core.base import BaseHandler
from core.models import Voto, Candidato


class VotadosHandler(BaseHandler):

    def get(self):
        usuario = self.logged

        votaria_ids = Voto.query(
            Voto.usuario == usuario.email_address, Voto.pontos == 1).fetch()

        nao_votaria_ids = Voto.query(
            Voto.usuario == usuario.email_address, Voto.pontos == -1).fetch()

        talvez_votaria_ids = Voto.query(
            Voto.usuario == usuario.email_address, Voto.pontos == 0).fetch()

        votaria = [Candidato.query(
            Candidato.candidato_id == int(k.candidato_id)).fetch()[0] for k in votaria_ids]

        nao_votaria = [Candidato.query(Candidato.candidato_id == int(
            k.candidato_id)).fetch()[0] for k in nao_votaria_ids]

        talvez_votaria = [Candidato.query(Candidato.candidato_id == int(
            k.candidato_id)).fetch()[0] for k in talvez_votaria_ids]

        return self.render('show_votados.html', votaria=votaria, nao_votaria=nao_votaria, talvez_votaria=talvez_votaria)


class VotoHandler(BaseHandler):

    def registrar(self):
        voto = Voto()

        voto.usuario = self.logged.email if self.logged else None
        voto.candidato_id = self.request.get('candidato')
        voto.pontos = int(self.request.get('voto'))

        voto.put()

        return self.render_json({'success': True})
