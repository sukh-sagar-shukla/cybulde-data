from cybulde.config_schemas.config_schema import Config
from cybulde.utils.config_utils import get_config
from cybulde.utils.data_utils import initialize_dvc, initialised_dvc_storage, commit_to_dvc
from cybulde.utils.utils import get_logger


@get_config(config_path="../configs", config_name="config")
def version_data(config: Config) -> None:
    # logger = get_logger(Path(__file__).name)
    initialize_dvc()
    initialised_dvc_storage(config.dvc_remote_name,config.dvc_remote_url)
    commit_to_dvc(config.dvc_raw_data_folder, config.dvc_remote_name)
    print(config)


if __name__ == "__main__":
    version_data()  # type: ignore
