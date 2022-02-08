from datetime import datetime
from typing import Optional

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
    ip: Optional[str] = None
    merchantOrderParams: Optional[list] = None
    attributes: Optional[list] = None
    cardAuthInfo: Optional[dict] = None
    authDateTime: Optional[datetime] = None
    terminalId: Optional[str] = None
    authRefNum: Optional[str] = None
    paymentAmountInfo: Optional[dict] = None
    bankInfo: Optional[dict] = None
    orderBundle: Optional[dict] = None
