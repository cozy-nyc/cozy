from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# import stripe
# stripe.api_key = settings.STRIPE_SECERT_KEY

# Create your views here.
@login_required
def checkout(request):
    publishKey = settings.STRIPE_PUBLISHBLE_KEY
    customer_id = request.user.userstripe.stripe_id
    if request.method == "POST":
        # Token is created using Stripe.js or Checkout!
        # Get the payment token submitted by the form:
        token = request.POST['stripeToken']

        # Charge the user's card:
        customer = stripe.Customer.retrieve(customer_id)
        customer.source.create(source=token)
        charge = stripe.Charge.create(
          amount=1000,
          currency="usd",
          description="Example charge",
          customer=customer,
        )
    context = {
        'publishKey': publishKey
    }
    template = 'checkout.html'
    return render(request, template, context)
