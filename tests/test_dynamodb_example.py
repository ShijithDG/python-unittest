import boto3
from moto import mock_dynamodb2
from src.boto3_example import DynamodBExample
import pytest


@mock_dynamodb2
def test_create_dynamo_table():
    '''
        Implement the test logic here for testing create_dynamo_table method
    '''
    
    dynamo_example = DynamodBExample()
    dynamo_example.create_movies_table()

    # Check if the table is created
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Movies')

    # Verify the table exists
    assert table.table_status == 'ACTIVE'



@mock_dynamodb2
def test_add_dynamo_record_table():
    '''
        Implement the test logic here for testing add_dynamo_record_table method
    '''
    dynamo_example = DynamodBExample()
    dynamo_example.create_movies_table()
    
    item = {
        'year': 2021,
        'title': 'Spider-Man: No Way Home',
        'genre': 'Action'
    }
       
    # Add the item to the table
    dynamo_example.add_dynamo_record('Movies', item)
    
    # Verify the item was added
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Movies')
    response = table.get_item(
        Key={
            'year': 2021,
            'title': 'Spider-Man: No Way Home'
        }
    )
    
    # Assert that the item exists and has the expected values
    assert 'Item' in response
    assert response['Item']['year'] == 2021
    assert response['Item']['title'] == 'Spider-Man: No Way Home'
    
    assert False

@mock_dynamodb2
def test_add_dynamo_record_table_failure():
    '''
        Implement the test logic here test_add_dynamo_record_table method for failures
    '''
    
    dynamo_example = DynamodBExample()

    # Define the item to add
    item = {
        'year': 2023,
        'title': 'Spider-Man: Across the Spider-Verse',
    }

    # Attempt to add the item to a non-existent table
    with pytest.raises(Exception):
        dynamo_example.add_dynamo_record('NonExistentTable', item)
    assert False
    
    # Attempt to add the item to a non-existent table
    # try:
    #     dynamo_example.add_dynamo_record('NonExistentTable', item)
    #     # If no exception was raised, we fail the test
    #     assert False, "Expected ClientError was not raised"
    # except ClientError as e:
    #     # Assert the exception code
    #     assert e.response['Error']['Code'] == 'ResourceNotFoundException'
