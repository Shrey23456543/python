emails = [
    "john@example.com",
    "alice@company.org",
    "bob@service.net"
]
domains = [email.split('@')[1] for email in emails]

print(domains)
