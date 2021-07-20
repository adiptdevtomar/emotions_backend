from django.shortcuts import render
from emotions import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import tensorflow as tf
import pandas as pd
import pickle

class Predict():
    def predict_new(sentence):
        model = tf.keras.models.load_model("Emotion.h5")
        sentence_lst=[]
        sentence_lst.append(sentence)
        with open('tokenizer.pickle', 'rb') as handle:
            tokenizer = pickle.load(handle)
        sentence_seq=tokenizer.texts_to_sequences(sentence_lst)
        sentence_padded=tf.keras.preprocessing.sequence.pad_sequences(sentence_seq,maxlen=80,padding='post')
        ans=model.predict(sentence_padded)
        return ans

@api_view(['POST'])
def getEmotionsView(request):
    if request.method == "POST":
        serializer = serializers.EmotionsSerializer(data = request.data, context={"request":request})
        if serializer.is_valid():
            result = Predict.predict_new(serializer.data["text"])
            return Response({
                "text": serializer.data["text"],
                "result": {
                    'joy': result[0][0],
                    'anger': result[0][1],
                    'love': result[0][2],
                    'sadness': result[0][3],
                    'fear': result[0][4],
                    'surprise': result[0][5]
                }
            }, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)