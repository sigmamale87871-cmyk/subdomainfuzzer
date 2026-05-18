import requests
import sys
subdomains_list = open("subdomains.txt").read()
subdomains = subdomains_list.splitlines()

for domains in subdomains:
    sub_domains = f"http://{domains}.{sys.argv[1]}"

    try:
        requests.get(sub_domains)
    except requests.ConnectionError:
        print(f"Dead: {sub_domains}")
    else:
        print(sub_domains)
