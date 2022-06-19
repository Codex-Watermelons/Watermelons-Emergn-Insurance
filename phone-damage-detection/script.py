import numpy as np
from PIL import Image
import tensorflow as tf
import imageio as iio
from keras.preprocessing import image

def img_to_array(img, data_format='channels_last', dtype='float32'):
    """Converts a PIL Image instance to a Numpy array.
    # Arguments
        img: PIL Image instance.
        data_format: Image data format,
            either "channels_first" or "channels_last".
        dtype: Dtype to use for the returned array.
    # Returns
        A 3D Numpy array.
    # Raises
        ValueError: if invalid `img` or `data_format` is passed.
    """
    if data_format not in {'channels_first', 'channels_last'}:
        raise ValueError('Unknown data_format: %s' % data_format)
    # Numpy array x has format (height, width, channel)
    # or (channel, height, width)
    # but original PIL image has format (width, height, channel)
    x = np.asarray(img, dtype=dtype)
    if len(x.shape) == 3:
        if data_format == 'channels_first':
            x = x.transpose(2, 0, 1)
    elif len(x.shape) == 2:
        if data_format == 'channels_first':
            x = x.reshape((1, x.shape[0], x.shape[1]))
        else:
            x = x.reshape((x.shape[0], x.shape[1], 1))
    else:
        raise ValueError('Unsupported image shape: %s' % (x.shape,))
    return x

#Load the saved model
model = tf.keras.models.load_model('firemodel')
im = iio.imread("crph.png")
#Convert the captured frame into RGB
im = Image.fromarray(im, 'RGB')
#Resizing into 224x224 because we trained the model with this image size.
im = im.resize((224,224))
x = img_to_array(im)
classes = ['cracked','not-cracked']
x = np.expand_dims(x, axis=0) /255
prediction = model.predict(x)
print(prediction)
MaxPosition=np.argmax(prediction)
prediction_label=classes[MaxPosition]
print(prediction_label)