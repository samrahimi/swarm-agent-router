from swarm import Swarm, Agent
from routable_agent import RoutableAgent

def get_internet_installation_time(customer_address, urgent=False):
    """
    Returns a suggested appointment date and time to install a new internet connection. If the customer agrees, you can then book_internet_installation for that date and local_time.
    If the suggested date and time is not convenient for the customer, just call this function again and it will return an alternative timeslot
    If the customer is not satisfied with the waiting time to get their internet up and running, call this with urgent=True to get the absolute soonest possible appointment

    """
    return {"date": "22-11-2024", "local_time": "16:20"}


def book_internet_installation(customer_address, customer_name, customer_phone, date, local_time):
    """
    Books an appointment to install a new internet connection. The customer_address, customer_name, and customer_phone are required to book the appointment.
    
    customer_address: the address where the internet will be installed. must be a valid address in the Rogers service area and include the postal code
    customer_name: the name of the customer who will be present at the installation
    customer_phone: the phone number of the customer
    date: the date of the appointment in the format DD-MM-YYYY
    local_time: the local time of the appointment in the format HH:MM (24-hour clock)

    Returns a confirmation message with the appointment details
    """

    return "Your appointment has been booked for {date} at {local_time}. A Rogers technician will arrive at {customer_address} to install your new internet connection. Thank you for choosing Rogers Communications!"


def get_internet_offers(postal_code):
    """
    Gets the available high-speed internet offers for the customer based on their location.

    postal_code: any valid Canadian postal code
    """
    

    gta_plans = """
    INSIDE THE GREATER TORONTO AREA:
    
    1. High Speed Internet 100: $60/month
    2. High Speed Internet 500: $80/month
    3. High Speed Internet Gigabit: $100/month
    4. High Speed Internet Gigabit Unlimited: $120/month
    """
    
    other_plans = """
    1. High Speed Internet 50: $70/month
    2. High Speed Internet 100: $90/month
    3. High Speed Internet 350: $200/month"
    """

    disclaimer="""
    All plans require a 2-year contract and a $50 installation fee that will be charged on the customer's first bill. 
    Prices do not include taxes. 
    Plans High Speed Internet 50 / 100 / 350 / Gigabit include 100GB of bandwidth usage. 
    High Speed Internet Gigabit Unlimited Plan inclues unlimited bandwidth usage.
    """

    if postal_code.startswith("M") or postal_code.startswith("m"):
        return gta_plans + disclaimer
    else:
        return other_plans + disclaimer


internet_sales_agent=RoutableAgent(
    agent= Agent(
    name="Pratham",
    instructions="Your name is Pratham and you are a high speed internet sales specialist for Rogers Communications. Please greet the customer in a friendly way, and then help them with their high speed internet sales inquiry. Your job is to sell the customer the best possible internet product based on their location (see available internet offers, below) and book them a professional installation.",
    functions=[get_internet_installation_time, book_internet_installation, get_internet_offers]
    ),
    agent_id="internet_sales_agent",
    agent_description="High Speed Internet Sales Specialist",
)
