# Text reactions ==========================

follow = """
woof woof! arf! bow wow! arf arf woof!

(Ok! I will follow you and might respond to your posts. Say "stop" to me and I will stop.)
"""

unfollow = """
arf arf arf! bow wow woof woof!

(Ok! I will unfollow you and will not respond to your posts anymore. Say "start" to me if you want me to follow again.)
"""

unknown = """
woof woof woof! whine whine, bark bark!

(I don't understand, I'm just a dog and am not very smart. Say "start" to me if you want me to follow you, or "stop" to unfollow.)
"""

# Image reactions ==========================

base_image_path = "resources/images/"

image_path_for_level = [
    base_image_path + "dog_1_normal.jpg",
    base_image_path + "dog_2_zoom.jpg",
    base_image_path + "dog_3_power.jpg"
]

image_max = len(image_path_for_level)