import socket
import logging
import subprocess

def get_logger(name:str) -> logging.Logger:
    return logging.getLogger(f"[{socket.gethostname()}] {name}")

def run_shell_command(cmd: str) -> str:
    return subprocess.run(cmd, text=True, shell=True, capture_output=True).stdout