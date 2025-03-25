'''
  For more samples please visit https://github.com/Azure-Samples/cognitive-services-speech-sdk 
'''

import azure.cognitiveservices.speech as speechsdk

# Creates an instance of a speech config with specified subscription key and service region.
# speech_key = <the endpoint key from the deployment in speech studio>
# service_region = "eastus"

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
#speech_config.endpoint_id = <the alphanumeric code at the end of the deployment url>
speech_config.speech_synthesis_voice_name = "MichelleSandfordNeural"
speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Audio24Khz160KBitRateMonoMp3)

#text = "Hi, this is my custom voice."
#file_name = "sample.wav"
text = (
    "Hello everyone! I'm Michelle Sandford or rather, I am Michelle Sandford's Custom Neural Voice. Today I'm excited to introduce you to "
    "Microsoft Azure Custom Neural Voice. This innovative technology allows you to create "
    "a unique, customized synthetic voice for your applications. Let's dive into what it is, "
    "how to set it up, and how it works.\n\n"
    "What is Microsoft Azure Custom Neural Voice?\n\n"
    "Microsoft Azure Custom Neural Voice is a text-to-speech feature that enables you to build "
    "a highly natural-sounding voice tailored to your brand or characters. By providing human "
    "speech samples as training data, you can create a one-of-a-kind voice that represents your "
    "brand, personifies machines, or enhances user interactions with applications.\n\n"
    "How to Set It Up\n\n"
    "Setting up Custom Neural Voice involves a few key steps:\n\n"
    "Design the Voice Persona: Start by defining the persona of the voice you want to create. "
    "This includes the voice's characteristics, such as tone, pitch, and speaking style. Use a "
    "persona brief document to guide this process.\n\n"
    "Prepare the Training Data: Select and prepare the scripts that will be used for recording. "
    "These scripts should represent the various user scenarios for your voice, including different "
    "sentence types like statements, questions, and exclamations.\n\n"
    "Record the Audio Samples: Record the audio samples using a professional recording setup. For "
    "a high-quality voice, you'll need around three hundred to two thousand utterances. If you're just evaluating, you "
    "can use the CNV Lite option, which requires twenty to fifty utterances.\n\n"
    "I only used three hundred to record this voice, which is why it's not always perfect. \n\n"
    "Upload and Train the Model: Use Azure's Speech Studio to upload your recorded audio and "
    "corresponding scripts. Train the model using the provided tools. This process involves several "
    "compute hours, depending on the quality and quantity of your data.\n\n"
    "Deploy the Voice Model: Once the model is trained, deploy it to a custom endpoint. This allows "
    "you to integrate the synthetic voice into your applications.\n\n"
    "How It Works\n\n"
    "Custom Neural Voice leverages advanced neural text-to-speech technology and a multilingual, "
    "multi-speaker universal model. Here's a brief overview of the process:\n\n"
    "Data Collection: Collect high-quality audio samples and corresponding scripts.\n"
    "Model Training: Train the model using Azure's powerful AI capabilities. The model learns the "
    "nuances of the voice from the provided samples.\n"
    "Voice Deployment: Deploy the trained model to a custom endpoint, making it accessible for your "
    "applications.\n"
    "Integration: Integrate the custom voice into your applications, allowing users to interact with "
    "a natural-sounding, personalized voice.\n\n"
    "And that's it! With Microsoft Azure Custom Neural Voice, you can create a unique voice that "
    "enhances user experiences and brings your brand to life. Thank you for watching, and I hope you "
    "found this overview helpful. Until next time, take care!"
)
file_name = "CNV.wav"


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