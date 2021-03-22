# Snapchat Memories Downloader
***
## What does this script do?
The purpose of this Python Script is to download your snapchat memories provided by a Data Request and appropriately rename them, utilising date metadata if it's detected.

## Why?
By default, Snapchat provide you with a JSON File of your memories and not the files themselves, these URL's require a post request in order to actually obtain the download link.
If you were to do this manually, this would take a significant amount of time, prompting me to create this script.

## How to run it?
You need ```Python``` and ```Pip``` installed on your system.

- Git Clone this repository
- Make a snapchat data request by following the guide here: https://support.snapchat.com/en-GB/a/download-my-data
- Extract the ```mydata_<date>.zip``` and place the ```memories_history.json``` file in the Git Repo folder
- Open a Terminal that has Python in the PATH and cd into the Git Repo
- Run ```pip install ffmpeg``` - https://pypi.org/project/ffmpeg/
- Before continuing, verify the following items are in your Current Working Directory:
  - `download_memories.py` - File
  - `Download` - Folder (Empty!)
  - `memories_history.json`
- Finally, run ```python download_memories.py``` - File (Found in a Snapchat Data Request)
- Your Memories will be downloaded in the ```Download``` folder in your current working directory.

#### Please note, this script assumes that you have an empty ```Download``` folder as per the Repo before running

## Any issues?
Please feel free to raise any issues or enhancements you think would be beneifical for this script in the issues tab
