with open("server_logs.txt", "r") as infile, open("alerts.txt", "w") as outfile:
    for line in infile:
        if line.strip().upper().startswith("CRITICAL"):
            outfile.write(line)