# -*- coding: utf-8 -*-

from aiohttp import web
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
                        web.get('/consulta_dtnasc/{cpf}', self.get_cpf),
                        web.post('/consulta_dtnasc/', self.post_cpf)])
        app.router.add_static('/pages/', path='pages/', append_version=False)
        app.router.add_static('/consulta_dtnasc/pages', path='pages/', append_version=False)
        self.env = Environment(loader=PackageLoader('webservice', 'pages'), autoescape=select_autoescape(['html']))
        web.run_app(app, host='0.0.0.0', port=7979)

    async def get_cpf(self, request):
        cpf = request.match_info['cpf']
        #return web.Response(text=PeopleService().check_cpf(cpf=cpf), content_type='text/plain')
        return web.json_response(PeopleService().check_cpf(cpf=cpf))

    async def post_cpf(self, request):
        data = await request.post()
        cpf = data.get('cpf')
        asw = PeopleService().check_cpf(cpf=cpf)
        page = self.env.get_template('resposta.html')
        out = page.render(resp=asw)
        return web.Response(text=out, content_type='html')

    async def home_page(self, request):
        """ Método da homepage do serviço."""
        page = self.env.get_template('index.html')
        out = page.render()
        return web.Response(text=out, content_type='html')


if __name__ == '__main__':
    Handler()
