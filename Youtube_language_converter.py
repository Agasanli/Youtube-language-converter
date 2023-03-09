import moviepy.editor as mp
import speech_recognition as sr
from pytube import YouTube
from googletrans import Translator
from gtts import gTTS
import os
import re

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        video_title = youtubeObject.title # Videonun başlığını alır
        youtubeObject.download()
        print("Video yükləmə tamamlandı.")
        print(f"Yükənən video: {video_title}") # Yüklənən videonun başlığını yazdırır
        return video_title
    except:
        print("Bir xəta baş verdi.")

def transcribe_video(video_path):
    video = mp.VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile("eng_audio.wav")

    recognizer = sr.Recognizer()
    with sr.AudioFile("eng_audio.wav") as source:
        audio_text = recognizer.record(source)

    text = recognizer.recognize_google(audio_text, language='en-US')
    with open("engdilinde.txt", "w", encoding="utf-8") as text_file:
        text_file.write(text)

def translate_text(filename):
    # translate
    translator = Translator()

    # çeviriləcək dillər
    source_lang = 'en'
    target_lang = 'tr'

    # faylı açıb və oxumaq
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    # Mətn tərcümə
    translated_text = translator.translate(text, src=source_lang, dest=target_lang)

    # eng faylını açır və tərcümə olunmuş mətni yazdırır
    with open('turkdilinde.text', 'w', encoding='utf-8') as f:
        f.write(translated_text.text)

    # oxuyur
    filename = "turkdilinde.text"
    with open(filename, "r", encoding="utf-8") as f:
        mytext = f.read()


    mytext = re.sub(r'[^\w\s]', '', mytext)

    audio = gTTS(text=mytext, lang="tr", slow=False)
    audio.save("netice.mp3")
    os.system("start netice.mp3")

link = input("YouTube video linkini daxil edin: ")
video_title = Download(link)
transcribe_video(video_title+".mp4")
translate_text("engdilinde.txt")
