import os
from playsound import playsound
import webbrowser
from sounds import Dog, Cat

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
