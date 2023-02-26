from datetime import datetime

from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, NumberAttribute, UTCDateTimeAttribute
)

class Wishes(Model):
    class Meta:
        table_name = 'wishes'
        region = 'ap-northeast-1'
        host = 'http://localhost:8000'
        write_capacity_units = 10
        read_capacity_units = 10
    account_id =  UnicodeAttribute(hash_key=True)
    wish_id = NumberAttribute(range_key=True)
    title = UnicodeAttribute(null=True)
    detail = UnicodeAttribute(null=True)
    status = UnicodeAttribute
    created_at = UTCDateTimeAttribute
    updated_at = UTCDateTimeAttribute
