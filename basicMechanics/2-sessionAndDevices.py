import tensorflow as tf

###                                                    ###
#        EXECUTE GRAPH IN SESSION v3 ON DEVICE           #
###                                                    ###
with tf.Session() as sess:
  with tf.device("/cpu:0"):
    matrix1 = tf.constant([[3., 3.]])
    matrix2 = tf.constant([[2.],[2.]])
    product = tf.matmul(matrix1, matrix2)
    result = sess.run([product])
    print(result)
    
# Devices are specified with strings. The currently supported devices are:
# "/cpu:0": The CPU of your machine.
# "/gpu:0": The GPU of your machine, if you have one.
# "/gpu:1": The second GPU of your machine, etc.
# Execute on cluster :
# with tf.Session("grpc://example.org:2222") as sess:
#   # Calls to sess.run(...) will be executed on the cluster.
#   ...