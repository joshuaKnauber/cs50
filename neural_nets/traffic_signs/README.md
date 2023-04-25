# Traffic Signs

Download dataset from https://cdn.cs50.net/ai/2020/x/projects/5/gtsrb.zip and extract to gttsrb in this directory.

## Experiments

### Conv 32 relu, Max Pooling, Flatten, Dense 128 relu, Dense 43 softmax

**10 Epochs, 100 img each** -> Training loss: 0.0796 - Training accuracy: 0.9864, Test loss: 0.7519 - Test accuracy: 0.8953

### Conv 32 relu, Max Pooling, Flatten, Dense 128 relu, Dropout 0.2, Dense 43 softmax

\+ added dropdout

**10 Epochs, 100 img each** -> Training loss: 2.5939 - accuracy: 0.2628, Test loss: 2.4773 - Test accuracy: 0.3134

### Conv 32 relu, Max Pooling, Flatten, Dense 128 relu, Dense 64 relu, Dense 43 softmax

\+ added dense layer

**10 Epochs, 100 img each** -> Training loss: 1.1338 - Training accuracy: 0.6938, Test loss: 1.2664 - Test accuracy: 0.6971

### Conv 32 relu, Max Pooling, Conv 64 relu, Max Pooling, Flatten, Dense 128 relu, Dense 43 softmax

\+ added second convolutional layer

**10 Epochs, 100 img each** -> Training loss: 0.1196 - Training accuracy: 0.9767, Test loss: 0.3949 - Test accuracy: 0.9163

### Conv 32 relu, Max Pooling, Conv 64 relu, Max Pooling, Flatten, Dense 128 relu, Dense 64 relu, Dense 43 softmax

\+ added second dense layer

**10 Epochs, 100 img each** -> Training loss: 0.2179 - Training accuracy: 0.9500, Test loss: 0.4181 - Test accuracy: 0.9087

### Conv 32 relu, Average Pooling, Conv 64 relu, Average Pooling, Flatten, Dense 128 relu, Dense 43 softmax

\+ switched to average pooling

**10 Epochs, 100 img each** -> Training loss: 0.1931 - Training accuracy: 0.9570, Test loss: 0.3667 - Test accuracy: 0.9128

### Conv 32 relu, Average Pooling, Conv 64 relu, Average Pooling, Conv 128 relu, Average Pooling Flatten, Dense 128 relu, Dense 43 softmax

\+ added third convolutional layer

**10 Epochs, 100 img each** -> Training loss: 0.3021 - Training accuracy: 0.9217, Test loss: 0.4053 - Test accuracy: 0.8953

## Testing top with all images

### Conv 32 relu, Max Pooling, Flatten, Dense 128 relu, Dense 43 softmax

**10 Epochs, all imgs** -> Training loss: 0.1966 - Training accuracy: 0.9548, Test loss: 0.3816 - Test accuracy: 0.9249

### Conv 32 relu, Max Pooling, Conv 64 relu, Max Pooling, Flatten, Dense 128 relu, Dense 43 softmax

**10 Epochs, all imgs** -> Training loss: 0.0943 - Training accuracy: 0.9765, Test loss: 0.2707 - Test accuracy: 0.9444

### Conv 32 relu, Average Pooling, Conv 64 relu, Average Pooling, Flatten, Dense 128 relu, Dense 43 softmax

**10 Epochs, all imgs** -> Training loss: 0.0714 - Training accuracy: 0.9819, Test loss: 0.1585 - Test accuracy: 0.9684

### Conv 32 relu, Average Pooling, Conv 64 relu, Average Pooling, Conv 128 relu, Average Pooling Flatten, Dense 128 relu, Dense 43 softmax

**10 Epochs, all imgs** -> Training loss: 0.0790 - Training accuracy: 0.9809, Test loss: 0.9809 - Test accuracy: 0.9781
