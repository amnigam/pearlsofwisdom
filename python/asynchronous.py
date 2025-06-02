import asyncio 
import requests 

url = 'https://dog.ceo/api/breeds/image/random'     # DOG API that returns response in below format

# {
#     "message": "https://images.dog.ceo/breeds/affenpinscher/n02110627_13221.jpg",
#     "status": "success"
# }

# We want to download the dog image so we will pull out the dog image URL.
img = requests.get(url).json()['message'] 

async def fetchImg(url):
    # Download the dog image
    r = requests.get(url, stream=True)      # streaming allows content to be iterated over
    with open("dog.jpg", "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):   # iterate with a size of 1024
            f.write(chunk)
        
# When we await an aysnchronous function or co-routine it gets scheduled for execution.
# However, the await is allowed only inside an async function. 
async def start():
    print('[+] Downloading image...')
    dog_img = await fetchImg(img) 
    print('Image Downloaded')

if __name__ == '__main__':
    asyncio.run(start())        # asyncio.run is used to setup the event loop. Don't use when it is already running.
