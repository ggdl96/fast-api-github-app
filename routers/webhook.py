from fastapi import APIRouter
from models.webhooks import PullRequestWebhook
from services.auth import gen_jwt

webhook_router = APIRouter()

@webhook_router.post("/github/webhook")
async def github_webhook(payload: PullRequestWebhook):
    # print('payload: ', payload)
    printed = False

    if (payload.action == 'created' and payload.installation): 
        # print('payload.installation: ', payload.installation)
        #gen_jwt()
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
