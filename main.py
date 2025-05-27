from gui.file_browser import Choose_file, Choose_output_folder
from modules.file_handler import process_excel_file
from modules.logger import get_logger
logger = get_logger(__name__)

def main():
    file_path = Choose_file()
    if not file_path:
        logger.warning("Files Not Selected. please select a file.")
        return
    
    output_folder = Choose_output_folder()
    if not output_folder:
        logger.warning("Output folder not selected. Please select an output folder.")
        return
    
    logger.info(f"Selected File:{file_path}")
    logger.info(f"Choosen Output Folder: {output_folder}")

    process_excel_file(file_path, output_folder)

    if __name__ == "main":
        main()
        logger.info("Processing completed successfully.")