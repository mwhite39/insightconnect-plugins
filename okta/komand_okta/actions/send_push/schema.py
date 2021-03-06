# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Push an MFA challenge to a user's device and wait for a success or rejection"


class Input:
    FACTOR_ID = "factor_id"
    USER_ID = "user_id"
    

class Output:
    FACTOR_STATUS = "factor_status"
    

class SendPushInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "factor_id": {
      "type": "string",
      "title": "Okta Factor ID",
      "description": "Factor ID of the user to push verification to",
      "order": 2
    },
    "user_id": {
      "type": "string",
      "title": "Okta User ID",
      "description": "User ID to push verification to",
      "order": 1
    }
  },
  "required": [
    "factor_id",
    "user_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SendPushOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "factor_status": {
      "type": "string",
      "title": "Factor Status",
      "description": "User factor status",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
