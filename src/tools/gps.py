from langchain.tools import tool


@tool
def check_road_incidents(gps_coords: dict) -> list[dict]:
    """
    Check road_incidents and get traffic alerts
    
    Args:
        gps_coords: GPS coordinates

    Returns:
        The traffic alerts
    """

    incidents = [
        {
            "type": "accident",
            "severity": "high",
            "description": "Accidente en la autopista",
            "distance_km": 2.3
        },
        {
            "type": "traffic_jam",
            "severity": "medium",
            "description": "Retención de tráfico",
            "distance_km": 5.1
        }
    ]

    return incidents