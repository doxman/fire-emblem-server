def fetch_map(handler):
    try:
        with open('handler/map/map.png', 'rb') as map_file:
            message = map_file.read()
        
        if message is not None:
            handler.send_response(200)
            handler.send_header('Content-type', 'image/png')  
            handler.send_header('Access-Control-Allow-Origin', 'http://localhost:3000')  
            handler.end_headers()

            handler.wfile.write(message)
            return

    except IOError:
        handler.send_error(404, 'Could not find map file')

def map_options(handler):
    handler.send_response(204)
    handler.send_header('Access-Control-Allow-Credentials', 'true')
    handler.send_header('Access-Control-Allow-Origin', 'http://localhost:3000')
    handler.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
    handler.send_header("Access-Control-Allow-Headers", "X-Requested-With, Content-type")
    handler.end_headers()

