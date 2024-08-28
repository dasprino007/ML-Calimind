#!/usr/bin/env python
import asyncio
import re
import cv2
import random
import base64
import json

from websockets.asyncio.server import serve

def send_Image(filename='images.jpg'):
    dataType = re.findall(r"\W+$", filename)
    with open(filename, 'rb') as imgfile:
        base64_bytes = base64.b64encode(imgfile.read())
        base64_encoded = base64_bytes.decode()
    return json.dumps({"url":base64_encoded, "Type": dataType})

async def Image(websocket):
    while True:
        await websocket.send(send_Image())
        await asyncio.sleep(random.random() * 2 + 1)
    

async def main():
    async with serve(Image, "localhost", 5765):
        await asyncio.get_running_loop().create_future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())