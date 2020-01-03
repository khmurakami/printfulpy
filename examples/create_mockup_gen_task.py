#!/usr/bin/env python
# -*- coding: utf-8 -*-

from printfulpy import PrintfulPy

import json

client = PrintfulPy(api_key="8naldv9l-3gyz-cl2g:yv7r-pwgnxg8e5bjr")
raw_json = client.create_mockup_gen_task(variant_ids=[
    4012, 4013], image_url="http://cute-n-tiny.com/wp-content/uploads/2010/12/cute-baby-gentoo-penguin-400x266.jpg")
with open("mock_up_json.json", "w") as data_file:
        json.dump(raw_json, data_file, indent=4, sort_keys=True)
