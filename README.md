# Proyecto-Desarrollo-Wen
El proyecto de desarrollo web enfocado en una pastelería, abarcando la problemática de gestión de pedidos e inventario de materia prima 
Este proyecto utiliza base de datos mysql, esto pues debido al funcionamiento de nuestra plataforma es necesario mayor concurrencia de la que nos permite sqlite, por lo tanto, para efectuar su funcionamiento debe instalar dicho motor y ademas los requeriment
Para la instalacion se le aconseja seguir estos pasos :

	sudo apt-get install python3-dev libmysqlclient-dev
	
	pip install mysqlclient
	
	sudo apt-get install mysql-server
	
	
	para configurar el .cnf, utilizar este comando en la consola:
		sudo nano /etc/mysql/my.cnf
		(porfavor ingresar los datos solicitados y sus credenciales)

	para mayor detalle y paso a paso, consultar el siguiente enlace
	
	https://www.digitalocean.com/community/tutorials/how-to-create-a-django-app-and-connect-it-to-a-database

solucion problematica
Para solucionar la problemática en cuestión (administración de stock y de pedidos) desarrollamos una plataforma que busca facilitar el proceso de pedidos para que puedan ser realizados de manera autónoma de parte del cliente y a su vez mas sencilla para registrar por parte del vendedor. Y para la parte del stock creamos un administrador que permite realizar reabastecimientos y llevar cuentas de stock automáticamente en razón de los pedidos.

Este proyecto fue realizado por:
	Nicolas Cordova ( JP )
	Alvaro Abarca
	Israel Castro
	

