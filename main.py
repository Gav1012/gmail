from simplegmail import Gmail
from simplegmail.query import construct_query

gmail = Gmail()

query_params = {
    "newer_than": (5, "day"),
    # "older_than": (1, "hour"),
    "unread": True,
    "sender": [["jobs-noreply@linkedin.com"], ["jobs-listings@linkedin.com"]]
}

messages = gmail.get_messages(query = construct_query(query_params))

for message in messages:
    print("From: " + message.sender)
    print("Subject: " + message.subject)
    print("Data: " + message.date)
    print("Preview: " + message.snippet)