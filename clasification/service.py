from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D, Dropout, Activation, BatchNormalization
from keras import backend as K
from keras import optimizers, regularizers, Model
from keras.applications import densenet

from keras.preprocessing.image import load_img, img_to_array
from PIL import Image
import numpy as np
import os
from django.conf import settings


class Densenet:
    clases = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']
    img_width, img_height = 224, 224
    batch_size = 32
    num_classes = 6 
    model = None
    #load_weights_file = 'weights_save_densenet121_val_acc_83.022.h5'
    imagen = None
    
    def __init__(self, load_weights_file='weights_save_densenet121_val_acc_83.022.h5'):
        super().__init__()
        self.load_weights_file = load_weights_file

        if K.image_data_format() == 'channels_first':
            input_shape = (3, self.img_width, self.img_height)
        else:
            input_shape = (self.img_width, self.img_height, 3)

        self.model = self.generate_transfer_model(input_shape, self.num_classes)
        self.load_weights()

    def generate_transfer_model(self, input_shape, num_classes):
        # imports the pretrained model and discards the fc layer
        base_model = densenet.DenseNet121(
            include_top=False,
            weights='imagenet',
            input_tensor=None,
            input_shape=input_shape,
            pooling='max') #using max global pooling, no flatten required

        # add fc layers
        x = base_model.output
        #x = Dense(256, activation="relu")(x)
        x = Dense(256, activation="elu", kernel_regularizer=regularizers.l2(0.1))(x)
        x = Dropout(0.6)(x)
        x = BatchNormalization()(x)
        predictions = Dense(num_classes, activation="softmax")(x)

        # this is the model we will train
        model = Model(inputs=base_model.input, outputs=predictions)

        # compile model using accuracy to measure model performance and adam optimizer
        #optimizer = optimizers.Adam(lr=0.0001)
        optimizer = optimizers.SGD(lr=0.0001, momentum=0.9, nesterov=True)
        model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy', 'mse'])

        return model

    def review(self):
        self.model.summary()

    def sorter_action(self, imagen):
        print(imagen)
        im = Image.open(imagen)
        image = img_to_array(im.resize((self.img_width, self.img_height)))
        img_tensor = np.expand_dims(image, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
        img_tensor /= 255.
        # image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
        self.imagen = img_tensor
        
    def load_weights(self):
        print("loading weights")
        file_path = os.path.join(settings.BASE_DIR, 'clasification', 'pesos', self.load_weights_file)
        self.model.load_weights(file_path)

    def prediction(self):
        predicted_batch = self.model.predict(self.imagen)
        pred = predicted_batch[0]
        the_pred = np.argmax(pred)
        predicted = self.clases[the_pred] # nombre del que se predice
        val_pred = round(max(pred)*100, 2) #porcentaje
        # print(the_pred, predicted, val_pred)
        return {"pred": the_pred, "name": predicted, "porc":val_pred}
    

