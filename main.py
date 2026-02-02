import requests

print("Python funciona 😎")

r = requests.get("https://api.github.com")
print("Status de GitHub API:", r.status_code)
