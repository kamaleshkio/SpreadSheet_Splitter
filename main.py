from gui.file_browser import choose_file, choose_output_folder
from modules.file_handler import process_excel_file
from modules.logger import get_logger

logger = get_logger(__name__)

def main():
    file_path = choose_file()
    if not file_path:
        logger.warning("No input file selected.")
        return

    output_folder = choose_output_folder()
    if not output_folder:
        logger.warning("No output folder selected.")
        return

    logger.info(f"Input file: {file_path}")
    logger.info(f"Output folder: {output_folder}")

    process_excel_file(file_path, output_folder)

if __name__ == "__main__":
    main()