import stripe
from app.core.config import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session(plano_id: str, user_id: int):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': plano_id,
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:3000/success',
        cancel_url='http://localhost:3000/cancel',
    )
    
    return {
        "checkout_url": session.url,
        "session_id": session.id
    }
