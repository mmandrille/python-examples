from ftplib import FTP


# Usefull functions
def get_content(ftp_client):
    folders = []
    ftp_client.dir(folders.append)
    folders = [f.split()[-1] for f in folders]
    return folders


# Code
if __name__ == "__main__":
    with FTP() as ftp_client:
        print("Connecting to FPT Server...")
        ftp_client.connect(host='localhost', port=21, timeout=None)
        ftp_client.login(user='username', passwd='mypass')

        print(f"Our actual path is: {ftp_client.pwd()}")

        # Creating File
        new_folder = "TestFolder"
        if new_folder not in get_content(ftp_client):
            ftp_client.mkd(new_folder)  # Create a Folder
            print(f"Creating {new_folder} folder")
        else:
            print(f"{new_folder} folder already exists")

        # move into the new folder:
        print(f"Moving to Folder: {new_folder}")
        ftp_client.cwd(f"{ftp_client.pwd()}{new_folder}")
        print(f"Our actual path is: {ftp_client.pwd()}")

        # copy a file from our computer to ftp folder:
        filename = 'README.md'
        if filename not in get_content(ftp_client):
            print(f"Creating {filename} file in {ftp_client.pwd()}")
            with open(filename, 'rb') as file:
                ftp_client.storbinary(f"STOR {filename}", file)
        else:
            print(f"{filename} file already exists in {ftp_client.pwd()}")

        # Show file on fpt folder:
        print(f"Our Folder contains: {get_content(ftp_client)}")
