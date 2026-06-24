import os

# for i in range(1, 13):
files = os.listdir("ClutteredFolder")
i = 1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"ClutteredFolder/{file}", f"ClutteredFolder/{i}.png")
        i = i + 1