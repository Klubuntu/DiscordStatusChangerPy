import requests
import datetime

def changeStatus(token, statusName, statusEmoji, statusUNIXTimeExpiredDate):
    # Convert Unix time to RFC 3339
    dt = datetime.datetime.fromtimestamp(statusUNIXTimeExpiredDate).astimezone()
    RFCtime = dt.isoformat()

    postURL = "https://discord.com/api/v9/users/@me/settings"

    myobj = {

        "custom_status": {

            "text": statusName,

            "expires_at": RFCtime,

            "emoji_name": statusEmoji

        }

    }

    requests.patch(postURL, json=myobj, headers={"authorization": token})
    print("[" + RFCtime  + "]" +  " Status Changed")

