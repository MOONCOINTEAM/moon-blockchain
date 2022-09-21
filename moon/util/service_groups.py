from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": (
        "moon_harvester moon_timelord_launcher moon_timelord moon_farmer "
        "moon_full_node moon_wallet moon_data_layer moon_data_layer_http"
    ).split(),
    # TODO: should this be `data_layer`?
    "data": "moon_wallet moon_data_layer".split(),
    "data_layer_http": "moon_data_layer_http".split(),
    "node": "moon_full_node".split(),
    "harvester": "moon_harvester".split(),
    "farmer": "moon_harvester moon_farmer moon_full_node moon_wallet".split(),
    "farmer-no-wallet": "moon_harvester moon_farmer moon_full_node".split(),
    "farmer-only": "moon_farmer".split(),
    "timelord": "moon_timelord_launcher moon_timelord moon_full_node".split(),
    "timelord-only": "moon_timelord".split(),
    "timelord-launcher-only": "moon_timelord_launcher".split(),
    "wallet": "moon_wallet".split(),
    "introducer": "moon_introducer".split(),
    "simulator": "moon_full_node_simulator".split(),
    "crawler": "moon_crawler".split(),
    "seeder": "moon_crawler moon_seeder".split(),
    "seeder-only": "moon_seeder".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
