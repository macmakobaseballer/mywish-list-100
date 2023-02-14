import boto3
from app.core.config import settings

def create_table(dynamodb=None):
    table = dynamodb.create_table(
        TableName="bucket_list",
        KeySchema=[{"AttributeName": "account_id", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "account_id", "AttributeType": "S"}],
        ProvisionedThroughput={"ReadCapacityUnits": 10, "WriteCapacityUnits": 10},
    )

    return table


if __name__ == "__main__":
    dynamodb = boto3.resource(
        service_name="dynamodb",
        endpoint_url=settings.DYN_ENDPOINT_URL,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.DYN_REGION_NAME,
    )
    bucket_list_table = create_table(dynamodb)
    print(f"Table status: {bucket_list_table.table_status}")
