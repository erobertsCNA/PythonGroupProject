def load_videos(filename):
    """
    Loads video data from a file.

    Input:
    - filename (str): File name to load videos from.

    Output:
    - list: List of video dictionaries.
    """
    videos = []
    try:
        with open(filename, "r") as file:
            for line in file:
                title, director, release_year, genre, duration = line.strip().split('|')
                videos.append({
                    "title": title,
                    "director": director,
                    "release_year": int(release_year),
                    "genre": genre,
                    "duration": int(duration)
                })
    except FileNotFoundError:
        pass
    return videos

def save_videos(filename, videos):
    """
    Saves video data to a file.

    Input:
    - filename (str): File name to save videos to.
    - videos (list): List of video dictionaries.

    Output:
    - None
    """
    with open(filename, "w") as file:
        for video in videos:
            file.write(f"{video['title']}|{video['director']}|{video['release_year']}|{video['genre']}|{video['duration']}\n")

def add_video(videos):
    """
    Adds a new video to the list.

    Input:
    - videos (list): List of video dictionaries.

    Output:
    - None
    """
    title = input("Enter video title: ")
    director = input("Enter director: ")
    release_year = int(input("Enter release year: "))
    genre = input("Enter genre: ")
    duration = int(input("Enter duration (in minutes): "))
    videos.append({
        "title": title,
        "director": director,
        "release_year": release_year,
        "genre": genre,
        "duration": duration
    })
    print("Video added successfully!")

def edit_video(videos):
    """
    Edits an existing video.

    Input:
    - videos (list): List of video dictionaries.

    Output:
    - None
    """
    display_all_videos(videos)
    index = int(input("Enter the video index to edit: ")) - 1
    if 0 <= index < len(videos):
        video = videos[index]
        print(f"Editing {video['title']}...")
        video['title'] = input(f"Enter new title (or press Enter to keep '{video['title']}'): ") or video['title']
        video['director'] = input(f"Enter new director (or press Enter to keep '{video['director']}'): ") or video['director']
        video['release_year'] = int(input(f"Enter new release year (or press Enter to keep '{video['release_year']}'): ") or video['release_year'])
        video['genre'] = input(f"Enter new genre (or press Enter to keep '{video['genre']}'): ") or video['genre']
        video['duration'] = int(input(f"Enter new duration (or press Enter to keep '{video['duration']}'): ") or video['duration'])
        print("Video updated successfully!")
    else:
        print("Invalid video index!")

def delete_video(videos):
    """
    Deletes a video from the list.

    Input:
    - videos (list): List of video dictionaries.

    Output:
    - None
    """
    display_all_videos(videos)
    index = int(input("Enter the video index to delete: ")) - 1
    if 0 <= index < len(videos):
        deleted_video = videos.pop(index)
        print(f"Deleted video: {deleted_video['title']}")
    else:
        print("Invalid video index!")

def display_all_videos(videos):
    """
    Displays all video titles.

    Input:
    - videos (list): List of video dictionaries.

    Output:
    - None
    """
    if not videos:
        print("No videos in the library.")
    else:
        for i, video in enumerate(videos, 1):
            print(f"{i}. {video['title']}")

def display_video_details(videos):
    """
    Displays details of a selected video.

    Input:
    - videos (list): List of video dictionaries.

    Output:
    - None
    """
    display_all_videos(videos)
    index = int(input("Enter the video index to view details: ")) - 1
    if 0 <= index < len(videos):
        video = videos[index]
        print(f"Title: {video['title']}")
        print(f"Director: {video['director']}")
        print(f"Release Year: {video['release_year']}")
        print(f"Genre: {video['genre']}")
        print(f"Duration: {video['duration'] // 60} hours {video['duration'] % 60} minutes")
    else:
        print("Invalid video index!")

def list_videos_by_criteria(videos):
    """
    Lists videos by specific criteria.

    Input:
    - videos (list): List of video dictionaries.

    Output:
    - None
    """
    criteria_map = {
        1: "director",
        2: "release_year",
        3: "genre",
        4: "duration"
    }
    print("The following criteria is available:")
    for key, value in criteria_map.items():
        print(f"{key}. {value.replace('_', ' ').title()}")

    criteria_choice = int(input("Enter criteria: "))
    if criteria_choice in criteria_map:
        criteria = criteria_map[criteria_choice]
        unique_values = sorted(set(video[criteria] for video in videos))

        print(f"You selected {criteria.replace('_', ' ').title()}. The list of available {criteria.replace('_', ' ')}s is below:")
        for i, value in enumerate(unique_values, 1):
            print(f"{i}. {value}")

        selection = input("Enter selection: ")
        filtered_videos = [video for video in videos if str(video[criteria]) == selection]
        for video in filtered_videos:
            print(f"{video['title']} ({video['release_year']}), Directed by {video['director']}, Genre: {video['genre']}, Duration: {video['duration']} minutes")
    else:
        print("Invalid criteria selection!")

def menu():
    """
    Displays the main menu and processes user input.

    Input:
    - None

    Output:
    - None
    """
    filename = "video_library.txt"
    videos = load_videos(filename)

    while True:
        print("\nChoose from the options below:")
        print("1. Add new video.")
        print("2. Edit video.")
        print("3. Delete video.")
        print("4. Display all videos by name.")
        print("5. Display detailed video information.")
        print("6. List videos by criteria.")
        print("7. Exit.")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_video(videos)
        elif choice == "2":
            edit_video(videos)
        elif choice == "3":
            delete_video(videos)
        elif choice == "4":
            display_all_videos(videos)
        elif choice == "5":
            display_video_details(videos)
        elif choice == "6":
            list_videos_by_criteria(videos)
        elif choice == "7":
            save_videos(filename, videos)
            print("Thank you for using the Video Library Management System!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    menu()
