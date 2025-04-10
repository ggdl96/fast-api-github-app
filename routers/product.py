import logging
from fastapi import APIRouter, Depends, HTTPException
from models.product import Step, SubmitResponse, SubmitPayload
from services.auth import verify_action_jwt_token

product_router = APIRouter(
    tags=["product"],
)
logger = logging.getLogger("product_logger")

@product_router.post("/submit")
async def submit_in_product(data: SubmitPayload, decoded_token=Depends(verify_action_jwt_token)) -> SubmitResponse:
    logger.info("Start processing of subimit message")
    response_steps = []
    final_response = SubmitResponse(
        message="",
        description="The message was successfully processed",
        steps=[]
    )

    final_response_error = SubmitResponse(
        message="",
        description="Something went wrong",
        steps=[]
    )

    if (data.message.lower().find('not-allowed') != -1):
        response_steps.append(Step(name='process message', status='failed'))

        final_response_error.steps = response_steps
        final_response_error.description = "Message contains unallowed content."
        final_response_error.message = "Unable to process"
        logger.error("Message processing failed, not-allowed")
        raise HTTPException(400, detail=final_response_error.model_dump())

    response_steps.append(Step(name='process message', status='completed'))

    final_response.steps = response_steps
    final_response.message = f"This was the received message: {data.message}"
    logger.info('returning final response')
    return final_response
