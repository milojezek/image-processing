import logging

from azure.core.exceptions import ResourceNotFoundError
from azure.storage.blob import BlobClient, BlobServiceClient

from .azure_storage_config import AZURE_STORAGE_CONNECTION_STRING

def get_blob_as_bytes(container_name: str, blob_name: str) -> bytes:
    """
    Get an Azure storage blob named `blob_name` from `container_name` container and return it as bytes.

    :raises ValueError: If `AZURE_STORAGE_CONNECTION_STRING` environment variable is not set.
    :raises NameError: If the requested file was not found on Azure Storage.
    """
    conn_str = AZURE_STORAGE_CONNECTION_STRING
    if not conn_str:
        raise ValueError("`AZURE_STORAGE_CONNECTION_STRING` environment variable is not set.")

    blob_client = BlobClient.from_connection_string(conn_str, container_name=container_name, blob_name=blob_name)
    try:
        # The Azure client has some implicit retry mechanism.
        return blob_client.download_blob().readall()
    except ResourceNotFoundError as err:
        logging.exception(f"File {container_name}/{blob_name} not found.")
        raise NameError(f"Scan not found. Requested file ({blob_name}) was not found on Azure Storage.") from err


def list_containers() -> list[str]:
    """
    List all containers in the Azure Storage account.

    :raises ValueError: If `AZURE_STORAGE_CONNECTION_STRING` environment variable is not set.
    """
    conn_str = AZURE_STORAGE_CONNECTION_STRING
    if not conn_str:
        raise ValueError("`AZURE_STORAGE_CONNECTION_STRING` environment variable is not set.")

    blob_service_client = BlobServiceClient.from_connection_string(conn_str)
    return [container.name for container in blob_service_client.list_containers()]