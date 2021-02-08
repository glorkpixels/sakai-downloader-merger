import ffmpeg

input_video = ffmpeg.input('video.mp4')

input_audio = ffmpeg.input('sound.mp4')


try:
    
    ffmpeg.concat(input_video, input_audio, v=1, a=1).output('finished_video.mp4').run()
except Exception as e:
    print(e)