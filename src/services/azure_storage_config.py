import os

PROTOCOL = "DefaultEndpointsProtocol=https"
ACCOUNT_NAME = "AccountName=" + os.getenv("AZURE_STORAGE_ACCOUNT_NAME")
ACCOUNT_KEY = "AccountKey=" + os.getenv("AZURE_STORAGE_ACCOUNT_KEY")
STORAGE_SUFFIX = "EndpointSuffix=" + os.getenv("AZURE_STORAGE_SUFFIX")

AZURE_STORAGE_CONNECTION_STRING = f"{PROTOCOL};{ACCOUNT_NAME};{ACCOUNT_KEY};{STORAGE_SUFFIX}"