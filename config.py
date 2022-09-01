# -*- coding: utf-8 -*-

import yaml
from pprint import pprint

yaml_file = "conf/config.yaml"


def config():
    with open(yaml_file, 'r', encoding='UTF-8') as f:
        return yaml.safe_load(f)


if __name__ == '__main__':
    pprint(config())
    pprint(config().get("room_list"))
