import pytest
from airalo_client import get_bearer_token, submit_order, get_esims

def test_api_flow():
	# Get the token
	token = get_bearer_token()
	assert token is not None and isinstance(token, str)

	# Submit the order
	order_response= submit_order(token, quantity = 6, package_id ="merhaba-7days-1gb")
	assert order_response.status_code == 200

	# Get the sim cards
	esims_response = get_esims(token)
	assert esims_response.status_code == 200

	first_item = esims_response["data"][0]
	simable = first_item["simable"]

	assert simable["quantity"] == 6
	assert simable["package"] == "merhaba-7days-1gb"
	assert simable["data"] == "1 GB"
	assert simable["price"] == "4.5"


