from fastapi import FastAPI, HTTPException
import requests

app = FastAPI(name="notification")
app.title = "Notification service"


@app.get("/connection/")
async def connection_to_auth():
    return {"connection": "Notif service"}


def check_connection(url: str) -> bool:
    ok = False
    try:
        response = requests.get(url)
        if response.status_code == 200:
            ok = "True"
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

    return ok


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8003, reload=True)