from typing import Dict

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class PGSettings(BaseSettings):
    host: str = Field(alias="PGHOST")
    database: str = Field(alias="PGDATABASE")
    user: str = Field(alias="PGUSER")
    password: str = Field(alias="PGPASSWORD")
    port: str = Field(alias="PGPORT")

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    @property
    def database_link(self) -> str:
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"

    @property
    def database_creds(self) -> Dict[str, str]:
        return {
            "host": self.host,
            "database": self.database,
            "user": self.user,
            "password": self.password,
            "port": self.port,
        }
        
        
pg_settings = PGSettings()