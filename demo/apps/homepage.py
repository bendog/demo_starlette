from starlette.applications import Starlette
from starlette.responses import JSONResponse

app = Starlette()


def homepage(request):
    return JSONResponse({'hello': 'world'})

app.add_route('/', homepage, methods=['GET'])
