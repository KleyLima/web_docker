# -*- coding: utf-8 -*-


class DistHtml:

    @classmethod
    def __init__(cls, string, zeros):
        cls.html=\
                """
                <html>
                    <head>
                        <title>Distancia de Zeros</title>
                    </head>
                    <body>
                    	<p style = "font-family:arial;font-size:35px;font-style:italic;color:black;text-align:left">
                          {}
                      </p>
                      <p style = "color:purple;font-size:24px;text-align:left;">
                        {}
                      </p>
                    </body>
                </html>             
                """.format(string, zeros)

