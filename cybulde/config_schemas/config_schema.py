from hydra.core.config_store import ConfigStore
from pydantic.dataclasses import dataclass


@dataclass
class Config:
    dvc_remote_name: str = "gdrive"
    dvc_remote_url: str = "gdrive://1c8x_dQpCHhsDAfYzmB08ceroW5kt1T-L"
    dvc_raw_data_folder: str = "data/raw"

def setup_config() -> None:
    cs = ConfigStore.instance()
    cs.store(name="config_schema", node=Config)
