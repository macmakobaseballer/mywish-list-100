from app.core import settings

from datetime import datetime
from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, NumberAttribute, UTCDateTimeAttribute
)
from zoneinfo import ZoneInfo

def get_current_time():
        return datetime.now()

class WishModel(Model):
    class Meta:
        table_name = 'wish_list'
        region = settings.DYN_REGION_NAME
        host = settings.DYN_ENDPOINT_URL
        write_capacity_units = 10
        read_capacity_units = 10
    account_id =  UnicodeAttribute(hash_key=True)
    wish_id = NumberAttribute(range_key=True)
    title = UnicodeAttribute(null=True)
    description = UnicodeAttribute(null=True)
    status = UnicodeAttribute
    created_at = UTCDateTimeAttribute(default_for_new=get_current_time)
    updated_at = UTCDateTimeAttribute(default_for_new=get_current_time)

if not WishModel.exists():
    WishModel.create_table(read_capacity_units=10, write_capacity_units=10, wait=True)
