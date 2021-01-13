# Telstra Messaging

The SDK for the Telstra messaging API.

## Installing

```bash
pip install messaging
```

## Getting Started

Set the `TLS_CLIENT_KEY` and `TLS_CLIENT_SECRET` environment variables. These
are the `Client key` and `Client secret` you can find here:
<https://dev.telstra.com/user/me/apps>.

To send your first SMS:

```python
from tls.messaging import sms

sms.send(to="+61412345678", body="Hi")
```

```bash
TLS_CLIENT_KEY="XXXX" TLS_CLIENT_SECRET="YYYY" python app.py
```
