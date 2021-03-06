# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Updates a specified cell in Google Sheets with new data"


class Input:
    CELL = "cell"
    SHEET_ID = "sheet_id"
    UPDATE = "update"
    WORKSHEET = "worksheet"
    

class Output:
    UPDATE_INFORMATION = "update_information"
    VALUE = "value"
    

class UpdateCellInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "cell": {
      "type": "string",
      "title": "Cell",
      "description": "The cell to update e.g. A1, B6, C55, etc",
      "order": 2
    },
    "sheet_id": {
      "type": "string",
      "title": "Sheet ID",
      "description": "The ID of the spreadsheet to update",
      "order": 1
    },
    "update": {
      "type": "string",
      "title": "Update",
      "description": "The data to update the cell with",
      "order": 3
    },
    "worksheet": {
      "type": "string",
      "title": "Worksheet",
      "description": "The worksheet to update e.g. Sheet1",
      "order": 4
    }
  },
  "required": [
    "cell",
    "sheet_id",
    "update",
    "worksheet"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UpdateCellOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "update_information": {
      "$ref": "#/definitions/update",
      "title": "Update Information",
      "description": "Information on the update performed",
      "order": 2
    },
    "value": {
      "type": "string",
      "title": "Value",
      "description": "The value of the updated cell",
      "order": 1
    }
  },
  "definitions": {
    "update": {
      "type": "object",
      "title": "update",
      "properties": {
        "spreadsheetId": {
          "type": "string",
          "title": "Spreadsheet ID",
          "description": "The ID of the updated spreadsheet",
          "order": 1
        },
        "updatedCells": {
          "type": "integer",
          "title": "Updated Cells",
          "description": "The number of cells updated",
          "order": 5
        },
        "updatedColumns": {
          "type": "integer",
          "title": "Updated Columns",
          "description": "The number of columns updated",
          "order": 4
        },
        "updatedRange": {
          "type": "string",
          "title": "Updated Range",
          "description": "The worksheet and range updated e.g. Sheet1!A1",
          "order": 2
        },
        "updatedRows": {
          "type": "integer",
          "title": "Updated Rows",
          "description": "The number of rows updated",
          "order": 3
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
