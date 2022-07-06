import  requests as req

cabecalho = {'user-agent': 'Windows 13'}
req.post('texte.com',
         headers=cabecalho)

