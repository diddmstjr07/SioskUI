class SpeechToTextConverter:
    def __init__(self):
        import speech_recognition
        self.detection = speech_recognition
        self.detector = self.detection.Recognizer()
        self.recognizer = self.detection.Recognizer()
        self.error_non = speech_recognition.exceptions.UnknownValueError
        self.error_wait = speech_recognition.exceptions.WaitTimeoutError

    def check_microphone(self):
        detected = []
        for index, name in enumerate(self.detection.Microphone.list_microphone_names()):
            detected.append(str(f"[{index}] {name}"))
        return detected
    
    def Detecting(self, index):
        mic = self.detection.Microphone(device_index=index)
        try:
            with mic as source:
                audio = self.detector.listen(source, timeout = 1, phrase_time_limit = 10)
                result = self.detector.recognize_google(audio, language='ko-KR')
                return result
        except self.error_non:
            print("Non Voice Detected")
            return None
        except self.error_wait:
            print("Non Voice Detected")
            return None