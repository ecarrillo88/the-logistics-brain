import re


def extract_order_id(text: str) -> str | None:
    match = re.search(r"#ORD-\d+", text)

    if not match:
        return {"order": None}

    return match.group(0)

