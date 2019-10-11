# -*- coding: utf-8 -*-


class CPFHtml:

    @classmethod
    def __init__(cls, cpf, valid):
        cls.html=\
                """
                <html>
                    <head>
                        <title>Valida CPF</title>
                    </head>
                    <body>
                    	<p style = "font-family:arial;font-size:20px;font-style:normal;color:blue;text-align:right">
                          CPF: 
                          <span style = "color:red;">{} </span>
                      </p>
                      <p style = "color:green;font-size:18px;text-align:right;">
                      	Valid: {}
                      </p>
                    </body>
                </html>             
                """.format(cpf, valid)

