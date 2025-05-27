import re
import datetime
from modules.logger import get_logger

logger = get_logger(__name__)

def extract_date_from_filename(filename):
    pattern = r'(\d{2})([a-zA-Z]+)(\d{4})'
    match = re.search(pattern, filename)
    if not match:
        logger.error("Filename does not match date pattern.")
        raise ValueError("Date pattern not found in filename.")

    day_str, month_str, year_str = match.groups()
    day = int(day_str)
    year = int(year_str)

    try:
        month = datetime.datetime.strptime(month_str, '%b').month if len(month_str) == 3 else datetime.datetime.strptime(month_str, '%B').month
    except ValueError as e:
        logger.error(f"Invalid month string in filename: {month_str}")
        raise

    date_obj = datetime.datetime(year, month, day)
    formatted_date = date_obj.strftime("%d/%m/%Y")
    logger.info(f"Extracted date: {formatted_date}")
    return formatted_date