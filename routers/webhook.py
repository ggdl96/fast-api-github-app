import logging
from fastapi import APIRouter, Depends, Request
from models.webhooks import RequestPayloadWebhook
from services.webhook import github_webhook_validation

webhook_router = APIRouter()
logger = logging.getLogger("webhook_logger")

@webhook_router.post("/github/webhook")
async def github_webhook(request: Request, payload: RequestPayloadWebhook, a = Depends(github_webhook_validation)):
    printed = False
    logger.info("github webhook for sending events")
    if (payload.action == 'created' and payload.installation): 
        print('installed')
        ## STORE IN OWN DB

    if (payload.installation): 
        print('payload: ', payload)
        printed = True

    if (payload.workflow_job):
        # print('payload.workflow_job: ', payload.workflow_job)
        printed = True

    if (payload.workflow_run):
        # print('payload.workflow_run: ', payload.workflow_run)
        print('payload: ', payload)

        printed = True

    if not printed:
        print('payload: ', payload)
        
    return None
