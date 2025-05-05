import requests

BASE_URL = "https://sandbox-partners-api.airalo.com"

CLIENT_ID = "7e29e2facf83359855f746fc490443e6"
CLIENT_SECRET = "e5NNajm6jNAzrWsKoAdr41WfDiMeS1l6IcGdhmbb"

def get_bearer_token():
	url = f"{BASE_URL}/v2/token"
	payload = {'client_id': CLIENT_ID,
	'client_secret': CLIENT_SECRET,
	'grant_type': 'client_credentials'
	}
	headers = {
	'Accept': 'application/json'
	}
	response = requests.post(url, headers=headers, data=payload)
	response.raise_for_status()
	return response.json()['data']['access_token']


def submit_order(token, quantity, package_id, order_type=None, description=None, brand_settings_name=None):
	url=f"{BASE_URL}/v2/orders"
	headers = {
	#"Accept": 'application/json'
	"Authorization": f"Bearer {token}"}
	payload ={
		'quantity': quantity,
		'package_id': package_id
	}
	if order_type is not None:
		payload['order_type']= order_type
	if description is not None:
		payload['description']= description
	if brand_settings_name is not None:
		payload['brand_settings_name']= brand_settings_name
	response = requests.post(url, json=payload, headers=headers)
	response.raise_for_status()
	return response

def get_esims(token, with_order=False, created_at=None):
	url=f"{BASE_URL}/v2/sims"
	params = {}
	if with_order:
		params["include"] = "order"
	if created_at:
		params["filter[created_at]"] = f"{created_at} - {created_at}"
	headers = {"Authorization": f"Bearer {token}"}
	response = requests.get(url, headers=headers, params=params)
	response.raise_for_status()
	return response


