from datetime import datetime


def generate_unique_email():
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"abhishek_{timestamp}@gmail.com"