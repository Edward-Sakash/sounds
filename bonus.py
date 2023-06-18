
########################################


##########################################################

"""import os
import webbrowser

def play_video(file_path):
    webbrowser.open(file_path)

user_input = input("If you would like to play 'audio_files', press 'a'. Otherwise, press 'v' if you would like to play 'video_files': ")

if user_input == 'a':
    # Code to play audio_files
    print("Playing audio_files...")
elif user_input == 'v':
    # Code to play video_files
    print("Playing video_files...")
else:
    folder_choice = input("Choose a folder (audio_files/video_files): ")
    file_choice = input("Choose a file (dog/cat): ")

    if folder_choice == "audio_files":
        # Code to handle audio files
        print(f"Chose folder: {folder_choice}")
        print(f"You chose: {file_choice}")

    elif folder_choice == "video_files":
        # Code to handle video files
        print(f"Chose folder: {folder_choice}")
        print(f"You chose: {file_choice}")

        if file_choice == "dog":
            play_video(os.path.join("video_files", "dog_video.mp4"))
        elif file_choice == "cat":
            play_video(os.path.join("video_files", "cat_video.mp4"))

    else:
        print("Invalid folder choice.")"""

#######################################################

"""import os
import webbrowser

def play_video(file_path):
    webbrowser.open(file_path)

folder_choice = input("Choose a folder (audio_files/video_files): ")
if folder_choice == "audio_files":
    folder_choice = 'a'
elif folder_choice == "video_files":
    folder_choice = 'v'

if folder_choice == 'a':
    # Code to handle audio files
    file_choice = input("Choose a file (dog/cat): ")
    print(f"Chose folder: audio_files")
    print(f"You chose: {file_choice}")
elif folder_choice == 'v':
    # Code to handle video files
    file_choice = input("Choose a file (dog/cat): ")
    print(f"Chose folder: video_files")
    print(f"You chose: {file_choice}")
    if file_choice == "dog":
        play_video(os.path.join("video_files", "dog_video.mp4"))
    elif file_choice == "cat":
        play_video(os.path.join("video_files", "cat_video.mp4"))
else:
    print("Invalid folder choice.")
"""

############################################################

"""import os
import webbrowser

def play_video(file_path):
    webbrowser.open(file_path)

folder_choice = input("Choose a folder ('audio_files'/'video_files'): ")

if folder_choice == 'audio_files':
    folder_choice = 'a'
elif folder_choice == 'video_files':
    folder_choice = 'v'

if folder_choice == 'a':
    # Code to handle audio files
    file_choice = input("Choose a file (dog/cat): ")
    print(f"Chose folder: audio_files")
    print(f"You chose: {file_choice}")

elif folder_choice == 'v':
    # Code to handle video files
    file_choice = input("Choose a file (dog/cat): ")
    print(f"Chose folder: video_files")
    print(f"You chose: {file_choice}")

    if file_choice == "dog":
        play_video(os.path.join("video_files", "dog_video.mp4"))
    elif file_choice == "cat":
        play_video(os.path.join("video_files", "cat_video.mp4"))

else:
    print("Invalid folder choice.")"""
#################################################################

"""import os
import subprocess

def play_audio(file_path):
    # Code to play audio files
    subprocess.call(["afplay", file_path])

def play_video(file_path):
    # Code to play video files
    # (You can use your preferred method to play video files)
    pass

folder_choice = input("Choose a folder ('audio_files'/'video_files'): ")

if folder_choice == 'audio_files':
    folder_choice = 'a'
elif folder_choice == 'video_files':
    folder_choice = 'v'

if folder_choice == 'a':
    # Code to handle audio files
    file_choice = input("Choose a file (dog/cat): ")
    print(f"Chose folder: audio_files")
    print(f"You chose: {file_choice}")

    if file_choice == "dog":
        play_audio(os.path.join("audio_files", "dog_audio.mp3"))
    elif file_choice == "cat":
        play_audio(os.path.join("audio_files", "cat_audio.mp3"))

elif folder_choice == 'v':
    # Code to handle video files
    file_choice = input("Choose a file (dog/cat): ")
    print(f"Chose folder: video_files")
    print(f"You chose: {file_choice}")

    if file_choice == "dog":
        play_video(os.path.join("video_files", "dog_video.mp4"))
    elif file_choice == "cat":
        play_video(os.path.join("video_files", "cat_video.mp4"))

else:
    print("Invalid folder choice.")
"""
###############################################

"""import os
from playsound import playsound
import webbrowser

def play_video(file_path):
    webbrowser.open(file_path)

def play_audio(file_path):
    playsound(file_path)

# Take user input
choice = input("If you would like to play 'audio', enter 'a'. Otherwise, enter 'v' to play 'video': ")

if choice.lower() == 'a':
    # Code to handle audio files
    folder_choice = input("Choose a folder ('audio_files'): ")

    if folder_choice.lower() == 'audio_files':
        file_choice = input("Choose a file ('dog'/'cat'): ")

        if file_choice.lower() == 'dog':
            play_audio(os.path.join("audio_files", "dog_sound.mp3"))
        elif file_choice.lower() == 'cat':
            play_audio(os.path.join("audio_files", "cat_sound.mp3"))
        else:
            print("Invalid file choice. Please enter 'dog' or 'cat'.")
    else:
        print("Invalid folder choice. Please enter 'audio_files'.")
elif choice.lower() == 'v':
    # Code to handle video files
    folder_choice = input("Choose a folder ('video_files'): ")

    if folder_choice.lower() == 'video_files':
        file_choice = input("Choose a file ('dog'/'cat'): ")

        if file_choice.lower() == 'dog':
            play_video(os.path.join("video_files", "dog_video.mp4"))
        elif file_choice.lower() == 'cat':
            play_video(os.path.join("video_files", "cat_video.mp4"))
        else:
            print("Invalid file choice. Please enter 'dog' or 'cat'.")
    else:
        print("Invalid folder choice. Please enter 'video_files'.")
else:
    print("Invalid input. Please enter 'a' for audio or 'v' for video.")
"""
########################################################################
import os
from playsound import playsound
import webbrowser

def play_video(file_path):
    webbrowser.open(file_path)

def play_audio(file_path):
    playsound(file_path)

# Take user input
choice = input("If you would like to play 'audio', enter 'a'. Otherwise, enter 'v' to play 'video': ")

if choice.lower() == 'a':
    # Code to handle audio files
    folder_choice = input("Choose a folder ('audio_files'): ")

    if folder_choice.lower() == 'audio_files':
        file_choice = input("Choose a file ('dog'/'cat'): ")

        if file_choice.lower() == 'dog':
            play_audio(os.path.join("audio_files", "dog_sound.mp3"))
        elif file_choice.lower() == 'cat':
            play_audio(os.path.join("audio_files", "cat_sound.mp3"))
        else:
            print("Invalid file choice. Please enter 'dog' or 'cat'.")
    else:
        print("Invalid folder choice. Please enter 'audio_files'.")
elif choice.lower() == 'v':
    # Code to handle video files
    folder_choice = input("Choose a folder ('video_files'): ")

    if folder_choice.lower() == 'video_files':
        file_choice = input("Choose a file ('dog'/'cat'/'panda'/'pandas'): ")

        if file_choice.lower() == 'dog':
            play_video(os.path.join("video_files", "dog_video.mp4"))
        elif file_choice.lower() == 'cat':
            play_video(os.path.join("video_files", "cat_video.mp4"))
        elif file_choice.lower() == 'panda':
            play_video(os.path.join("video_files", "panda_video.mp4"))
        elif file_choice.lower() == 'pandas':
            play_video(os.path.join("video_files", "panda_video1.mp4"))    
        else:
            print("Invalid file choice. Please enter 'dog', 'cat', 'panda', or 'pandas'.")
    else:
        print("Invalid folder choice. Please enter 'video_files'.")
else:
    print("Invalid input. Please enter 'a' for audio or 'v' for video.")
