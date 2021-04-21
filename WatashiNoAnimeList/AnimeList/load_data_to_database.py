from .models import Anime

desc = """High schooler Hayase Nagatoro loves to spend her free time doing one thing, and that is to bully her Senpai! After Nagatoro and her friends stumble upon the aspiring artist's drawings, they find enjoyment in mercilessly bullying the timid Senpai. Nagatoro resolves to continue her cruel game and visits him daily so that she can force Senpai into doing whatever interests her at the time, especially if it makes him uncomfortable.

Slightly aroused by and somewhat fearful of Nagatoro, Senpai is constantly roped into her antics as his interests, hobbies, appearance, and even personality are used against him as she entertains herself at his expense. As time goes on, Senpai realizes that he doesn't dislike Nagatoro's presence, and the two of them develop an uneasy friendship as one patiently puts up with the antics of the other.

[Written by MAL Rewrite]"""

b = Anime(studio="Telecom Animation Film", name_eng='Ijiranaide, Nagatoro-san', description=desc, num_episodes=12, status="Currently Airing",
          premiered="Spring 2021", source="Manga", genres=[" Slice of Life", "Comedy", "Romance" ], duration=" 23 min. per ep.",
          score=7.20, image="https://cdn.myanimelist.net/images/anime/1900/110097.jpg")
b.save()
