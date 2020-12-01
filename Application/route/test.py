from .. import App


@App.get("/test/testing")
async def t():
    return {"result": "asd"}
