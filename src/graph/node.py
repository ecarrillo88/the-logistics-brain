from src.helpers.common import extract_order_id
from src.tools.orders import get_order_details


def get_order(state):
    content = state.get("ticket", {}).get("content")
    order_id = extract_order_id(content)
    order = get_order_details.invoke({"order_id": order_id})

    if not order:
        return {"order": None}

    return {"order": order}