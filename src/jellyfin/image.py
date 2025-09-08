"""
Module `image` - High-level interface for ImageApi.
"""
from __future__ import annotations

import os, requests, mimetypes, tempfile, uuid

from jellyfin.items import Item
from jellyfin.generated import ImageType, ImageApi

class Image():

    def __init__(self, api: Api):
        """Initializes the Image API wrapper.

        Args:
            api (Api): An instance of the Api class.
        """
        self.api = api
        self.image_api = api.generated.ImageApi(api.client)

    def upload_from_url(self, item: Item | str | uuid.UUID, image_type: ImageType, uri: str) -> bool:
        """
        Uploads an image for a given item.

        Args:
            item (Item | str | uuid.UUID): The item to upload the image for.
            image_type (ImageType): The type of the image (e.g., "Primary", "Backdrop").
            uri (str): The URI of the image file.

        Returns:
            bool: True if the upload was successful, False otherwise.
        """
        try:
            tmp = self.get_image_tmp(uri)
            self.upload_from_file(item, image_type, tmp)
            os.remove(tmp)
        except Exception as e:
            print(f"Failed to upload image: {e}")
            return False
        return True

    def upload_from_file(self, item: Item | str | uuid.UUID, image_type: ImageType, file_path: str) -> bool:
        """
        Uploads an image for a given item from a local file.

        Args:
            item (Item | str | uuid.UUID): The item to upload the image for.
            image_type (ImageType): The type of the image (e.g., "Primary", "Backdrop").
            file_path (str): The path to the local image file.

        Returns:
            bool: True if the upload was successful, False otherwise.
        """
        if isinstance(item, (str, uuid.UUID)):
            item = self.api.items.by_id(item)

        if item is None:
            raise ValueError("Item not found")
        
        if not isinstance(item, Item):
            raise ValueError(f"Invalid item type: {type(item)}")

        content_type, _ = mimetypes.guess_type(file_path)
        try:
            self.image_api.set_item_image(
                item.id,
                image_type,
                file_path,
                _content_type=content_type
            )
        except Exception as e:
            print(f"Failed to upload image: {e}")
            return False
        return True
        
    def get_image_tmp(self, uri: str) -> str:
        """ Downloads an image from a URI to a temporary file.

        Args:
            uri (str): The URI of the image to download.

        Returns:
            str: The path to the temporary file containing the downloaded image.
        """
        response = requests.get(uri)
        suffix = os.path.splitext(uri)[-1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp_file:
            tmp_file.write(response.content)
            tmp_file_path = tmp_file.name
            
        return tmp_file_path