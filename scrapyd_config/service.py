import configparser

import yaml

from . import utils


class ScrapydConfigService(object):
    def __init__(self):

        self.yml_filepath = "scrapyd-config.yml"

    def generate_conf_file(self, env: str, output_dir: str) -> None:

        yml_file = self._get_yml_file()

        conf_file = configparser.ConfigParser()

        for key, value in yml_file.get("base", {}).items():

            if value is None:
                continue

            if isinstance(value, dict):
                conf_file[key] = {}

                for subkey, subvalue in value.items():
                    conf_file[key][subkey] = str(subvalue)

            else:
                conf_file[key] = value

        try:
            env_keyvalues = yml_file[env]
        except KeyError:
            raise utils.UndefinedEnvError(
                f"provided env value does not have a corresponding scrapyd-config.yml value: {env}"
            ) from None

        for key, value in env_keyvalues.items():

            if value is None:
                continue

            if isinstance(value, dict):

                for subkey, subvalue in value.items():
                    conf_file[key][subkey] = str(subvalue)

            else:
                conf_file[key] = value

        with open(f"{output_dir}/scrapyd.conf", "w") as configfile:
            conf_file.write(configfile)

    def _get_yml_file(self) -> dict:

        with open(self.yml_filepath, "r") as stream:
            return yaml.safe_load(stream)
