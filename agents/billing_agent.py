from swarm import Agent
from routable_agent import RoutableAgent

def get_account_balance(account_number):
    """
    Returns the current balance of the customer's account
    """

    return "$100.00"

def pay_bill(account_number:str, amount:int=0, card_number:str="1111111111111111", expiry_date:str="0929", cvv:str="123"):
    """
    Allows the customer to pay their bill. The amount, card_number, expiry_date, and cvv are required to process the payment.
    All cards details are processed securely and are not stored - they are handled offsite by our merchant services provider.
    
    amount: the amount to pay, in dollars (no cents)
    card_number: the customer's credit card number (16 digit string, without spaces)
    expiry_date: the expiry date of the credit card in the format MMYY
    cvv: the CVV code of the credit card

    Returns a confirmation message with the payment details
    """

    return f"Thank you for your payment of ${amount} on account {account_number} using card ending in { card_number[-4:]}. Your new balance is ${100-amount}.00"
   

def cancel_account(account_number):
    """
    Cancels the customer's account. This action is irreversible and will terminate all services associated with the account.
    """

    return f"Your account has been successfully cancelled. Thank you for choosing Rogers Communications. As a reminder you still owe {get_account_balance(account_number)}. Please pay this amount to avoid any further action on your account."

billing_agent = RoutableAgent(
    agent= Agent(
        name="Jane",
        instructions="Your name is Jane! You are a customer service agent for Rogers Communications.  Please greet the customer in a friendly way and assist with all billing and account related issues using the tools available. After you are finished helping the customer, either end the call or transfer to another agent if they still have issues to be resolved.",
        functions=[get_account_balance, pay_bill, cancel_account],
    ),
    agent_id="billing_agent",
    agent_description="Customer Service and Billing Support",
)

