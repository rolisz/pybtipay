from datetime import datetime

from pydantic import BaseModel


class PaymentRegistration(BaseModel):
    orderId: str
    formUrl: str


class PaymentStatus(BaseModel):
    errorCode: str
    errorMessage: str
    orderNumber: str
    orderStatus: int
    actionCode: int
    actionCodeDescription: str
    amount: int
    currency: str
    date: datetime
    orderDescription: str
    ip: str
    merchantOrderParams: list
    attributes: list
    cardAuthInfo: dict
    authDateTime: datetime
    terminalId: str
    authRefNum: str
    paymentAmountInfo: dict
    bankInfo: dict
    orderBundle: dict
