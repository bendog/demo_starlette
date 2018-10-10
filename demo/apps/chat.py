from apistar import types, validators
from apistar.exceptions import ValidationError
from starlette.applications import Starlette
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse

app = Starlette()


class ChatData(types.Type):
    message = validators.String(description="The message will be sent back to you", max_length=1000, min_length=1)


@app.route('/', methods=['GET', 'POST'])
async def chat(request: Request):
    print(request)
    if request.method == 'GET':
        data = None
    else:
        data = await request.json()
        print(type(data))
        print(data)
        if data:
            try:
                data = dict(ChatData(data))
            except ValidationError as e:
                raise HTTPException(status_code=422, detail="%s(%s)" % (e.__class__.__name__, str(e)))
    return JSONResponse({"chat": data})
