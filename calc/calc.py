from cgi import parse_qs
from template import html

def application(environ, start_response):
	d = parse_qs(environ['QUERY_STRING'])
	a = d.get('a',[''])[0]
	b = d.get('b',[''])[0]
	sum, mul = 'None','None' 
	if '' not in [a,b]:
		if a.isdigit() and b.isdigit():
			sum = int(a)+int(b)
			mul = int(a)*int(b)
		else :
			sum = 'Error'
			mul = 'Error'
	else : 
		if [a,b][0]== '': a = 'None'
                else : sum,mul = 'Error','Error'
                if [a,b][1]== '': b = 'None'
                else : sum,mul = 'Error','Error'
	response_body = html % {'a':a, 'b':b, 'sum':str(sum), 'mul':str(mul)}
	start_response('200 OK',[
		('Content-Type', 'text/html'),
		('Content-Length',str(len(response_body)))])
	return [response_body]
