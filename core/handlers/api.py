# -*- coding: utf-8 -*-
'''
Created on Sept 26, 2013

@author: Rafael Nunes
'''
import logging as log

from core import settings
from core.base import BaseHandler, user_required
from core.models import Subject

class APIHandler(BaseHandler):

	def get_courses(self):
		all_courses = Subject.query().fetch()
		
		#Format to JSON
		all_classes = []
		for course in all_courses:
		  for clazz in course.get_classes():
		    as_json = clazz.to_dict(ignore=['videos', 'materials', 'resources', 'comments'])
		    as_json['videos'] = [video.to_dict() for video in clazz.videos]
		    as_json['materials'] = [{'title': material.title, 'url': settings.HOST_NAME + material.get_download_url()} for material in clazz.materials]
		    as_json['resources'] = [resource.to_dict() for resource in clazz.resources]
		    all_classes.append(as_json)
		    
		
		all_courses = [course.to_dict() for course in all_courses]
		
		

		return self.render_json({'success': True, 'courses': all_courses, 'classes': all_classes})

















	# CHECKLIST
	def get_cadastro_mobile(self):
	    cadastro = {
	      'tipoAvaria': [
		{'id': 1, 'desc': 'Amasado'}, {'id': 2, 'desc': 'Arranhado'}, {'id': 3, 'desc': 'Rasgado'}, {'id': 4, 'desc': 'Sujo'}, {'id': 5, 'desc': 'Quebrado'}, {'id': 6, 'desc': 'PT'}
	      ],
	      'tipoVeiculo':[
		{'id': 1, 'desc': 'Automoveis'}, {'id': 2, 'desc': 'Cavalo Mecanico'}, {'id': 3, 'desc': 'Utilitario'}, 
	      ],
	      'itemVerificacao': [
		{'id': 1, 'desc': 'Pneus', 'fotoObrigatoria': True, 'tipoVeiculo': 1}, {'id': 2, 'desc': 'Parabrisas', 'fotoObrigatoria': True, 'tipoVeiculo': 1}, 
		{'id': 3, 'desc': 'Estofamento', 'fotoObrigatoria': True, 'tipoVeiculo': 1}, {'id': 4, 'desc': 'Chassi', 'fotoObrigatoria': True, 'tipoVeiculo': 1},
		{'id': 5, 'desc': 'Rastreador', 'fotoObrigatoria': False, 'tipoVeiculo': 1}, {'id': 6, 'desc': 'Lataria', 'fotoObrigatoria': True, 'tipoVeiculo': 1}
	      ],
	      
	    }
	    
	    return self.render_json(cadastro)
    
  
  	def get_percursos(self):
	    percursos = {
	      'success': True, 'imei': self.request.get('imei'),
	      'percursos':[
		{'id': 1, 'desc_produto': 'Veiculo', 'modelo': 'L200', 'placa': 'ABC1234', 'chassi': 'ABC123XYZ', 'data_coleta': '01/02/2014 12:45',
		 'logradouro_coleta': 'Rua X1', 'numero_coleta': 11, 'cidade_coleta': 'SBC1', 'uf_coleta': 'SP1',
		 'logradouro_entrega': 'Rua X1', 'numero_entrega': 12, 'cidade_entrega': 'SBC1', 'uf_entrega': 'SP1',
		 'status': '2', 'tipoVeiculo': 1
		},
		{'id': 2, 'desc_produto': 'Veiculo', 'modelo': 'Golf', 'placa': 'ABC1234', 'chassi': 'ABC123XYZ', 'data_coleta': '01/02/2014 12:45',
		 'logradouro_coleta': 'Rua X2', 'numero_coleta': 21, 'cidade_coleta': 'SBC2', 'uf_coleta': 'SP2',
		 'logradouro_entrega': 'Rua X2', 'numero_entrega': 22, 'cidade_entrega': 'SBC2', 'uf_entrega': 'SP2',
		 'status': '2', 'tipoVeiculo': 1
		},
		{'id': 3, 'desc_produto': 'Diversos', 'modelo': 'Caixa', 'placa': 'ABC1234', 'chassi': 'ABC123XYZ', 'data_coleta': '01/02/2014 12:45',
		 'logradouro_coleta': 'Rua X3', 'numero_coleta': 31, 'cidade_coleta': 'SBC3', 'uf_coleta': 'SP3',
		 'logradouro_entrega': 'Rua X3', 'numero_entrega': 32, 'cidade_entrega': 'SBC3', 'uf_entrega': 'SP3',
		 'status': '2', 'tipoVeiculo': 1
		},
	      ]
	    }
	    return self.render_json(percursos)
	  
   
  	def track_motorista(self):
		lat = self.request.get('lat')
		lon = self.request.get('lon')
		imei = self.request.get('imei')

		json_body = json.decode(self.request.body)

		for loc in json.decode(json_body['locations']):
			print 'Latidude: %s | Longitude: %s | IMEI: %s' %(loc['latitude'], loc['longitude'], loc['imei'])

		return self.render_json({'success': True})