import json
from base64 import *

def create_vfs_structure():
    # Текстовый файл
    text_1 = "Hello, i was created on 21 of September of 2025"
    text_2 = "Hallo, ich war...  "
    config_text_1 = ("[DEFAULT]" +
                     "vfs_path = vfs_struct_file.txt"+
                     "script_path = vfs_start_script.txt")
    config_text_2 = ("[NOTDEFAULT]" +
                     "vfs_path = vfs_struct_file.odt"+
                     "script_path = vfs_start_script_w_bugs.odt")
    movie = "sorry, no movie for u"
    music = "sorry, no music for u"
    what = "what"
    do_not_read_me = "Have not i told you not to read it?"
    
    
    encoded_text_1 = b64encode(text_1.encode('utf-8')).decode('utf-8')
    encoded_text_2 = b64encode(text_2.encode('utf-8')).decode('utf-8')
    encoded_config_text_1 = b64encode(config_text_1.encode('utf-8')).decode('utf-8')
    encoded_config_text_2 = b64encode(config_text_2.encode('utf-8')).decode('utf-8')
    encoded_movie = b64encode(movie.encode('utf-8')).decode('utf-8')
    encoded_music = b64encode(music.encode('utf-8')).decode('utf-8')
    encoded_what = b64encode(what.encode('utf-8')).decode('utf-8')
    encoded_do_not_read_me = b64encode(do_not_read_me.encode('utf-8')).decode('utf-8')
    # we encode to bytes with utf-8 format then to base64 format, then back to ctring with utf-8
    
    vfs_structure = {
    "type": "directory",
    "name": "MAIN_CAT",
    "path": "/",
    "children": [
        
        {
        "type": "directory",
        "name": "SUB_CAT_1_office",
        "path": "/SUB_CAT_1_office",
        "children": [
            {
            "type": "file",
            "name": "file1.txt",
            "path": "/SUB_CAT_1_office/file1.txt",
            "content": encoded_text_1,
            "encoding": "base64",
            "size": len(text_1)
            },
            
            
        {
            "type": "file",
            "name": "file2.odt",
            "path": "/SUB_CAT_1_office/file2.odt",
            "content": encoded_text_2,
            "encoding": "base64",
            "size": len(text_2),
            }
        ]
    },
    {
      "type": "directory",
      "name": "SUB_CAT_2_config",
      "path": "/SUB_CAT_2_config",
      "children": [
        {
          "type": "file",
          "name": "MANUAL.ini",
          "path": "/SUB_CAT_2_config/MANUAL.ini",
          "content": encoded_config_text_1,
          "encoding": "base64",
          "size": len(config_text_1)
        },
        {
          "type": "file",
          "name": "HELP.ini",
          "path": "/SUB_CAT_2_config/HELP.ini",
          "content": encoded_config_text_2,
          "encoding": "base64",
          "size": len(config_text_2)
        }
      ]
    },
    {
      "type": "directory",
      "name": "SUB_CAT_3_fun",
      "path": "/SUB_CAT_3_fun",
      "children": [
        {
          "type": "file",
          "name": "movie.mp4",
          "path": "/SUB_CAT_3_fun/movie.mp4",
          "content": encoded_movie,
          "encoding": "base64",
          "size": len(movie),
          "metadata": {
              "duration": "00:05:30",
              "resolution": "1920x1080"
          }
        },
        {
          "type": "file",
          "name": "music.mp3",
          "path": "/SUB_CAT_3_fun/music.mp3",
          "content": encoded_music,
          "encoding": "base64",
          "size": len(music),
          "metadata": {
            "duration": "00:03:45",
            "artist": "Unknown Artist"
          }
        }
      ]
    },
    {
      "type": "directory",
      "name": "SUB_CAT_5",
      "path": "/SUB_CAT_5",
      "children": [
        {
          "type": "directory",
          "name": "SUB_SUB_CAT_1",
          "path": "/SUB_CAT_5/SUB_SUB_CAT_1",
          "children": [
            {
              "type": "file",
              "name": "what.txt",
              "path": "/SUB_CAT_5/SUB_SUB_CAT_1/what.txt",
              "content": encoded_what,
              "encoding": "base64",
              "size": len(what)
            }
          ]
        },
        {
          "type": "directory",
          "name": "SUB_SUB_CAT_2",
          "path": "/SUB_CAT_5/SUB_SUB_CAT_2",
          "children": [
            {
              "type": "file",
              "name": "DOnotREADME.md",
              "path": "/SUB_CAT_5/SUB_SUB_CAT_2/DOnotREADME.md",
              "content": encoded_do_not_read_me,
              "encoding": "base64",
              "size": len(do_not_read_me)
            }
          ]
        }
      ]
    }
  ]
}
    
    with open('vfs.json', 'w') as f:
        json.dump(vfs_structure, f, indent=2)
        
    # Открывается файл 'vfs.json' для записи, и структура VFS сохраняется в него с отступами в 2 пробела

create_vfs_structure()