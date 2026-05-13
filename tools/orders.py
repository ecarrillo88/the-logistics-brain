from langchain.tools import tool
from typing import Any

ORDER_DATABASE = {
    "#ORD-123": {
        "order_id": "#ORD-123",
        "status": "processing",
        "created_at": "2026-04-23T10:15:00Z",
        "estimated_delivery_date": "2026-05-01T00:00:00Z",
        "total_amount": 59.90,
        "currency": "EUR",
        "client": {
            "id": "cli_12345",
            "name": "John",
            "last_name": "Doe",
            "email": "john.doe@email.com",
            "phone": "+34600123456",
            "address": {
                "street": "Calle Mayor 10",
                "city": "Valencia",
                "postal_code": "46001",
                "country": "ES"
            }
        },
        "metadata": {
            "source": "web",
            "payment_method": "card",
            "is_gift": False,
            "priority": "normal",
            "notes": "Entrega por la tarde si es posible"
        },
    }
}

@tool
def get_order_details(order_id: str) -> dict:
    """
    Returns the order details: metadata, client, and status.

    Args:
        order_id: The order id
    
    Returns:
        The order
    """

    return ORDER_DATABASE.get(order_id)

@tool
def update_delivery_schedule(order_id: str, new_time: str) -> dict:
    """
    Update the delivery schedule.

    Args:
        order_id: The order id
        new_time: New estimated delivery date
    """

    order = ORDER_DATABASE.get(order_id)
    order.estimated_delivery_date = new_time

    return order

@tool
def generate_invoice_pdf(order_id: str) -> str:
    """
    Generate the download link for the invoice in PDF format

    Args:
        order_id: The order id

    Returns:
        The order invoice URL
    """

    return f"https://www.the-logistics-brain.org/order/{order_id}/invoice.pdf"