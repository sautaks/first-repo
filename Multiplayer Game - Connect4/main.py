import sys
import subprocess

if len(sys.argv) < 2:
    print("Usage: python main.py [server|client]")
    sys.exit(1)

mode = sys.argv[1].lower()

if mode == "server":
    subprocess.run([sys.executable, "server.py"])
elif mode == "client":
    subprocess.run([sys.executable, "client.py"])
else:
    print("Unknown mode. Use 'server' or 'client'.")
