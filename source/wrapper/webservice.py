# -*- coding: utf-8 -*-

from aiohttp import web
from source.service.people_service import PeopleService



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
        app.add_routes([web.get('/consulta_dtnasc/{cpf}', self.get_cpf),
                        web.post('/consulta_dtnasc/', self.post_cpf)])
        web.run_app(app, host='0.0.0.0', port=7979)

    async def get_cpf(self, request):
        cpf = request.match_info['cpf']
        return web.json_response(PeopleService().check_cpf(cpf=cpf))

    async def post_cpf(self, request):
        data = await request.json()
        cpf=data.get('cpf') 
        return web.json_response(PeopleService().check_cpf(cpf=cpf))

if __name__ == '__main__':
    Handler()
