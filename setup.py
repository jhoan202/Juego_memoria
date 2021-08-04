from distutils.core import setup
import py2exe

setup(name="Juego de Memoria",

	version="1.0",
	description="""Este juego tiene unos
	unos pequeños errores, que se trataran de corregir
	para su correcto  funcionamiento""",
	author="JHOAN BARRERA",
	author_email='jhoanbarreravanegas@gmail.com',
	url='juegodememoriasinlicencia.com',
	license="free",
	scripts=["juego_memoria.py"],
	console=["juego_memoria.py"],
	options={"py2exe":{"bundle_files":1}},
	zipfile=None,




	) 