from aiohttp import web
from json.decoder import JSONDecodeError
from aioslacker import Slacker
from conf.settings import SLACK_BOT_TOKEN

async def handle(request):
    return web.Response(text="Hello!")

async def unknown(request):
    url = request.match_info.get('url')
    text = f'Unknown enpoint "{url}".'
    return web.Response(text=text)

async def incomming_message(request):
    try:
        response = await request.json()
        print(response)
    except Exception:
        return web.Response(text=request.headers)

    if request.method == 'POST':
        if 'challenge' in response:
            return web.json_response(data={"challenge": response.get('challenge')})

        if response["event"]["type"] == "message":
            await reply_to_message(response["event"])

        return web.Response()

    return web.json_response(data=response)

async def reply_to_message(event):
    text = (f"Ой <@{event['user']}>, я еще такой глупый! ")

    await slack_client.chat.post_message(event["channel"], text=text)

santa_app = web.Application()
santa_app.add_routes([web.get('/', handle),
                web.get('/msg', incomming_message),
                web.post('/msg', incomming_message),
                web.get('/{url}', unknown),])

if __name__ == '__main__':
    slack_client = Slacker(SLACK_BOT_TOKEN)
    web.run_app(santa_app, port=80)
