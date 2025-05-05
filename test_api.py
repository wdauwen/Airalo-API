import pytest
from airalo_client import get_bearer_token, submit_order, get_esims

def test_api_flow():
	# Get the token
	token = get_bearer_token()
	assert token is not None and isinstance(token, str)

	# Submit the order
	order_response= submit_order(token, quantity = 6, package_id ="merhaba-7days-1gb")
	assert order_response.status_code == 200

	created_at = order_response.json()["data"]["created_at"]

	# Get the sim cards
	esims_response = get_esims(token, with_order=True, created_at=created_at)
	assert esims_response.status_code == 200

	orders = esims_response.json()["data"]

	for order in orders:
		if order["created_at"] != created_at:
			continue

		first_item = orders[0]
		simable = first_item["simable"]

		assert simable["quantity"] == 6
		assert simable["package"] == "Merhaba-1 GB - 7 Days"
		assert simable["data"] == "1 GB"
		assert simable["price"] == "4.5"


