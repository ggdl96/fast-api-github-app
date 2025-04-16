import logging
import hmac
import hashlib
from fastapi import Request, HTTPException
from core.constants.base_config import settings

logger = logging.getLogger("webhook_service_logger")

github_headers = {
    "X-GitHub-Event": {"required": True, "error_msg": "Missing X-GitHub-Event header"},
    "X-Hub-Signature-256": {"required": True, "error_msg": "Missing X-Hub-Signature-256 header"},
    "User-Agent": {"required": False},
    "X-GitHub-Hook-ID": {"required": False},
    "X-GitHub-Hook-Installation-Target-ID": {"required": False},
    "X-GitHub-Hook-Installation-Target-Type": {"required": False},
    "X-GitHub-Delivery": {"required": False}
}
    
def verify_github_webhook_body_signature(signature: str, payload_body: bytes) -> bool:
    """Verify that the webhook request body that came from GitHub has a valid signature.

    Args:
        signature (str): the signature from header
        payload_body (bytes): the body of the request

    Raises:
        HTTPException: _description

    Returns:
        bool: True if valid, False if not
    """
    if not signature:
        return False
    
    webhook_secret = settings.GITHUB_WEBHOOK_SECRET
    if not webhook_secret:
        error_secret_not_set = "GITHUB_WEBHOOK_SECRET is not set!"
        logger.error(error_secret_not_set)
        raise HTTPException(
            status_code=400,
            detail=error_secret_not_set
        )
    
    logger.info("Starting signature validation process")

    expected_signature = hmac.new(
        webhook_secret.encode('utf-8'),
        payload_body,
        hashlib.sha256
    ).hexdigest()
    
    logger.info("Validation of expected signature")

    return hmac.compare_digest(f"sha256={expected_signature}", signature)

from typing import Dict, Any

async def github_webhook_validation(request: Request) -> Dict[str, Any]:
    """Validation of Github webook

    Args:
        request (Request): the incoming request

    Raises:
        HTTPException: Error message of header
        HTTPException: Invalid JSON payload
        HTTPException: Invalid webhook signature

    Returns:
        Dict[str, Any]: the [headers] and [body]
    """
    headers = {}
    for header_name, config in github_headers.items():
        header_value = request.headers.get(header_name)
        headers[header_name] = header_value
        
        if config["required"] and not header_value:
            logger.warning(config["error_msg"])
            raise HTTPException(
                status_code=400,
                detail=config["error_msg"]
            )
    
    event = headers["X-GitHub-Event"]
    signature = headers["X-Hub-Signature-256"]
    
    try:
        body = await request.body()
  
        logger.info(f"Received GitHub webhook event: {event}")
        
        if not verify_github_webhook_body_signature(signature, body):
            logger.error("Invalid webhook signature")
            raise HTTPException(status_code=403, detail="Invalid webhook signature")
    
        body_json = await request.json()

        return {
            "headers": headers,
            "body": body_json
        }
    except HTTPException:
       raise
    except Exception as e:
        logger.error(f"Error parsing webhook body: {str(e)}")
        raise HTTPException(
            status_code=400,
            detail="Invalid JSON payload"
        )
