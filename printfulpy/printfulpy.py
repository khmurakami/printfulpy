#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 8naldv9l-3gyz-cl2g:yv7r-pwgnxg8e5bjr

import requests
import wget
import json

# Create async requests
import asyncio
import aiofiles
import aiohttp


class PrintfulPy():

    def __init__(self, api_key):

        if api_key is None:
            raise Exception("No Client id inserted")

        self.root_url = "https://api.printful.com/"
        self.api_key = api_key

    def get_list_of_orders(self, status=None, offset=None, limit=100):

        """Get a list of all orders by filters. Default returns unfiltered orders

        Args:
            status (string): Filter orders by status
            offset (integer): Result by a certain offset
            limit (integer): Number of items per page

        Return:
            raw_json (dict): Raw results of the json

        """

        url = self.root_url + "/orders"

        data = {
            "status": str(status),
            "offset": str(integer),
            "limit": str(limit)
        }

        r = requests.get(url, params=data)
        raw_json = r.json()
        return raw_json

    # https://www.mapillary.com/developer/api-documentation/#pagination
    def get_product_list(self):

        """Get all of the printful products. (Not yours)

        Args:
            None

        Return:
            raw_json (dict): Dictionary of the result json requested

        """

        url = self.root_url + "/products"

        data = {}

        r = requests.get(url, params=data)
        raw_json = r.json()
        return raw_json

    def get_variant_info(self, variant_id=71):

        """Get information on the variant of a product

        Args:
            variant_id (int): The Variant ID. Not the product id

        Return:
            raw_json (dict): Dictionary of the raw request

        """

        url = self.root_url + "/products/variant/" + str(product_id) 

        data = {}

        r = requests.get(url, params=data)
        raw_json = r.json()
        return raw_json

    def get_product_variant_list(self, product_id=71):

        """Get all the variants of a product

        Args:
            product_id (int): The Product ID

        Return:
            raw_json (dict)

        """

        url = self.root_url + "/products/" + str(product_id)

        data = {}

        r = requests.get(url, params=data)
        raw_json = r.json()
        return raw_json
        

    def get_printfiles(self, product_id=71, orientation=None):

        """Get the type of prints a product can generate

        Args:
            product_id (int): Product ID of the item you want to get
            orientation (string): "horizontal" or "vertical" only for wall art product

        Return:
            raw_json (dict): 

        """

        url = self.root_url + "/mockup-generator/printfiles/" + str(product_id)

        data = {
            "orientation": orientation
        }

        r = requests.get(url, params=data)
        raw_json = r.json()
        return raw_json

    def get_layout_templates(self, product_id=72, orientation=None, technique=None):

        """Retrive list of templates that can be used for client-side positioning

        Args:
            product_id (int): The Product Id 
            orientation (String): Horizontal or Vertical
            techinque (String):

        Return:
            raw_json (dict):

        """

        url = self.root_url + "/mockup-generator/templates" + str(product_id)

        data = {
            "orientation": orientation,
            "technique": technique
        }

        r = requests.get(url, params=data)
        raw_json = r.json()
        print(raw_json)
        return raw_json


    def create_mockup_gen_task(self, product_id=71, image_url=None, variant_ids=None, format="jpg", width=None, product_options=None, option_groups=None, files=None):
        
        """Create a Mockup Generation Task

        Args:
            id (int): The Product ID
            varitant_ids (list of ints): The 
            format (string):
            width (int):
            product_options (list of strings):
            options_groups (list of strings):
            files (?)

        Return: 
            raw_json (dict):

        """

        # The Url for generating a task
        url = self.root_url + "/mockup-generator/create-task/" + str(product_id)

        data = {
            "variant_ids": str(variant_ids),
            "format": format,
            "files": [
                {
                    "placement": "front",
                    "image_url": image_url,
                    "position": {
                        "area_width": 1800,
                        "area_height": 2400,
                        "width": 1800,
                        "height": 1800,
                        "top": 300,
                        "left": 0
                    }
                },
                {
                    "placement": "back",
                    "image_url": image_url,
                    "position": {
                        "area_width": 1800,
                        "area_height": 2400,
                        "width": 1800,
                        "height": 1800,
                        "top": 300,
                        "left": 0
                    }
                }
            ]
        }

        r = requests.post(url, params=data)
        raw_json = r.json()
        return raw_json


if __name__ == "__main__":

    client = PrintfulPy(api_key="8naldv9l-3gyz-cl2g:yv7r-pwgnxg8e5bjr")
    raw_json = client.create_mockup_gen_task(variant_ids=[4012, 4013], image_url="https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwi6sbChjt3mAhWUsJ4KHVMpBKMQjRx6BAgBEAQ&url=https%3A%2F%2Fwww.amazon.com%2FPeppermint-Tiffany-Young%2Fdp%2FB07KLYJ31F&psig=AOvVaw0qf5u2h1CHaqfrAfKh8Yle&ust=1577786331733378")
    with open("mock_up_json.json", "w") as data_file:
        json.dump(raw_json, data_file, indent=4, sort_keys=True)
