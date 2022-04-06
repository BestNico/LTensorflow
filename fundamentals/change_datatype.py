from numpy import dtype
import tensorflow as tf

# Create a new tensor with default datatype (float32)

A = tf.constant([1.7, 7.4])
print(A)

B = tf.constant([7, 10])
print(B)

# Change from float32 to float16 
print(tf.cast(A, dtype=tf.float16))

# Change from int32 to float32
print(tf.cast(B, dtype=tf.float32)) 