#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Standard Libraries
from base64 import standard_b64encode
import json

# Third Party Libraries
import requests
import wget


# Create async requests
# import asyncio
# import aiofiles
# import aiohttp


class PrintfulPy():

    def __init__(self, api_key):

        if api_key is None:
            raise Exception("No Client id inserted")

        self.root_url = "https://api.printful.com/"
        self.key = bytearray(api_key, 'utf-8')
        self.headers = {'Content-Type': 'application/json',
                        'Authorization': "Basic {0}".format(self._auth())}

    def _auth(self):
        return standard_b64encode(self.key).decode('ascii')

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
            "offset": str(offset),
            "limit": str(limit)
        }

        r = requests.get(url, params=data)
        raw_json = r.json()
        return raw_json

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
        url = self.root_url + "mockup-generator/create-task/" + str(product_id)
        print(url)

        data = {
            "variant_ids": variant_ids,
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

        print(data)
        print(self.headers)

        r = requests.post(url, data=json.dumps(data), headers=self.headers)
        raw_json = r.json()
        return raw_json
    
    def get_mockup_gen_task_result(self, task_key):

        """Check the status of the task

        Args:
            task_key (string): The task key from creating a mockup to see the status of the url

        Return:
            raw_json (dict): The raw output of the json

        """

        url = self.root_url + "mockup-generator/task"

        print(url)

        data = {
            "task_key": task_key
        }

        r = requests.get(url, params=data, headers=self.headers)
        raw_json = r.json()
        print(raw_json)
        return raw_json

    def get_list_sync_products(self, status="all", search=None, offset=None, limit=100):

        """Get a list of Sync Products

        Args:
            status (String): Filter items by status. "synced", "unsynced", "all"
            search (String): Product search needle
            offset (integer): Result set offset
            limit (integer): Number of items per page (max 100)

        Return:
            raw_json (dict): The raw output of the json

        """

        url = self.root_url + "store/products"

        print(url)

        data = {
            "status": status,
            "search": search,
            "offset": offset,
            "limit": limit
        }

        r = requests.get(url, params=data, headers=self.headers)
        raw_json = r.json()
        print(raw_json)
        return raw_json

    def get_list_of_files(self, status=None, offset=None, limit=10):

        """Get of your files that you uploaded to the file libarry

        Args:
            status (String): Filter items by file status
            offset (integer): Result set offset
            limit (integer): Number of items per page (max 100)

        Return:
            raw_json (dict): The raw output of the json

        """

        url = self.root_url + "files"

        print(url)

        data = {
            "status": status,
            "offset": offset,
            "limit": limit
        }

        r = requests.get(url, params=data, headers=self.headers)
        raw_json = r.json()
        print(raw_json)
        return raw_json

    def get_layout_templates(self, product_id, orientation=None, technique=None):

        """Get of your files that you uploaded to the file libarry

        Args:
            status (String): Filter items by file status
            offset (integer): Result set offset
            limit (integer): Number of items per page (max 100)

        Return:
            raw_json (dict): The raw output of the json

        """

        url = self.root_url + "mockup-generator/templates/{0}".format(product_id)

        print(url)

        data = {
            "status": product_id,
            "orientation": orientation,
            "technique": technique
        }

        r = requests.get(url, params=data, headers=self.headers)
        raw_json = r.json()
        print(raw_json)
        return raw_json

    def get_product_variant_printfiles(self, product_id, orientation=None, technique=None):

        """Retrieve product variant printfiles

        Args:
            product_id (String): Product ID
            orientation (String): 
            technique (String):

        Return:
            raw_json (dict):

        """

        url = self.root_url + "mockup-generator/printfiles/{0}".format(product_id)

        print(url)

        data = {
            "product_id": product_id,
            "orientation": orientation,
            "technique": technique
        }

        r = requests.get(url, params=data, headers=self.headers)
        raw_json = r.json()
        print(raw_json)
        return raw_json

    def upload_new_file(self, file_name, image_url):

        # The Url for generating a task
        url = self.root_url + "files"
        print(url)

        data = {
            "type": "preview",
            "url": image_url,
            "filename": file_name
        }

        print(data)
        print(self.headers)

        r = requests.post(url, data=json.dumps(data), headers=self.headers)
        raw_json = r.json()
        return raw_json

    def create_new_sync_product(self, product_name="example_tshirt", variant_id=4012, retail_price=25.0, file_url=None):

        """Create a new product in your store

        Args:
            product_name (String): The name of the product
            variant_id (int): The product you are trying to create
            retail_price (float): The price you are trying to price it at
            file_url (String): The path to which to png file is located 

        """

        # The Url for generating a task
        url = self.root_url + "store/products"
        print(url)

        data = {
                "sync_product":{
                    "name": product_name
                },
                "sync_variants":[
                    {
                        "variant_id": variant_id,
                        "files":[
                            {
                                "url": file_url
                            }
                        ],
                    }
                ]
            }

        print(data)
        print(self.headers)

        r = requests.post(url, data=json.dumps(data), headers=self.headers)
        raw_json = r.json()
        return raw_json


if __name__ == "__main__":

    client = PrintfulPy(api_key="8naldv9l-3gyz-cl2g:yv7r-pwgnxg8e5bjr")
    # raw_json = client.create_mockup_gen_task(variant_ids=[4012], image_url="https://firebasestorage.googleapis.com/v0/b/tshirtai.appspot.com/o/temp.jpg?alt=media&token=83b0cbaa-9bd3-44db-8bcf-e31feefe3b98")
    # with open("mock_up_json.json", "w") as data_file:
    #     json.dump(raw_json, data_file, indent=4, sort_keys=True)

    # raw_json = client.get_mockup_gen_task_result("z5400ae1e4db7a924c7901254c7143e4")
    # with open("mock_up_result_json", "w") as data_file:
    #     json.dump(raw_json, data_file, indent=4, sort_keys=True)

    # raw_json = client.get_product_list()
    # with open("mock_up_json.json", "w") as data_file:
    #     json.dump(raw_json, data_file, indent=4, sort_keys=True)

    # raw_json = client.get_product_variant_printfiles(71)
    # with open("printfiles.json", "w") as data_file:
    #     json.dump(raw_json, data_file, indent=4, sort_keys=True)

    # raw_json = client.get_list_sync_products()
    # with open("sync_products.json", "w") as data_file:
    #     json.dump(raw_json, data_file, indent=4, sort_keys=True)

    google_download_link = "https://storage.googleapis.com/tshirt_pictures/parrot_water_color_test_1.png"
    # raw_json = client.upload_new_file(google_download_link)
    # with open("upload_file.json", "w") as data_file:
    #     json.dump(raw_json, data_file, indent=4, sort_keys=True)

    raw_json = client.create_new_sync_product(file_url=google_download_link)
    with open("create_sync_product.json", "w") as data_file:
        json.dump(raw_json, data_file, indent=4, sort_keys=True)


