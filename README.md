# Handwritten Text Recognition with TensorFlow

## Dataset:
+   I have used Iam-on-line-handwriting-database Dataset.


## Model:
+   Used model consist of ResNet50+2 RNN (Bi-LSTM) for text recognition.
+   ResNet as backbone and BiLSTM as refine layer. 
+   The performance is not so good.
+   But this model learning is good. Need to do some hyperparameters tuning to get good results.

## For train:

        python main.py --train


## For testing 

        python main.py --validate


