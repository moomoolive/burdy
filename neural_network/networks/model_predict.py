import tensorflow as tf

string = tf.constant(['I love amazon echo'], dtype=tf.string)

new_model = tf.keras.models.load_model('my_model')

print(new_model.predict(string)[0][0])