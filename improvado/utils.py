import hashlib
from datetime import datetime


def generate_unique_filename(filename: str):
    """
    :param filename:
    :return: str: unique filename compose by the original name plus a hash generated from the timestamp in
    order to avoid name collisions
    """
    name, extension = filename.split('.')
    timestamp = str(datetime.timestamp(datetime.now())).split('.')[1]
    return f"{name}__{hashlib.shake_256(timestamp.encode()).hexdigest(2)}.{extension}"
