from cgi import parse_qs
from template import html

def application(environ, start_response):
	d = parse_qs(environ['QUERY_STRING'])
	a = d.get('a',[''])[0]
	b = d.get('b',[''])[0]
	sum, mul = 0, 0
	if '' not in [a,b]:
		a,b,c=int(a),int(b)
		x = [n/10.0 for n in range(-40,41)]
		y = [a *n**2 + b*n +c for n in x]
		sum = a+b
		mul = a*b
	response_body = html % {'sum':sum, 'mul':mu;}
	start_response('200 OK',[
		('Content-Type', 'text/html'),
		('Content-Length',str(len(response_body)))])
	return [response_body]
