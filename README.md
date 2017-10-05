# Python client for STUDIS API
Ultra simple client for Studis API

## Basic usage

First enter the authentication token
```python
import studis_api.studis_api as studis
studis.KEY = "STUDIS_TOKEN"
studis.URL = "https://studis.site.com"
```
To get the the data of a staff member
```python
studis.call('/osebeapi/oseba/XXXX')
```
