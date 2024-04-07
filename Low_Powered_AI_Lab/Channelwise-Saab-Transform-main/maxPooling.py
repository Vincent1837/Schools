import tensorflow as tf

# Example feature map (4x4) represented as a 2D array
# This could be an output from a convolutional layer
feature_map = tf.constant([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
], dtype=tf.float32)

# Reshape to match expected input shape for tf.nn.max_pool
feature_map = tf.reshape(feature_map, [1, 4, 4, 1])

# Apply max pooling with a filter size of 2x2 and stride of 2x2
pool_output = tf.nn.max_pool2d(
    feature_map,
    ksize=[1, 2, 2, 1],  # Size of the sliding window for each dimension of the input tensor
    strides=[1, 2, 2, 1],  # Stride of the sliding window for each dimension of the input tensor
    padding='VALID'  # No padding is applied to the input
)

print("Original Feature Map:\n", feature_map.numpy().squeeze())
print("\nOutput Feature Map after Max Pooling:\n", pool_output.numpy().squeeze())
