DATABASE = {
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
                "postal_code": "46000",
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
    },
    "#ORD-555": {
        "order_id": "#ORD-555",
        "status": "sent",
        "created_at": "2026-05-01T20:07:00Z",
        "estimated_delivery_date": "2026-05-15T00:00:00Z",
        "total_amount": 120.00,
        "currency": "EUR",
        "client": {
            "id": "cli_54321",
            "name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@email.com",
            "phone": "+34600123456",
            "address": {
                "street": "Calle Mayor 10",
                "city": "Madrid",
                "postal_code": "28000",
                "country": "ES"
            }
        },
        "metadata": {
            "source": "web",
            "payment_method": "card",
            "is_gift": False,
            "priority": "normal",
            "notes": "Dejar al vecino de la puerta 2 si no estoy en casa"
        },
    },
}

def get_order_by_id(order_id: str) -> dict:
    return DATABASE.get(order_id)

def update_order(order_id: str, order: dict) -> None:
    DATABASE[order_id] = order