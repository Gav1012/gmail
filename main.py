from simplegmail import Gmail
from simplegmail.query import construct_query

gmail = Gmail()

query_params = {
    "newer_than": (1, "week"),
    "older_than": (1, "day")
}

# messages = gmail.get_unread_inbox(query = construct_query(query_params))
messages = gmail.get_unread_inbox()

for message in messages:
    print("From: " + message.sender)
    print("Subject: " + message.subject)
    print("Data: " + message.date)
    print("Preview: " + message.snippet)