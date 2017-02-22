import tensorflow as tf

# A feed temporarily replaces the output of an operation with a tensor value. 
# You supply feed data as an argument to a run() call. The feed is only used for the run call to which it is passed. 
# The most common use case involves designating specific operations to be "feed" operations by using tf.placeholder() to create them:

input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.mul(input1, input2)

with tf.Session() as sess:
  print(sess.run([output], feed_dict={input1:[7., 2.], input2:[2., 4.]}))

# output:
# [array([ 14.], dtype=float32)]