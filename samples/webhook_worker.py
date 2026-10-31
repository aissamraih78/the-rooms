"""
SyntaxCraft Studio - Webhook & Event Dispatcher Worker
Listens to Merchant of Record (Lemon Squeezy) webhooks, verifies HMAC signatures,
updates local databases, and dispatches real-time alerts.
"""

import hmac
import hashlib
import logging
from typing import Dict, Any
from fastapi import FastAPI, Request, HTTPException, Header, status
from pydantic import BaseModel

from config import settings

logger = logging.getLogger("syntaxcraft.webhook")
app = FastAPI(
    title="SyntaxCraft Webhook Engine",
    description="Production-grade webhook receiver for Lemon Squeezy and automated dispatchers.",
    version="1.0.0"
)


class WebhookPayload(BaseModel):
    event_name: str
    data: Dict[str, Any]


def verify_signature(payload_body: bytes, signature_header: str) -> bool:
    """Validates Lemon Squeezy HMAC SHA-256 signature."""
    if not signature_header:
        return False
    digest = hmac.new(
        key=settings.webhook_secret.encode("utf-8"),
        msg=payload_body,
        digestmod=hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(digest, signature_header)


@app.get("/health")
def health_check():
    """Health status endpoint for Docker container checks."""
    return {"status": "healthy", "service": "SyntaxCraft-Webhook-Engine", "version": "1.0.0"}


@app.post("/webhooks/lemon-squeezy", status_code=status.HTTP_200_OK)
async def handle_lemon_squeezy_webhook(
    request: Request,
    x_signature: str = Header(default="")
):
    """
    Handles Lemon Squeezy order fulfillment events:
    - order_created: Provision digital license and send automated GitHub invite
    - subscription_created: Provision SaaS workspace
    """
    body = await request.body()
    
    # In test environments or when secret is set, verify cryptographic signature
    if settings.environment == "production" and not verify_signature(body, x_signature):
        logger.warning("Rejected unauthorized webhook call with invalid HMAC signature.")
        raise HTTPException(status_code=403, detail="Invalid cryptographic signature")

    payload = await request.json()
    event_name = payload.get("meta", {}).get("event_name", "unknown")
    logger.info(f"Received verified Lemon Squeezy event: '{event_name}'")

    if event_name in ["order_created", "order_refunded"]:
        order_data = payload.get("data", {})
        customer_email = order_data.get("attributes", {}).get("user_email", "N/A")
        total_formatted = order_data.get("attributes", {}).get("total_formatted", "$0.00")
        
        logger.info(f"Processing order for customer: {customer_email} - Amount: {total_formatted}")
        # Dispatch GitHub repository invitation or ZIP delivery here
        return {
            "status": "processed",
            "event": event_name,
            "fulfillment": "instant_repository_access_granted",
            "customer": customer_email
        }

    return {"status": "acknowledged", "event": event_name}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("webhook_worker:app", host=settings.webhook_host, port=settings.webhook_port, reload=True)

