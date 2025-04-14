version_file = "version.txt"

# Read current version
with open(version_file, "r") as f:
    version = f.read().strip()

major, minor, patch = map(int, version.split("."))
patch += 1  # You can change this logic if you want minor/major bumps
new_version = f"{major}.{minor}.{patch}"

# Write back new version
with open(version_file, "w") as f:
    f.write(new_version)

print(f"Version updated to: {new_version}")