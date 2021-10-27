import speech_recognition as sr


# Use Stereo Mix device index if your class is virtual.
# Use Microphone if the it's an offline class.
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
