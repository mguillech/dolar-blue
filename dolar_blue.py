#!/usr/bin/env python

import requests
from pyquery import PyQuery

USER_AGENT = 'Mozilla/5.0'
CG_URL = 'http://www.cordobaguias.com.ar/cotizacion-dolar-en-cordoba.html'
PDB_URL = 'http://www.preciodolarblue.com.ar'

headers = {'User-Agent': USER_AGENT}

cg = PyQuery(requests.get(CG_URL, headers=headers).content).find('.cuadroPrecioD').text().replace(' pesos', '')
pdb_tds = PyQuery(requests.get(PDB_URL, headers=headers).content).find('td')
pdb = (pdb_tds.eq(3).text(), pdb_tds.eq(4).text())

print 'cordobaguias | preciodolarblue'
print '-' * 30
print '%s | %s' % (cg, ' / '.join(pdb))

