from cgi import parse_qs
from template import html

def application(environ, start_response):
	d = parse_qs(environ['QUERY_STRING'])
	a = d.get('a',[''])[0]
	b = d.get('b',[''])[0]
	sum, mul = 'None','None' 
	message = 'Please Enter Values of a and b.'
        if '' not in [a,b]:
                if a.isdigit() and b.isdigit():
                        sum = int(a)+int(b)
                        mul = int(a)*int(b)
                        message = 'Well Done!'
                else : 
                        sum = 'Error'
                        mul = 'Error'
                        message = 'Please Enter Inteagers.'
        else : 
                if [a,b][0]== '': a = 'None'
                else : 
                        sum,mul = 'Error','Error'
                        message = 'Please Enter a Value of b.'
                if [a,b][1]== '': b = 'None'
                else :
                        sum,mul = 'Error','Error'
                        message = 'Please Enter a Value of a.'
        response_body = html % {'a':a, 'b':b, 'sum':str(sum), 'mul':str(mul), 'message':message}
	start_response('200 OK',[
		('Content-Type', 'text/html'),
		('Content-Length',str(len(response_body)))])
	return [response_body]
