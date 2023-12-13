from gtts import gTTS
import os

def text_to_speech(input_file, output_file):
    # Read the content of the text file
    with open(input_file, 'r' , encoding='utf-8') as file:
        text = file.read()

    # Create a gTTS object
    tts = gTTS(text, lang='en')

    # Save the speech as an audio file
    tts.save(output_file)

    # Play the audio file
    os.system(f'start {output_file}')

if __name__ == "__main__":
    input_file = 'Python Mini Projects\Convert Text To Audio\input.txt'  # Replace with the path to your text file
    output_file = 'Python Mini Projects\Convert Text To Audio\audio.mp3'  # Replace with the desired output audio file path

    text_to_speech(input_file, output_file)
    print("Audio is file is ready. Please check in your output file")
