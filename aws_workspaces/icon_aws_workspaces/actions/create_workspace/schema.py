# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Create a workspace"


class Input:
    BUNDLE_ID = "bundle_id"
    DIRECTORY_ID = "directory_id"
    ROOT_VOLUME_ENCRYPTION_ENABLED = "root_volume_encryption_enabled"
    TAGS = "tags"
    USER_VOLUME_ENCRYPTION_ENABLED = "user_volume_encryption_enabled"
    USERNAME = "username"
    VOLUME_ENCRYPTION_KEY = "volume_encryption_key"
    WORKSPACE_PROPERTIES = "workspace_properties"
    

class Output:
    WORKSPACE_ID_STATE = "workspace_id_state"
    

class CreateWorkspaceInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "bundle_id": {
      "type": "string",
      "title": "Bundle ID",
      "description": "The identifier of the bundle for the workspace",
      "order": 3
    },
    "directory_id": {
      "type": "string",
      "title": "Directory ID",
      "description": "The identifier of the AWS Directory Service directory for the workspace",
      "order": 1
    },
    "root_volume_encryption_enabled": {
      "type": "boolean",
      "title": "Root Volume Encryption Enabled",
      "description": "Flag indicating whether the data stored on the root volume is encrypted",
      "order": 6
    },
    "tags": {
      "type": "array",
      "title": "Tags",
      "description": "Tags",
      "items": {
        "$ref": "#/definitions/tag"
      },
      "order": 8
    },
    "user_volume_encryption_enabled": {
      "type": "boolean",
      "title": "User Volume Encryption Enabled",
      "description": "Flag indicating whether the data stored on the user volume is encrypted",
      "order": 5
    },
    "username": {
      "type": "string",
      "title": "Username",
      "description": "The username of the user for the workspace",
      "order": 2
    },
    "volume_encryption_key": {
      "type": "string",
      "title": "Volume Encryption Key",
      "description": "The KMS key used to encrypt data stored on your workspace",
      "order": 4
    },
    "workspace_properties": {
      "$ref": "#/definitions/workspace_properties",
      "title": "Workspace Properties",
      "description": "Workspace properties",
      "order": 7
    }
  },
  "required": [
    "bundle_id",
    "directory_id",
    "username"
  ],
  "definitions": {
    "tag": {
      "type": "object",
      "title": "tag",
      "properties": {
        "key": {
          "type": "string",
          "title": "Key",
          "description": "The key in a key-value pair of a tag",
          "order": 1
        },
        "value": {
          "type": "string",
          "title": "Value",
          "description": "The value in a key-value pair of a tag",
          "order": 2
        }
      }
    },
    "workspace_properties": {
      "type": "object",
      "title": "workspace_properties",
      "properties": {
        "compute_type_name": {
          "type": "string",
          "title": "Compute Type Name",
          "description": "Compute type name",
          "enum": [
            "VALUE",
            "STANDARD",
            "PERFORMANCE",
            "POWER",
            "GRAPHICS",
            "POWERPRO",
            "GRAPHICSPRO"
          ],
          "order": 5
        },
        "root_volume_size": {
          "type": "integer",
          "title": "Root Volume Size",
          "description": "Root volume size in gigabytes",
          "default": 80,
          "order": 3
        },
        "running_mode": {
          "type": "string",
          "title": "Running Mode",
          "description": "Running mode",
          "enum": [
            "ALWAYS_ON",
            "AUTO_STOP"
          ],
          "order": 1
        },
        "running_mode_auto_stop_time_out": {
          "type": "integer",
          "title": "Running Mode Auto Stop Time Out",
          "description": "Running mode auto stop time out in minutes. It should be a multiple of 60",
          "default": 60,
          "order": 2
        },
        "user_volume_size": {
          "type": "integer",
          "title": "User Volume Size",
          "description": "User volume size in gigabytes",
          "default": 10,
          "order": 4
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateWorkspaceOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "workspace_id_state": {
      "$ref": "#/definitions/workspace_id_state",
      "title": "Workspace ID and State",
      "description": "ID and state of a created workspace",
      "order": 1
    }
  },
  "required": [
    "workspace_id_state"
  ],
  "definitions": {
    "workspace_id_state": {
      "type": "object",
      "title": "workspace_id_state",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID of a created workspace",
          "order": 1
        },
        "state": {
          "type": "string",
          "title": "State",
          "description": "Current status of a created workspace",
          "order": 2
        }
      },
      "required": [
        "id",
        "state"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
