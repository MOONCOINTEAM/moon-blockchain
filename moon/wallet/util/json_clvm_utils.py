from typing import Any

from moon.types.blockchain_format.program import Program


def json_to_moonlisp(json_data: Any) -> Any:
    list_for_moonlisp = []
    if isinstance(json_data, list):
        for value in json_data:
            list_for_moonlisp.append(json_to_moonlisp(value))
    else:
        if isinstance(json_data, dict):
            for key, value in json_data:
                list_for_moonlisp.append((key, json_to_moonlisp(value)))
        else:
            list_for_moonlisp = json_data
    return Program.to(list_for_moonlisp)
