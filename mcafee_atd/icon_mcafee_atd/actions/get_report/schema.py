# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Download the report of an analysis"


class Input:
    ID = "id"
    REPORT_TYPE = "report_type"
    TYPE_ID = "type_id"
    

class Output:
    FILE = "file"
    REPORT = "report"
    

class GetReportInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "ID",
      "description": "The Task ID, job ID, or MD5 value for the prepared analysis report",
      "order": 1
    },
    "report_type": {
      "type": "string",
      "title": "Report Type",
      "description": "The file type of the report to return in the file output",
      "default": "HTML",
      "enum": [
        "HTML",
        "TXT",
        "ZIP",
        "XML",
        "IOC",
        "STIX",
        "PDF",
        "SAMPLE"
      ],
      "order": 3
    },
    "type_id": {
      "type": "string",
      "title": "Type ID",
      "description": "Type of given ID parameter, the type must match the value of the ID field. The default value is MD5",
      "default": "MD5",
      "enum": [
        "MD5",
        "TASK ID",
        "JOB ID"
      ],
      "order": 2
    }
  },
  "required": [
    "id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetReportOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "file": {
      "type": "string",
      "title": "File",
      "displayType": "bytes",
      "description": "Prepared analysis report",
      "format": "bytes",
      "order": 1
    },
    "report": {
      "type": "object",
      "title": "Report",
      "description": "Return report in JSON",
      "order": 2
    }
  },
  "required": [
    "file"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
