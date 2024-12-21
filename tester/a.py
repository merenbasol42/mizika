from mizika import Mizika
from utils import *
import time

mizika = Mizika(
    add_path(
        get_curr_dir(__file__),
        "pls"
    )
)
try: mizika.create_pl("first")
except: pass

mizika.set_edit_pl(0)

try: mizika.add_song("/home/ustad/Projects/Python Export/mizika/tester/musics/‘the devil’s trill’ but like the best part.mp3")
except: pass
mizika.remove_song(0)

mizika.add_song("/home/ustad/Projects/Python Export/mizika/tester/musics/‘the devil’s trill’ but like the best part.mp3")

mizika.set_play_pl(0)
print(mizika.play_pl.path_list)
mizika.get_song(0)
mizika.play()
while True:
    time.sleep(0.5)
