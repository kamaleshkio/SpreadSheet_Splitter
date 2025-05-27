import re
import datetime
from modules.logger import get_logger

logger = get_logger(__name__)

def extract_date_from_filename(filename):

    pattern = r'(\d{2})([a-zA-Z]*})(\d{4})'

    match = re.search(pattern, filename)

    if not match:
        logger.error(f"Filename does not match expected format: {filename}")
        raise ValueError(f"Date Pattern not found in filenamr. ")
                         
    day_str, month_str, year_str = match.groups()
    day = int(day_str)
    year = int(year_str)

    try:
        month = datetime.datetime.strptime(month_str, '%b').month if len(month_str) ==3 else datetime.datetime.strptime(month_str, '%B').month

    except ValueError as e:
        logger.error(f"Invalid month string in filename {month_str}: {e}")
        raise e
    
    date = datetime.datetime(year, month, day)
    formatted_date = date.strftime("%d-%m-%y")
    logger.info(f'Extracted date from filename {filename}: {formatted_date}')
    return formatted_date