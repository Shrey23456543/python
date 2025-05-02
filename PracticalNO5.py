import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, LeakyReLU, BatchNormalization, Reshape, Flatten, Dropout
from keras.datasets import fashion_mnist

# Load and preprocess the data
(train_x, train_y), (val_x, val_y) = fashion_mnist.load_data()
train_x = train_x / 255.
val_x = val_x / 255.
train_x = train_x.reshape(-1, 28, 28, 1)

# Display sample images
fig, axe = plt.subplots(2, 2)
idx = 0
for i in range(2):
    for j in range(2):
        axe[i, j].imshow(train_x[idx].reshape(28, 28), cmap='gray')
        idx += 1
plt.show()

# Normalize between -1 and 1
train_x = train_x * 2 - 1
print(train_x.max(), train_x.min())

# Generator model
generator = Sequential()
generator.add(Dense(512, input_shape=[100]))
generator.add(LeakyReLU(alpha=0.2))
generator.add(BatchNormalization(momentum=0.8))
generator.add(Dense(256))
generator.add(LeakyReLU(alpha=0.2))
generator.add(BatchNormalization(momentum=0.8))
generator.add(Dense(128))
generator.add(LeakyReLU(alpha=0.2))
generator.add(BatchNormalization(momentum=0.8))
generator.add(Dense(784))
generator.add(Reshape([28, 28, 1]))
generator.summary()

# Discriminator model
discriminator = Sequential()
discriminator.add(Flatten(input_shape=[28, 28, 1]))
discriminator.add(Dense(256))
discriminator.add(LeakyReLU(alpha=0.2))
discriminator.add(Dropout(0.5))
discriminator.add(Dense(128))
discriminator.add(LeakyReLU(alpha=0.2))
discriminator.add(Dropout(0.5))
discriminator.add(Dense(64))
discriminator.add(LeakyReLU(alpha=0.2))
discriminator.add(Dropout(0.5))
discriminator.add(Dense(1, activation='sigmoid'))
discriminator.summary()

# Build GAN model
discriminator.compile(optimizer='adam', loss='binary_crossentropy')
discriminator.trainable = False

GAN = Sequential([generator, discriminator])
GAN.compile(optimizer='adam', loss='binary_crossentropy')
GAN.summary()

# Training the GAN
epochs = 30
batch_size = 100
noise_shape = 100

for epoch in range(epochs):
    print(f"Currently on Epoch {epoch+1}")
    for i in range(train_x.shape[0] // batch_size):
        if (i + 1) % 100 == 0:
            print(f"\tCurrently on batch number {i+1} of {train_x.shape[0] // batch_size}")
        
        noise = np.random.normal(0, 1, size=[batch_size, noise_shape])
        gen_image = generator.predict_on_batch(noise)

        real_images = train_x[i * batch_size: (i + 1) * batch_size]

        # Train discriminator on real images
        real_labels = np.ones((batch_size, 1))
        discriminator.trainable = True
        d_loss_real = discriminator.train_on_batch(real_images, real_labels)

        # Train discriminator on fake images
        fake_labels = np.zeros((batch_size, 1))
        d_loss_fake = discriminator.train_on_batch(gen_image, fake_labels)

        # Train generator via GAN
        noise = np.random.normal(0, 1, size=[batch_size, noise_shape])
        valid_y = np.ones((batch_size, 1))
        discriminator.trainable = False
        d_g_loss_batch = GAN.train_on_batch(noise, valid_y)

    # Plot generated images every 10 epochs
    if epoch % 10 == 0:
        samples = 10
        x_fake = generator.predict(np.random.normal(0, 1, size=(samples, 100)))
        for k in range(samples):
            plt.subplot(2, 5, k + 1)
            plt.imshow(x_fake[k].reshape(28, 28), cmap='gray')
            plt.xticks([])
            plt.yticks([])
        plt.tight_layout()
        plt.show()

print("Training is complete")

# Visualize final generated images
noise = np.random.normal(0, 1, size=[10, noise_shape])
gen_image = generator.predict(noise)

fig, axe = plt.subplots(2, 5)
fig.suptitle('Generated Images from Noise using GANs')
idx = 0
for i in range(2):
    for j in range(5):
        axe[i, j].imshow(gen_image[idx].reshape(28, 28), cmap='gray')
        axe[i, j].axis('off')
        idx += 1
plt.tight_layout()
plt.show()
