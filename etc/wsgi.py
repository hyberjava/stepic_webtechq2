def application(env, start_response):
    response_body = env['QUERY_STRING'].replace('&', '\n')
    start_response('200 OK', [('Content-Type', 'text/plain'), ('Content-Length', str(len(response_body)))])
    return [response_body]
