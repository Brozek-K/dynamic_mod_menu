from compatibility_patches import publisher, validator


def validate():
    validator.validate()


def publish_patches(publish_path, image):
    publisher.publish_patches(publish_path, image)
