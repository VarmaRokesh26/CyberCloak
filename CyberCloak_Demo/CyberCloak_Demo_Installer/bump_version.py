import configparser

config = configparser.ConfigParser()
config.read("version.ini")

major, minor, patch = map(int, config["Version"]["AppVer"].split("."))
patch += 1
new_version = f"{major}.{minor}.{patch}"

config["Version"]["AppVer"] = new_version
with open("version.ini", "w") as configfile:
    config.write(configfile)

print(f"Version updated to: {new_version}")
