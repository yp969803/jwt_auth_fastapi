from transformers import Wav2Vec2Tokenizer, Wav2Vec2ForCTC
from IPython.display import Audio
from IPython.display import Video
import moviepy.editor as mp
import torch
import librosa
import os
import speech_recognition as sr

def VideoToText(name:str):
    video = mp.VideoFileClip("c:/Users/hp/Desktop/cltrH2/videoDownload/videos/"+name) 
    audio_file = video.audio 
    audio_file.write_audiofile("c:/Users/hp/Desktop/cltrH2/transciptModel/testdata/"+name+".wav") 

    tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
    model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

    clip_paths=[]
    for dirname, _, filenames in os.walk('c:/Users/hp/Desktop/cltrH2/transciptModel/testdata'):
      for filename in filenames:
        clip_paths+=[(os.path.join(dirname, filename))]
        
    cc = []
    for path in clip_paths[0:1]:
       input_audio, _ = librosa.load(path, sr=16000)
       input_values = tokenizer(input_audio, return_tensors="pt", padding="longest").input_values
       with torch.no_grad():
        logits = model(input_values).logits
        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = tokenizer.batch_decode(predicted_ids)[0]
        cc += [transcription]
    
    
    return cc[0]

