# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Capture URL screenshot"


class Input:
    CACHE_AGE_DAYS = "cache_age_days"
    FORMAT = "format"
    SIZE = "size"
    TIMEOUT = "timeout"
    URL = "url"
    

class Output:
    SCREENSHOT = "screenshot"
    URL = "url"
    

class CaptureInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "cache_age_days": {
      "type": "integer",
      "title": "Cache Age Days",
      "description": "Use Cached Image From X days ago. Enter in the age in days that will be accepted. 0 means do not use cache",
      "default": 0,
      "enum": [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14
      ],
      "order": 4
    },
    "format": {
      "type": "string",
      "title": "Format",
      "description": "Format",
      "default": "JPG",
      "enum": [
        "JPG",
        "PNG",
        "GIF"
      ],
      "order": 3
    },
    "size": {
      "type": "string",
      "title": "Size",
      "description": "Size string. Sizes are listed here: https://screenshotmachine.com/apiguide.php",
      "default": "tiny",
      "enum": [
        "tiny",
        "small",
        "seminormal",
        "normal",
        "medium",
        "large",
        "extra_large",
        "full",
        "mobile_normal",
        "mobile_full"
      ],
      "order": 2
    },
    "timeout": {
      "type": "integer",
      "title": "Timeout",
      "description": "Timeout in ms to wait for capture",
      "default": 200,
      "enum": [
        0,
        200,
        400,
        600,
        800,
        1000
      ],
      "order": 5
    },
    "url": {
      "type": "string",
      "title": "URL",
      "description": "URL to screenshot",
      "order": 1
    }
  },
  "required": [
    "url"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CaptureOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "screenshot": {
      "$ref": "#/definitions/file",
      "title": "Screenshot",
      "description": "Screenshot Captured",
      "order": 2
    },
    "url": {
      "type": "string",
      "title": "URL",
      "description": "URL Captured",
      "order": 1
    }
  },
  "definitions": {
    "file": {
      "id": "file",
      "type": "object",
      "title": "File",
      "description": "File Object",
      "properties": {
        "content": {
          "type": "string",
          "title": "Content",
          "description": "File contents",
          "format": "bytes"
        },
        "filename": {
          "type": "string",
          "title": "Filename",
          "description": "Name of file"
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
