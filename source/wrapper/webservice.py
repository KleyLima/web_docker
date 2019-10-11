# -*- coding: utf-8 -*-

from aiohttp import web
import json


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
        app.add_routes([web.post('/', self.post),
                        web.post('/consulta_dtnasc/{cpf}', self.post)])
        # app.router.add_static('/pages/', path='pages/',
        #                       append_version=False)  # Adiciona rota 'interna' para arquivos dentro do projeto.
        web.run_app(app, host='localhost', port=7979)

    async def post(self, request):
        cpf = request.match_info['cpf']
        note = {"id": "Kley", "cpf": "{}".format(cpf)}
        note = json.dumps(note)
        return web.Response(status=200, body=note, content_type='application/json')


if __name__ == '__main__':
    Handler()
