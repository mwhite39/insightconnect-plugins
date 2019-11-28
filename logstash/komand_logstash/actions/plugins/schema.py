# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Retrieves information about all Logstash plugins that are currently installed"


class Input:
    pass

class Output:
    RESPONSE = "response"
    

class PluginsInput(komand.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class PluginsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "response": {
      "$ref": "#/definitions/response",
      "title": "Response",
      "description": "Response",
      "order": 1
    }
  },
  "definitions": {
    "response": {
      "type": "object",
      "title": "response",
      "properties": {
        "host": {
          "type": "string",
          "title": "Host",
          "order": 1
        },
        "http_address": {
          "type": "string",
          "title": "Http Address",
          "order": 3
        },
        "id": {
          "type": "string",
          "title": "Id",
          "order": 4
        },
        "name": {
          "type": "string",
          "title": "Name",
          "order": 5
        },
        "result": {
          "type": "object",
          "title": "Result",
          "order": 6
        },
        "version": {
          "type": "string",
          "title": "Version",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
