from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    `ftm-transcribe` settings management using
    [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)

    Note:
        All settings can be set via environment variables in uppercase,
        prepending `FTMTR_` (except for those with a given prefix)

    """

    model_config = SettingsConfigDict(env_prefix="ftmtr_")

    # language
    # model
