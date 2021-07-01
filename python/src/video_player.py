import random


"""A video player class."""


from .video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.play_status = False
        self.paused = False
        self.current_video= "None"


    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        print("Here's a list of all the available videos")

        all_videos = self._video_library.get_all_videos()
        sortedlist=[]

        for i in all_videos:
             sortedlist.append((f"{i.title}, ({i.video_id}), {i.tags}"))
        
        def sort_key(name):
            return name[0]


        sortedlist.sort(key=sort_key)

        print(*sortedlist, sep = "\n")

    def play_video(self, video_id):

        videos = self._video_library.get_all_videos()
        for video in videos:
            if video._video_id == video_id:
                if self.play_status:
                    print("Stopping video", self.current_video[0])
                print("Playing video: ", video._title)
                self.current_video = [video._title, video._video_id, video._tags]
                self.play_status = True
                self.paused = False
                return
        print("Cannot play video: Video does not exist")     


    def stop_video(self):
        """Stops the current video."""
        videos = self._video_library.get_all_videos()
        if self.play_status==True:
            print("Stopping Video:", self.current_video[0])
            self.play_status=False
        else:
            print("Cannot Stop Video: No video is currently Playing")


        

    def play_random_video(self):
        """Plays a random video from the video library."""
        videos = self._video_library.get_all_videos()

        video=random.choice(videos)

        if self.play_status:
            print("Stopping video", self.current_video[0])
        print("Playing video: ", video._title)
        self.current_video = [video._title, video._video_id, video._tags]
        self.play_status = True
        self.paused = False
        return


        print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""

        if self.paused:
            print("Video Already Paused", self.current_video[0])
        else:
            print("Pausing video: ", self.current_video[0])
            self.play_status = True
            self.paused = True
            return

    def continue_video(self):
        """Pauses the current video."""

        if self.paused:
            print("Continuing Video", self.current_video[0])
            self.paused = False
        else:
            print("Cannot continue Video, video is not paused")
            return

    def show_playing(self):
        """Displays video currently playing."""

        print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
