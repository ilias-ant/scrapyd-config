class ScrapydConfigError(Exception):
    """Base class for scrapyd-config exceptions."""


class UndefinedEnvError(Exception):
    """Error raised when provided env value does not have a corresponding scrapyd-config.yml value."""
