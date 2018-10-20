def fetch_map(handler):
    try:
        with open('handler/map/map.png', 'rb') as map_file:
            message = map_file.read()
        
        if message is not None:
            handler.send_response(200)
            handler.send_header('Content-type', 'image/png')    
            handler.end_headers()

            handler.wfile.write(message)
            return

    except IOError:
        handler.send_error(404, 'Could not find map file')
