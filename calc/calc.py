from cgi import parse_qs
from template import html

def application(environ, start_response):
	d = parse_qs(environ['QUERY_STRING'])
	a = d.get('a',[''])[0]
	b = d.get('b',[''])[0]
	sum, mul ='None','None' 
	if '' not in [a,b]:
		sum = int(a)+int(b)
		mul = int(a)*int(b)
	else : a,b = 'None','None'
	response_body = html % {'a':a,'b':b,'sum':str(sum), 'mul':str(mul)}
	start_response('200 OK',[
		('Content-Type', 'text/html'),
		('Content-Length',str(len(response_body)))])
	return [response_body]
