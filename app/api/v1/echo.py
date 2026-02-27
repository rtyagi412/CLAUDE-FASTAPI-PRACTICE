from fastapi import APIRouter

from app.models import EchoRequest

router = APIRouter()


@router.post("/echo")
def echo(body: EchoRequest) -> EchoRequest:
    return body
