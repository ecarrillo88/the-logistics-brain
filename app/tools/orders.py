from langchain.tools import tool

from app.database.order import get_order_by_id, update_order


@tool
def get_order_details(order_id: str) -> dict:
    """
    Returns the order details: metadata, client, and status.

    Args:
        order_id: The order id
    
    Returns:
        The order
    """

    return get_order_by_id(order_id)

@tool
def update_delivery_schedule(order_id: str, new_time: str) -> dict:
    """
    Update the delivery schedule.

    Args:
        order_id: The order id
        new_time: New estimated delivery date in YYYY-mm-ddTHH:MM:SSZ format
    """

    order = get_order_by_id(order_id)
    order["estimated_delivery_date"] = new_time
    update_order(order_id, order)

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