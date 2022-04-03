from PIL import Image
import imagehash

# hash = imagehash.average_hash(Image.open('images/one.jpg'))
hash = imagehash.average_hash(Image.open('images/desk-iphone.jpg'))
print(hash)

# otherhash = imagehash.average_hash(Image.open('images/other.jpg'))
otherhash = imagehash.average_hash(Image.open('images/desk-ipad.jpg'))
print(otherhash)

print(hash == otherhash)
print(hash - otherhash)
