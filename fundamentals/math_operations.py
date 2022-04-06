import tensorflow as tf

# squaring log square root

H = tf.range(1, 10)

## squaring
print(tf.square(H))

## Find square root (required non-int type)
print(tf.sqrt(tf.cast(H, dtype=tf.float32)))

## Find log (required non-int type)
print(tf.math.log(tf.cast(H, dtype=tf.float32)))
