# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Updates the role of the user in actual organization"


class Input:
    ORGANIZATION_ID = "organization_id"
    ROLE = "role"
    USER_ID = "user_id"
    

class Output:
    MESSAGE = "message"
    SUCCESS = "success"
    

class UpdateOrganizationUserInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "organization_id": {
      "type": "integer",
      "title": "Organization ID",
      "description": "Unique ID of the organization eg. 123 (-1 implies current)",
      "default": -1,
      "order": 1
    },
    "role": {
      "type": "string",
      "title": "User Role",
      "description": "New role for the user",
      "enum": [
        "Admin",
        "Editor",
        "Viewer"
      ],
      "order": 3
    },
    "user_id": {
      "type": "integer",
      "title": "User ID",
      "description": "Unique ID of the user eg. 123",
      "order": 2
    }
  },
  "required": [
    "role",
    "user_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UpdateOrganizationUserOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "message": {
      "type": "string",
      "title": "Message",
      "description": "Grafana API response, if any",
      "order": 2
    },
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "True, if the user was updated",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
