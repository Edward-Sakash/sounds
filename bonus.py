
########################################

########################################################
import os
import webbrowser

def play_video(file_path):
    webbrowser.open(file_path)

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
    print("Invalid folder choice.")
