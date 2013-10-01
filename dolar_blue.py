#!/usr/bin/env python

import requests
from pyquery import PyQuery

USER_AGENT = 'Mozilla/5.0'
CG_URL = 'http://www.cordobaguias.com.ar/cotizacion-dolar-en-cordoba.html'
PDB_URL = 'http://www.preciodolarblue.com.ar'
AMBITO_URL = 'http://www.ambito.com/economia/mercados/monedas/dolar/info/?ric=ARSB=C'

headers = {'User-Agent': USER_AGENT}

cg = PyQuery(requests.get(CG_URL, headers=headers).content).find('.cuadroPrecioD').text().replace(' pesos', '')
pdb_tds = PyQuery(requests.get(PDB_URL, headers=headers).content).find('td')
pdb = (pdb_tds.eq(3).text(), pdb_tds.eq(4).text())
ambito = PyQuery(requests.get(AMBITO_URL, headers=headers).content)

print 'cordobaguias | preciodolarblue'
print '-' * 30
print '%s | %s' % (cg, ' / '.join(pdb))
print 'Cueva (Ambito): %.2f | %.2f' % (float(ambito.find('#compra>big').text().replace(',', '.')),
                                   float(ambito.find("#venta>big").text().replace(',', '.')))

