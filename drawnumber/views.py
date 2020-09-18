from keras.models import load_model
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from io import BytesIO
import numpy as np
import base64
import re

model = load_model('digit_model.h5')

def home_page(request):
    return render(request, 'home_page.html')

@csrf_exempt
def img_data(request):
    if request.method == "POST":
        data = request.POST['data']
        base64_data = re.sub('^data:image/.+;base64,', '', data)
        img_bytes = base64.b64decode(base64_data)
        img = Image.open(BytesIO(img_bytes)).convert("L")
        img = img.resize((28, 28), Image.ANTIALIAS)
        img_array = np.asarray(img).reshape(1, 28, 28, 1).astype("float32") / 255
        number = np.argmax(model.predict(img_array), axis=-1)
        return HttpResponse(number)
    else:
        return HttpResponse("unsuccesful")