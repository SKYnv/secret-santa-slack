from aiohttp import web
from json.decoder import JSONDecodeError

async def handle(request):
    return web.Response(text="Hello!")

async def unknown(request):
    url = request.match_info.get('url')
    text = f'Unknown enpoint "{url}".'
    return web.Response(text=text)

async def incomming_message(request):
    try:
        response = await request.json()
    except JSONDecodeError:
        print(request)
        response = {}

    if request.method == 'POST':
        print(response)
        challenge = response.get('challenge')
        if challenge:
            return web.json_response(data={"challenge": challenge})
    return web.json_response(data=response)

santa_app = web.Application()
santa_app.add_routes([web.get('/', handle),
                web.get('/msg', incomming_message),
                web.post('/msg', incomming_message),
                web.get('/{url}', unknown),])

if __name__ == '__main__':
    web.run_app(santa_app, port=80)
