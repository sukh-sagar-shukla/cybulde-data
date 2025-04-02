from pathlib import Path
from cybulde.utils.utils import run_shell_command, get_logger

DATA_UTILS_LOGGER = get_logger(Path(__file__).name)

def is_dvc_initialized()->bool:
    return (Path().cwd() / ".dvc").exists()

def initialize_dvc()->None:
    if is_dvc_initialized():
        DATA_UTILS_LOGGER.info("DVC is already initialised")
        return
        
    DATA_UTILS_LOGGER.info("Initializing DVC")
    run_shell_command("dvc init")
    run_shell_command("dvc config core.analytics false")
    run_shell_command("dvc config core.autostage true")
    run_shell_command("git add .dvc")
    run_shell_command("git commit -nm 'Initialized DVC'")

    DATA_UTILS_LOGGER.info("Finished Initializing DVC")