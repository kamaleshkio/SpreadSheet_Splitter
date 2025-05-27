import pandas as pd
import os
from modules.date_extractor import extract_date_from_filename
from modules.logger import get_logger

logger = get_logger(__name__)

def process_excel_file(file_path, output_folder):
    try:
        date = extract_date_from_filename(os.path.basename(file_path))
        xls = pd.ExcelFile(file_path)

        for sheet_name in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=sheet_name)
            df['Date'] = date

            output_file = os.path.join(output_folder, f"{sheet_name}.csv")
            df.to_csv(output_file, index=False)
            logger.info(f"{output_file} saved successfully.")

    except Exception as e:
        logger.exception("Error processing Excel file")