import os
import shutil
from datetime import datetime
def backup_folder(source_dir, backup_dir):
    """
    Back up the contents of source_dir to backup_dir.

    :param source_dir: The directory to back up.
    :param backup_dir: The directory where the backup will be stored.
    """ 
    # Check if source_dir exists
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"The source directory '{source_dir}' does not exist.") 
    
    # Create a timestamped backup directory
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_subdir = os.path.join(backup_dir, f"backup_{timestamp}")
    os.makedirs(backup_subdir, exist_ok=True)
    # Copy the contents of source_dir to the backup directory
    try:
        shutil.copytree(source_dir, backup_subdir, dirs_exist_ok=True)
        print(f"Backup of '{source_dir}' created at '{backup_subdir}'")
    except Exception as e:
        raise RuntimeError(f"Failed to back up '{source_dir}': {e}")
    
source_dir = 'D:\A_DEV\Python'
    
backup_dir = 'D:\A_DEV\Python_bck'

backup_folder(source_dir, backup_dir)

    