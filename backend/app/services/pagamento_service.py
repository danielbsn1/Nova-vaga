import stripe
from app.core.config import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


def create_checkout_session(plano_id: str, user_id: int):
    session = stripe.checkout.Session.create(
        mode="payment",
        payment_method_types=["card"],
        line_items=[
            {
                "price": plano_id,
                "quantity": 1,
            }
        ],
        metadata={
            "user_id": user_id,
            "plano_id": plano_id,
        },
        success_url=settings.FRONT_SUCCESS_URL,
        cancel_url=settings.FRONT_CANCEL_URL,
    )

    return {
        "checkout_url": session.url,
        "session_id": session.id,
    }