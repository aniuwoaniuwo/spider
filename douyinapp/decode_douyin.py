#-*-coding:utf-8-*-
def decode_response(response):

    regex_list = [
            {'name':[' &#xe603; ',' &#xe60d; ',' &#xe616; '],'value':0},
            {'name':[' &#xe602; ',' &#xe60e; ',' &#xe618; '],'value':1},
            {'name':[' &#xe605; ',' &#xe610; ',' &#xe617; '],'value':2},
            {'name':[' &#xe604; ',' &#xe611; ',' &#xe61a; '],'value':3},
            {'name':[' &#xe606; ',' &#xe60c; ',' &#xe619; '],'value':4},
            {'name':[' &#xe607; ',' &#xe60f; ',' &#xe61b; '],'value':5},
            {'name':[' &#xe608; ',' &#xe612; ',' &#xe61f; '],'value':6},
            {'name':[' &#xe60a; ',' &#xe613; ',' &#xe61c; '],'value':7},
            {'name':[' &#xe60b; ',' &#xe614; ',' &#xe61d; '],'value':8},
            {'name':[' &#xe609; ',' &#xe615; ',' &#xe61e; '],'value':9},
        ]
    for regex in regex_list:
        for num in regex['name']:
            if num in response:
                response=response.replace(num,str(regex['value']))
    return response
