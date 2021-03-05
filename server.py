from aiohttp import web

async def handle(request):
    path = request.match_info.get('path', "index.html")
    print(path)
    with open("files/src/" + path, "r") as curfile:
        return web.Response(text=curfile.read())

app = web.Application()
app.router.add_get('/', handle)
app.router.add_get('/{path}', handle)

web.run_app(app, port=7321)