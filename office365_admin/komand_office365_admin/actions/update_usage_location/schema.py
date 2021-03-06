# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Updates usage location for a given user"


class Input:
    LOCATION = "location"
    USER_PRINCIPAL_NAME = "user_principal_name"
    

class Output:
    SUCCESS = "success"
    

class UpdateUsageLocationInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "location": {
      "type": "string",
      "title": "Usage Location",
      "description": "A two letter country code (ISO standard 3166)",
      "order": 1
    },
    "user_principal_name": {
      "type": "string",
      "title": "User Principal Name",
      "description": "The user principal name to update e.g. user@example.com",
      "order": 2
    }
  },
  "required": [
    "location",
    "user_principal_name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UpdateUsageLocationOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "True if successful",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
