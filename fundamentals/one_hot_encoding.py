import tensorflow as tf

# create a list of indices
some_list = [0, 1, 2, 3]

# One Hot encode our list of indices
print(tf.one_hot(some_list, depth=4))

"""
tf.Tensor(
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]], shape=(4, 4), dtype=float32)
"""

# Specify custom values for one hot encoding
print(tf.one_hot(some_list, depth=4, on_value="yo I love deep learning", off_value="I also like to dance"))

"""
tf.Tensor(
[[b'yo I love deep learning' b'I also like to dance'
  b'I also like to dance' b'I also like to dance']
 [b'I also like to dance' b'yo I love deep learning'
  b'I also like to dance' b'I also like to dance']
 [b'I also like to dance' b'I also like to dance'
  b'yo I love deep learning' b'I also like to dance']
 [b'I also like to dance' b'I also like to dance' b'I also like to dance'
  b'yo I love deep learning']], shape=(4, 4), dtype=string)
"""