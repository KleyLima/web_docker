# -*- coding: utf-8 -*-

from aiohttp import web
import json
from source.service.people_service import PeopleService
from jinja2 import Environment, PackageLoader, select_autoescape



class Handler:
    """
    Classe que representa os endpoints expostos no serviço, suas respectivas funções de tratamento e parâmetros que
    são passados na chamada.
    """

    def __init__(self):
        """
        Método que executa ao instanciar a classe, carrega os endpoints na tabela de rota e inicializa o serviço no
        port 7979
        """
        app = web.Application()
        app.add_routes([web.get('/', self.home_page),
                        web.post('/consulta_dtnasc/', self.post)])
        app.router.add_static('/pages/', path='pages/',
                              append_version=False)
        app.router.add_static('/consulta_dtnasc/pages', path='pages/',
                              append_version=False)
        self.env = Environment(loader=PackageLoader('webservice', 'pages'),
                               autoescape=select_autoescape(['html']))
        web.run_app(app, host='localhost', port=7979)

    async def post(self, request):
        data = await request.post()
        cpf = data.get('cpf')
        note = PeopleService().check_cpf(cpf=cpf)
        note = json.dumps(note)
        page = self.env.get_template('index1.html')
        out = page.render(nota=note)
        return web.Response(text=out, content_type='html')

    async def home_page(self, request):
        """ Método da homepage do serviço."""
        page = self.env.get_template('index.html')
        out = page.render()
        return web.Response(text=out, content_type='html')


if __name__ == '__main__':
    Handler()
