# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/file/apm/aaa/ping-access-properties-files' resources
# =============================================


class FileApmPingaccesspropertiesfilesSchema(MetaParser):

    schema = {}


class FileApmPingaccesspropertiesfiles(FileApmPingaccesspropertiesfilesSchema):
    """ To F5 resource for /mgmt/tm/file/apm/aaa/ping-access-properties-files
    """

    cli_command = "/mgmt/tm/file/apm/aaa/ping-access-properties-files"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
