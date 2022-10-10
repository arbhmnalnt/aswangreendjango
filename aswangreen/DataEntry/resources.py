from import_export import resources
from .models import *




class ClientResources(resources.ModelResources):
    class Meta:
        model = Client