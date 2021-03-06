# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Query shipping address info"


class Input:
    ADDRESS = "address"
    SHIPPING_ADDRESS = "shipping_address"
    SHIPPING_ADDRESS_2 = "shipping_address_2"
    SHIPPING_CITY = "shipping_city"
    SHIPPING_COMPANY = "shipping_company"
    SHIPPING_COUNTRY = "shipping_country"
    SHIPPING_DELIVERY_SPEED = "shipping_delivery_speed"
    SHIPPING_FIRST_NAME = "shipping_first_name"
    SHIPPING_LAST_NAME = "shipping_last_name"
    SHIPPING_PHONE_COUNTRY_CODE = "shipping_phone_country_code"
    SHIPPING_PHONE_NUMBER = "shipping_phone_number"
    SHIPPING_POSTAL = "shipping_postal"
    SHIPPING_REGION = "shipping_region"
    

class Output:
    RISK_SCORE = "risk_score"
    SHIPPING_RESULT = "shipping_result"
    

class ShippingLookupInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address": {
      "type": "string",
      "title": "IP Address",
      "description": "IP address to query",
      "order": 1
    },
    "shipping_address": {
      "type": "string",
      "title": "Shipping Address",
      "description": "Shipping address line 1",
      "order": 5
    },
    "shipping_address_2": {
      "type": "string",
      "title": "Shipping Address 2",
      "description": "Shipping address line 2",
      "order": 6
    },
    "shipping_city": {
      "type": "string",
      "title": "City",
      "description": "City of shipping address",
      "order": 7
    },
    "shipping_company": {
      "type": "string",
      "title": "Company Name",
      "description": "Company name in shipping info",
      "order": 4
    },
    "shipping_country": {
      "type": "string",
      "title": "Country Code",
      "description": "Two character country code",
      "order": 9
    },
    "shipping_delivery_speed": {
      "type": "string",
      "title": "Delivery Speed",
      "description": "Shipping Delivery Speed",
      "enum": [
        "none",
        "same_day",
        "overnight",
        "expedited",
        "standard"
      ],
      "order": 13
    },
    "shipping_first_name": {
      "type": "string",
      "title": "First Name",
      "description": "First name in shipping info",
      "order": 2
    },
    "shipping_last_name": {
      "type": "string",
      "title": "Last Name",
      "description": "Last name in shipping info",
      "order": 3
    },
    "shipping_phone_country_code": {
      "type": "string",
      "title": "Phone Country Code",
      "description": "Country code for phone number",
      "order": 12
    },
    "shipping_phone_number": {
      "type": "string",
      "title": "Phone Number",
      "description": "Phone number without country code",
      "order": 11
    },
    "shipping_postal": {
      "type": "string",
      "title": "Postal Code",
      "description": "Postal Code in shipping address",
      "order": 10
    },
    "shipping_region": {
      "type": "string",
      "title": "Region Code",
      "description": "Subdivision code in shipping address",
      "order": 8
    }
  },
  "required": [
    "address"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ShippingLookupOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "risk_score": {
      "type": "string",
      "title": "Risk Score",
      "description": "Overall risk score",
      "order": 2
    },
    "shipping_result": {
      "$ref": "#/definitions/shipping",
      "title": "Shipping Result",
      "description": "Results for shipping",
      "order": 1
    }
  },
  "definitions": {
    "shipping": {
      "type": "object",
      "title": "shipping",
      "properties": {
        "distance_to_billing_address": {
          "type": "integer",
          "title": "Distance To Billing Address",
          "description": "Distance to billing address",
          "order": 6
        },
        "distance_to_ip_location": {
          "type": "integer",
          "title": "Distance To Ip Location",
          "description": "Distance to IP location",
          "order": 5
        },
        "is_high_risk": {
          "type": "boolean",
          "title": "Is High Risk",
          "description": "Is shipping address high risk",
          "order": 1
        },
        "is_ip_in_country": {
          "type": "boolean",
          "title": "Is Ip In Country",
          "description": "Is IP in country",
          "order": 7
        },
        "is_postal_in_city": {
          "type": "boolean",
          "title": "Is Postal In City",
          "description": "Is postal code in city",
          "order": 2
        },
        "latitude": {
          "type": "string",
          "title": "Latitude",
          "description": "Latitude for shipping address",
          "order": 3
        },
        "longitude": {
          "type": "string",
          "title": "Longitude",
          "description": "Longitude for shipping address",
          "order": 4
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
