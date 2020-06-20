from cgi import parse_qs
from template import html

def application(environ, start_response):
	d = parse_qs(environ['QUERY_STRING'])
	a = d.get('a', [''])[0]
	b = d.get('b', [''])[0]
	response_body = html
	try:
		a, b = int(a), int(b)
		response_body = response_body.split('\n')
		response_body[8] += str(a+b)
		response_body[9] += str(a*b)
		response_body = '\n'.join(response_body)
	except:
		pass

	start_response('200 OK', [
		('Content-Type', 'text/html'),
		('Content-Length', str(len(response_body)))
	])
	return [response_body]

