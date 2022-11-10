# x = input("Enter your name: ")

# print("Your name is ", x)

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]
eyes = challenge[2][1]
goggles = challenge[2][0]
nothing = challenge[3]
print(f"My {eyes}! The {goggles} do {nothing}")

trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]
eyes = trial[2]["goggles"]
goggles = trial[2]["eyes"]
nothing = trial[3]
print(f"My {eyes}! The {goggles} do {nothing}")

nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]
eyes = nightmare[0]["user"]["name"]["first"]
goggles = nightmare[0]["kumquat"]
nothing = nightmare[0]["d"]
print(f"My {eyes}! The {goggles} do {nothing}!")
