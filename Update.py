import requests
print("checking for updates")
print("if this fails you need the request package from pip")


response = requests.get("https://api.github.com/repos/20Speedy12/Some-what-Dos-python/releases/latest")
print(response.json()["name"])
print("is the most current version") 
print ("your version is 1.2!")
exit()