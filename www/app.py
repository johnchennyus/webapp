import logging

logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time

from datetime import datetime

from aiohttp import web


# deal with the URL, later it will bind with particular URL
# Don't care about how the function deal with the request, the frame will handle it
def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')

def hello(request):
    return web.Response(body=b'<h1>Hello</h1>', content_type='text/html')



# construct a server application instance. and register the processing function to the application route
async def init(mainLoop):
    
    app = web.Application(loop=mainLoop)
    
    # when you use the app, the first thing you should do is to register URLs to router,and then use aiohttp.RequestHandleFactory as the protocal to construct socket
    
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello', hello)

    # Use coroutin to listen service .loop is the coroutine passed into function. 
    srv = await mainLoop.create_server(app.make_handler(), '127.0.0.1', 9000)

    logging.info('server started at http://127.0.0.1:9000...')

    return srv



loop = asyncio.get_event_loop()

loop.run_until_complete(init(loop))


loop.run_forever()



