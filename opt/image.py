from PIL import Image
import imagehash

hash = imagehash.average_hash(Image.open('images/one.jpg'))
print(hash)

otherhash = imagehash.average_hash(Image.open('images/other.jpg'))
print(otherhash)

print(hash == otherhash)
print(hash - otherhash)
