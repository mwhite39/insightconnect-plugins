# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Search for events"


class Input:
    ANALYSIS = "analysis"
    DATE_FROM = "date_from"
    DATE_UNTIL = "date_until"
    EVENT = "event"
    ORGANIZATION = "organization"
    PUBLISHED = "published"
    TAG = "tag"
    THREAT_LEVEL = "threat_level"
    

class Output:
    EVENT_LIST = "event_list"
    

class SearchEventsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "analysis": {
      "type": "string",
      "title": "Analysis",
      "description": "Search by analysis level",
      "enum": [
        "Don't search on",
        "Initial",
        "Ongoing",
        "Completed"
      ],
      "order": 8
    },
    "date_from": {
      "type": "string",
      "title": "Date",
      "description": "Search after this date e.g. 2018-03-22",
      "order": 3
    },
    "date_until": {
      "type": "string",
      "title": "Date Until",
      "description": "Search before this date e.g. 2018-03-22",
      "order": 4
    },
    "event": {
      "type": "string",
      "title": "Event",
      "description": "Search by event ID",
      "order": 1
    },
    "organization": {
      "type": "string",
      "title": "Organization",
      "description": "Search by organization",
      "order": 7
    },
    "published": {
      "type": "string",
      "title": "Published",
      "description": "Search by if published",
      "enum": [
        "Don't search on",
        "True",
        "False"
      ],
      "order": 6
    },
    "tag": {
      "type": "string",
      "title": "Tag",
      "description": "Search by tag",
      "order": 2
    },
    "threat_level": {
      "type": "string",
      "title": "Threat Level",
      "description": "Search by threat level",
      "enum": [
        "Don't search on",
        "Undefined",
        "Low",
        "Medium",
        "High"
      ],
      "order": 5
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SearchEventsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "event_list": {
      "type": "array",
      "title": "Event List",
      "description": "A list of event IDs that match the search",
      "items": {
        "type": "string"
      },
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
