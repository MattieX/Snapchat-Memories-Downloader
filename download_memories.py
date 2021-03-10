import os
import json
import requests
import threading
import time
import ffmpeg


def rename_files():
    dl_path = os.path.join(os.getcwd(), 'Download')
    os.chdir(dl_path)
    # Initialises a Count for Files that do not have date metadata
    count = 0
    for originalFilename in enumerate(os.listdir(os.getcwd())):
        # Accesses correct part of Tuple due to
        # Enumeration creating Tuple Datatype
        originalFilename = originalFilename[1]
        if "mp4" in originalFilename:
            try:
                vid_exif = ffmpeg.probe(originalFilename)
                # Uses FFMPEG Package Logic in order to get the correct time
                creation_time = vid_exif['streams'][0]['tags']['creation_time']
                destination_filename = "VID_" + str(creation_time).partition('T')[0]
                print(destination_filename)
                os.rename(originalFilename, destination_filename)
            except:
                count += 1
                print(f"No Creation Date was"
                      f"found for video {originalFilename}!")
                destination_filename = 'VID_Memory_' + str(count) + ".mp4"
                os.rename(originalFilename, destination_filename)
        # Snapchat Image Memories do not contain Date Metadata
        else:
            count += 1
            destination_filename = "IMG_Memory_" + str(count) + ".png"
            print(destination_filename)
            os.rename(originalFilename, destination_filename)


"""Downloads Memories to a 'Download' Folder"""
def download_file(download_link, media_type):
    # Makes the hashed filename more manageable
    filename = download_link.split('/')[-1][-10:]
    fileExtension = ".png" if (media_type == 'PHOTO') else ".mp4"
    fileStr = filename + fileExtension
    dl_path = os.path.join(os.getcwd(), 'Download', fileStr)
    with requests.get(download_link, stream=True) as memories_link:
        # Raises a HTTP Exception if one occured (Non-200 Response)
        memories_link.raise_for_status()
        with open(dl_path, 'wb') as f:
            for chunk in memories_link.iter_content(chunk_size=8192):
                f.write(chunk)


"""Post Request is made to obtain the Download Links"""
def makeRequest(url, media_type):
    response = requests.post(url)
    try:
        response.raise_for_status()
        download_link = response.text
        t = threading.Thread(target=download_file, args=(download_link, media_type))
        t.start()
    except requests.exceptions.HTTPError as error:
        print(f"There was an error accessing {url}\n"
              f"The HTTP Error Code returned was: {response.status_code}\n")


"""Manages Threaded Processes.
Gets download links --> Downloads Files --> Renames Files"""
def main():
    print("=====Getting Download Links=====")
    with open('memories_history.json') as json_file:
        data = json.load(json_file)
        for i in range((len(data["Saved Media"]))):
            url = (data["Saved Media"][i]["Download Link"])
            media_type = (data["Saved Media"][i]["Media Type"])
            print(url)
            t = threading.Thread(target=makeRequest, args=(url, media_type))
            t.start()
            time.sleep(0.2)

    print("=====Finished Downloading Files!=====")
    print("=====Renaming Files...=====")
    rename_files()


if __name__ == "__main__":
    main()
