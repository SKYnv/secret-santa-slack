from aiohttp import web

async def handle(request):
    return web.Response(text="Hello!")

async def unknown(request):
    url = request.match_info.get('url')
    text = f'Unknown enpoint "{url}".'
    return web.Response(text=text)

async def incomming_message(request):
    response = await request.json()
    return web.json_response(data=response)

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/msg', incomming_message),
                web.get('/{url}', unknown),])

if __name__ == '__main__':
    web.run_app(app, port=80)