# Airalo-API
*Automated API test code assignment for Airalo job application*

## Set-up
- clone the repo: `git clone <repo url>`
- cd into the repo
- Make sure Pytest is installed, if not `pip install -r requirements.txt`
- run `python -m pytest test_api.py -v -s`

## Rationale / open questions / thoughts
I could not find an easy way to link an id from the submit order response to tie to the get esim list request therefore I attempted to use the filter on "created at" however this has a flaw:
filtering by created at has no timestamp so if the test was run multiple times a day we would need to find a better way to look for the last submitted order.
What we could do is looping over iccid and do the esim list request 6 times but that looks like a lot of overhead if the quantity ramps up.