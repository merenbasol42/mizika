'''
MManager (Mizika Manager); "mizika" paketi için oynatma listesi işlemleri
işlevlerini yerine getiren sınıftır.
'''

import random
from typing import Optional, Union
from ..core.core import Song
from .playlist import Playlist
from .pl_list import PLList
from .enums import *

class MManager: #Mizika Manager
    def __init__(self, pls_dir_path: str):
        self.play_mode: str = PLAY_MODE.DEFAULT
        self.pl_index: Optional[int] = None
        self.curr_song: Optional[Song] = None
        self.play_pl: Optional[Playlist] = None
        self.edit_pl: Optional[Playlist] = None
        self.pl_list: PLList = PLList(pls_dir_path)

    #
    # Playing Methods   
    # 
    
    def set_play_pl(self, name_or_index: str):
        '''Set the playing playlist'''
        self.play_pl = self.pl_list.get(name_or_index)
        self.play_pl.load()

    def set_play_mode(self, new_mode: str):
        '''Set the play mode'''
        if new_mode in PLAY_MODE.ARR:
            self.play_mode = new_mode
        else:
            raise ValueError(f"Invalid play mode: {new_mode}")

    def load_song(self, index: int) -> Song:
        '''Load a song at a specific index in the current playlist'''
        if self.play_pl is None:
            raise ValueError("No playlist is currently loaded")
        
        if 0 <= index < len(self.play_pl.path_list):
            self.pl_index = index
            self.curr_song = self.play_pl.get_a_song(index)
            return self.curr_song
        
        raise IndexError("Song index out of range")

    def forward(self) -> Song:
        '''Return the next song based on play mode'''
        if self.play_pl is None or not self.play_pl.path_list:
            raise ValueError("No playlist or songs available")
        
        if self.play_mode == PLAY_MODE.ONE:
            return self.curr_song if self.curr_song else self.load_song(0)
        
        if self.play_mode == PLAY_MODE.MIX:
            self.pl_index = random.randint(0, len(self.play_pl.path_list) - 1)
        else:
            self.pl_index = (self.pl_index + 1) % len(self.play_pl.path_list)
        
        return self.load_song(self.pl_index)

    def backward(self) -> Song:
        '''Return the previous song based on play mode'''
        if self.play_pl is None or not self.play_pl.path_list:
            raise ValueError("No playlist or songs available")
        
        if self.play_mode == PLAY_MODE.ONE:
            return self.curr_song if self.curr_song else self.load_song(0)
        
        if self.play_mode == PLAY_MODE.MIX:
            import random
            self.pl_index = random.randint(0, len(self.play_pl.path_list) - 1)
        else:
            self.pl_index = (self.pl_index - 1 + len(self.play_pl.path_list)) % len(self.play_pl.path_list)
        
        return self.load_song(self.pl_index)

    #
    # Editing Methods
    #

    def set_edit_pl(self, name_or_index: str | int):
        '''Set the playlist for editing'''
        self.edit_pl = self.pl_list.get(name_or_index)
        self.edit_pl.load()
        
    def add_song(self, *paths: str):
        '''Add songs to the editing playlist'''
        if self.edit_pl is None: return
        
        self.edit_pl.add_song(*paths)

    def remove_song(self, *index: int):
        '''Remove songs from the editing playlist'''
        if self.edit_pl is None: return
        
        self.edit_pl.remove_song(*index)

    def insert_song(self, up_down: bool, target: int, *index: int):
        '''Insert or move songs in the editing playlist'''
        if self.edit_pl is None: return
        
        self.edit_pl.insert_song(up_down, target, *index)

    #
    # CRUD PL
    #

    def create_pl(self, name: str):
        '''Create a new playlist'''
        self.pl_list.create(name)

    def update_pl(self, name_or_index: Union[str, int], new_name: str):
        '''Update a playlist name'''
        self.pl_list.update(name_or_index, new_name)

    def delete_pl(self, name_or_index: Union[str, int]):
        '''Delete a playlist'''
        self.pl_list.delete(name_or_index)
