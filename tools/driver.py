from langchain.tools import tool

@tool
def verify_driver_status(driver_id: str) -> int:
    """
    Returns remaining driving hours.
    
    Args:
        driver_id: Driver identification number

    Returns:
        Remaining driving hours
    """
    return 18