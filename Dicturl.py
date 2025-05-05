urls = [
    "http://example.com",
    "https://secure-site.com",
    "ftp://files.example.org",
    "https://another-secure-site.com"
]

https_urls = [url for url in urls if url.startswith('https')]
print(https_urls)
