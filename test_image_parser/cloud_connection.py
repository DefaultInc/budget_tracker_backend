import io
import os

# Use google cloud for testing
from google.cloud import vision
from google.cloud.vision import types

def get_words_from_image():
	# Instantiates a client
	client = vision.ImageAnnotatorClient()

	# The name of the image file to annotate
	file_name = os.path.join(
		os.path.dirname(__file__),
		'../img_tests/receipt9.jpg')

	# Loads the image into memory
	with io.open(file_name, 'rb') as image_file:
		content = image_file.read()

	image = types.Image(content=content)

	# Performs label detection on the image file
	response = client.text_detection(image=image)
	words = response.text_annotations
	return words

def get_from_test_data():
	with open('test_data.txt') as f:
		lines = f.read().splitlines()
		result = []
		for line in lines:
			class Word(object):
				description = ""
				def __init__(self, desc):
					self.description = desc
			result.append(Word(line))
		return result
