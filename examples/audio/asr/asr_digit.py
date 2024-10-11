from maix import app, nn

speech = nn.Speech("/root/models/am_3332_192_int8.mud")
speech.init(nn.SpeechDevice.DEVICE_MIC, "hw:0,0")

def callback(data: str, len: int):
    print(data)

speech.digit(640, digit_callback)

while not app.need_exit():
    frames = speech.run(1)
    if frames < 1:
        print("run out\n")
        speech.deinit()
        break