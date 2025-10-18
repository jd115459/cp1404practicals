COLOUR_TO_HEX = {"absolute zero": "#0048Ba", "acid green": "#b0bf1a", "aliceblue": "#f0f8ff",
                 "alizarin crimson": "#e32636", "amaranth": "#e52b50", "amber": "	#ffbf00",
                 "amethyst": "#9966cc", "antiquewhite": "#faebd7", "apricot": "#fbceb1", "aqua": "#00ffff"}

for code, name in COLOUR_TO_HEX.items():
    print(f"{code} is {name}")

colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    try:
        print(f"{colour_name} is {COLOUR_TO_HEX[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter a colour name: ").lower()