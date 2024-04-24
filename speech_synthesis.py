from dotenv import load_dotenv
import os
import azure.cognitiveservices.speech as speechsdk

#Load the environment variables
load_dotenv()

# Creates an instance of a speech config with specified subscription key and service region.
speech_key = os.getenv("SPEECH_KEY")
service_region = os.getenv("SERVICE_REGION")

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
speech_config.endpoint_id = "51e82c31-a705-4ac4-9f11-23c1c20ade3d"
speech_config.speech_synthesis_voice_name = "MichelleSandfordNeural"
speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Audio24Khz160KBitRateMonoMp3)

text = "Hi, this is Michelle at Microsoft! Or is it?"
file_name = "sample2.wav"

# using the default speaker as audio output.
file_config = speechsdk.audio.AudioOutputConfig(filename=file_name)
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=file_config)

result = speech_synthesizer.speak_text_async(text).get()
# Check result
if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized for text [{}], and the audio was saved to [{}]".format(text, file_name))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))