# Youtube language converter (audio)
It translates the youtube video you want to the language you want.

Don't want to watch videos with subtitles on youtube? You can change the language of the video using the python code I wrote.

1) To use the code, you must first install the library in the "requirements.txt" file.

2) Then you can run the code

3) The code will give you 5 files as output. > Downloaded video, audio file(english language), text file(turkish and english language), audio file(turkish language(THE FILE YOU NEED))

4) You can translate the downloaded video into the language you want. For this, you need to make minor changes to the code.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
if you get the error "AttributeError: 'NoneType' object has no attribute 'span'" , here is what you will do. ↓

{home}/.local/lib/python3.7/site-packages/pytube/cipher.py

Line 411

transform_plan_raw = find_object_from_startpoint(raw_code, match.span()[1] - 1)

to

transform_plan_raw = js
