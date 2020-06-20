from cgi import parse_qs
from template import html

def application(environ, start_response):
	d = parse_qs(environ['QUERY_STRING'])
	a = d.get('a', [''])[0]
	b = d.get('b', [''])[0]
	response_body = html.split('\n')
	try:
		a, b = int(a), int(b)
		response_body[8] += str(a+b)
		response_body[9] += str(a*b)
			
	except:
		if a == '':
			response_body[4] = b' a is empty.' 
		if b == '': 
			response_body[6] = b' b is empty.'


	response_body = '\n'.join(response_body)
	start_response('200 OK', [
		('Content-Type', 'text/html'),
		('Content-Length', str(len(response_body)))
	])
	return [response_body]

