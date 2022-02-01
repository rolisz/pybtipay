import datetime
import json

import requests as requests

from btipay.exceptions import BTIPayException
from btipay.responses import PaymentRegistration, PaymentStatus


class BTIPayClient:

    def __init__(self, base_url, username, password):
        self._base_url = base_url
        self._username = username
        self._password = password

    def register_payment(self, order_number, amount, description, return_url, email, phone,
                         city, address, delivery_type='Comanda'):
        params = {
            "userName": self._username,
            "password": self._password,
            "orderNumber": order_number,
            "amount": amount,
            "currency": 946,
            "description": description,
            "returnUrl": return_url,
            "jsonParams": json.dumps({"FORCE_3DS2": True}),
            "orderBundle": json.dumps(
                {"orderCreationDate": datetime.date.today().isoformat(),
                 "customerDetails": {
                     "email": email,
                     "phone": phone,  # This needs.. processing probably
                     "deliveryInfo": {
                         "deliveryType": delivery_type,
                         "country": 642,
                         "city": city,
                         "postAddress": address,
                     },
                     "billingInfo": {
                         "country": 642,
                         "city": city,
                         "postAddress": address,
                     }
                 }})
        }
        url = f"{self._base_url}payment/rest/register.do"
        resp = requests.get(url, params=params)
        if resp:
            result = resp.json()
            if 'errorCode' in result:
                raise BTIPayException(result)
            return PaymentRegistration(orderId=result['orderId'], formUrl=result['formUrl'])
        raise BTIPayException({"errorMessage": "Network error", "details": resp.text})

    def get_payment_status(self, order_id):
        params = {
            "userName": self._username,
            "password": self._password,
            "orderId": order_id
        }
        url = f"{self._base_url}payment/rest/getOrderStatusExtended.do"
        resp = requests.get(url, params=params)
        if resp:
            result = resp.json()
            if 'errorCode' in result:
                raise BTIPayException({"errorCode": result['errorCode'],
                                       "errorMessage": result['errorMessage'],
                                       "actionCode": result['actionCode'],
                                       "actionCodeDescription": result['actionCodeDescription']})
            return PaymentStatus.parse_obj(result)
        raise BTIPayException({"errorMessage": "Network error", "details": resp.text})
