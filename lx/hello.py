def application(environ,start_response):
    satrt_response('200 ok',[('Content-Type','text/html')])   
    return [b'<h1>hello,wb!</h1>']