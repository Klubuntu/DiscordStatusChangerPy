# Discord Status Changer Python Library

### Requirements
``python3 > 3.6``

``pip install requests``

### Example Usage (check status_example.py):
```python
from status_user import *
# changeStatus("your_auth_token", "STATUS_NAME" , "UNICODE_EMOJI", UNIX_TIME)
changeStatus("your_auth_token", "TEST1" , "💡", 1667428883)
```

[All Emoji Unicode List](https://unicode.org/emoji/charts/full-emoji-list.html)

[Unix Time Converter/Generator](https://www.unixtimestamp.com/index.php)
