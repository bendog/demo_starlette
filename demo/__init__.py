import uvicorn
from starlette.exceptions import ExceptionMiddleware, HTTPException
from starlette.responses import JSONResponse
from starlette.routing import Router, Path, PathPrefix
from starlette.middleware.cors import CORSMiddleware  # this isn't currently working with starlette 0.3.6 on PyPI, but you can import from github.
from demo.apps import homepage, chat


app = Router([
    Path('/', app=homepage.app, methods=['GET']),
    PathPrefix('/chat', app=chat.app),
])

app = CORSMiddleware(app, allow_origins=['*'])


app = ExceptionMiddleware(app)


def error_handler(request, exc):
    return JSONResponse({"detail": exc.detail}, status_code=exc.status_code)


app.add_exception_handler(HTTPException, error_handler)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
