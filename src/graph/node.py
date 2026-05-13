import re
from src.tools.orders import get_order_details

def get_order(state):
    content = state.get("ticket", {}).get("content")
    match = re.search(r"#ORD-\d+", content)

    if not match:
        return {"order": None}

    order_id = match.group(0)

    order = get_order_details.invoke({"order_id": order_id})

    if not order:
        return {"order": None}

    return {"order": order}