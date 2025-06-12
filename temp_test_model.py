import tensorflow as tf
import numpy as np


model = tf.keras.models.load_model("models/efficientnet-imagenet-tsinghua.keras")


test = tf.keras.utils.image_dataset_from_directory(
    "raw_data/test_samples",
    seed=0,
    image_size=(224,224)
    )

class_names = test.class_names


def test_individual():
    individual_path = "B32829A3-EB5A-49DD-B293-087B30AB9489.jpg"

    img = tf.keras.utils.load_img(
        individual_path, target_size=(224,224)
    )
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    print(
        "This image most likely belongs to {} with a {:.2f} percent confidence."
        .format(class_names[np.argmax(score)], 100 * np.max(score))
    )


test_individual()
