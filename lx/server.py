from wsgiref.simple_server import make_server
from hello import application
 
httpd=make_server('',800,application)
print('running...')
httpd.serve_forever()