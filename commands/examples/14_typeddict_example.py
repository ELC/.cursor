from typing import TypedDict


class ConfigDict(TypedDict):
    host: str
    port: int
    debug: bool


@pytest.fixture
def server_config() -> ConfigDict:
    return {"host": "localhost", "port": 8000, "debug": True}


def test_server_starts_with_config(server_config: ConfigDict) -> None:
    from server import start_server

    result: bool = start_server(server_config)

    assert result is True

