def main(image):
    import requests
    # If you are using a Jupyter notebook, uncomment the following line.
    # %matplotlib inline
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle
    from PIL import Image
    from io import BytesIO
    import os
    import sys

    endpoint = 'https://recognizetextf.cognitiveservices.azure.com/'
    ocr_url = endpoint + "vision/v2.1/ocr"

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-Type': 'application/octet-stream',
    }
    params = {'visualFeatures': 'Description'}
    response = requests.post(ocr_url, headers=headers,
                             params=params, data=image)

    response.raise_for_status()
    analysis = response.json()

    # Extract the word bounding boxes and text.
    line_infos = [region["lines"] for region in analysis["regions"]]
    word_infos = []
    for line in line_infos:
        for word_metadata in line:
            for word_info in word_metadata["words"]:
                word_infos.append(word_info)

    # Output Text
    text = ''
    for word in word_infos:
        text = text+' '+word['text']

    return text