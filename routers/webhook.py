from fastapi import APIRouter
from models.webhooks import PullRequestWebhook

webhook_router = APIRouter()

@webhook_router.post("/github/webhook")
async def github_webhook(payload: PullRequestWebhook):
    print('payload: ', payload)
    
    return None
