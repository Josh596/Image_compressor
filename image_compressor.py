import click
from PIL import Image
import time
import os


#
@click.command()
@click.argument('image_url')
@click.option('--name', prompt = 'What do you want to save the file as?')
def compress(image_url, name):
	"""Program that compresses an image using pillow framework
	
	\n

	Pass image file url as an argument
	\n
	For example:python image_compressor.py 'image_url'
		 
	"""
	#Opening the image
	try:
		im = Image.open(image_url)

		prev_size_bytes = os.stat(image_url).st_size
		#Convert file_size to mb from bytes
		prev_size_mb = prev_size_bytes/(10 **(6))

		format_ = im.format
		#This line of code compresses the image
		file_loc = r"C:\Users\JOSHUA\Downloads\{}.{}".format(name, format_)
		im.save(file_loc, quality = 20, optimize = True)
		
		new_size_bytes = os.stat(file_loc).st_size
		#Convert file_size to mb from bytes
		new_size_mb = new_size_bytes/(10 **(6))


		click.echo(f'File has been compressed to {new_size_mb}mb from {prev_size_mb}mb bytes and saved to Downloads')
	except:
		click.echo(f'Make sure file is in proper format and file exists')

if __name__ == '__main__':
	compress()