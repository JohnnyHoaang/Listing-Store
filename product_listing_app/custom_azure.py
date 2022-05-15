from storages.backends.azure_storage import AzureStorage
import os
class AzureMediaStorage(AzureStorage):
    account_name = os.environ['AZURE_STORAGE_ACCOUNT_NAME']
    account_key = os.environ['AZURE_STORAGE_KEY'] 
    azure_container = 'media'
    expiration_secs = None
