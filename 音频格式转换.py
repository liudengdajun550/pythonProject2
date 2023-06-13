from pydub import AudioSegment


def trans_mp3_to_other(filepath, hz):
    song = AudioSegment.from_mp3(filepath)
    song.export("安静的午后_高至豪." + str(hz), format=str(hz))


def trans_wav_to_other(filepath, hz):
    song = AudioSegment.from_wav(filepath)
    song.export("安静的午后_高至豪." + str(hz), format=str(hz))


def trans_ogg_to_other(filepath, hz):
    song = AudioSegment.from_ogg(filepath)
    song.export("安静的午后_高至豪." + str(hz), format=str(hz))


def trans_flac_to_other(filepath, hz):
    song = AudioSegment.from_file(filepath)
    song.export("安静的午后_高至豪." + str(hz), format=str(hz))


# 参数1：音频路径， 参数2：转换后的格式
trans_flac_to_other("安静的午后_高至豪.flac", "MP3")