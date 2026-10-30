"""
SyntaxCraft Studio - Open Evaluation Sample: Lemon Squeezy Webhook Verification
Website: https://syntaxcraft.dev
License: Free for evaluation, MIT

Demonstrates HMAC-SHA256 signature verification and order dispatching.
"""

import hmac
import hashlib
import json


def verify_lemon_signature(raw_payload: bytes, signature_header: str, webhook_secret: str) -> bool:
    """Verifies that an incoming webhook genuinely originated from Lemon Squeezy."""
    if not signature_header:
        return False
    calculated_digest = hmac.new(
        key=webhook_secret.encode("utf-8"),
        msg=raw_payload,
        digestmod=hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(calculated_digest, signature_header)


def simulate_order_event():
    secret = "sample_test_secret_key_12345"
    sample_order = {
        "meta": {"event_name": "order_created"},
        "data": {
            "type": "orders",
            "id": "109842",
            "attributes": {
                "user_name": "Developer Customer",
                "user_email": "customer@example.com",
                "total_formatted": "$149.00",
                "status": "paid"
            }
        }
    }
    raw_bytes = json.dumps(sample_order, separators=(',', ':')).encode("utf-8")
    valid_signature = hmac.new(secret.encode("utf-8"), raw_bytes, hashlib.sha256).hexdigest()

    print("=" * 65)
    print("🔒 SyntaxCraft Studio — Lemon Squeezy Webhook Verification Demo")
    print("=" * 65)
    print(f"Incoming Event: {sample_order['meta']['event_name']}")
    print(f"Customer: {sample_order['data']['attributes']['user_email']}")
    print(f"Amount: {sample_order['data']['attributes']['total_formatted']}")
    
    # Test valid signature
    is_valid = verify_lemon_signature(raw_bytes, valid_signature, secret)
    print(f"\n[Test 1] Valid HMAC signature verified: {is_valid}")
    assert is_valid is True, "Valid signature failed"
    
    # Test forged signature
    is_invalid = verify_lemon_signature(raw_bytes, "forged_signature_xyz", secret)
    print(f"[Test 2] Forged signature rejected: {not is_invalid}")
    assert is_invalid is False, "Forged signature was not rejected"

    print("\n✓ Webhook security engine operating as expected.")
    print("=" * 65)


if __name__ == "__main__":
    simulate_order_event()
