from langchain_core.documents import Document
from langchain.text_splitter import CharacterTextSplitter
import os
from dotenv import load_dotenv
import requests
load_dotenv()

# data = """
# ****** 
# Contact details of Human Customer service representative from AudioPro Company:
#  email : contact@AudioPro.in
#  mobile number : 3636565642

# ******
# Details of Product : SonicWave 2000
#    - Over-ear wireless headphones with active noise cancellation.
#    - Crystal-clear audio quality with deep bass and crisp highs.
#    - Up to 30 hours of battery life on a single charge.
#    - Adjustable headband and memory foam ear cushions for comfort.
#    - Built-in microphone for hands-free calls.
#    - price 11151 rupees
#    - discount 10% 

# ******
   
   
# Details of Product : SonicWave 2000
#    - Over-ear wireless headphones with active noise cancellation.
#    - Crystal-clear audio quality with deep bass and crisp highs.
#    - Up to 30 hours of battery life on a single charge.
#    - Adjustable headband and memory foam ear cushions for comfort.
#    - Built-in microphone for hands-free calls.
#    - price 11151 rupees
#    - discount 10%

# ******
#  Details of Product: BassBlast Pro
#    - On-ear wired headphones designed for bass enthusiasts.
#    - Powerful bass-driven sound with enhanced low frequencies.
#    - Foldable design for easy portability and storage.
#    - Adjustable padded headband for a comfortable fit.
#    - Tangle-free flat cable with in-line remote and microphone.
#    - price 1500 rupees
#    - discount 15%
#    - festival offer
# ******
#  Details of Product: AeroFit 360
#    - Sports in-ear Bluetooth headphones for active lifestyles.
#    - Sweat-resistant and ergonomic design for a secure fit.
#    - Immersive sound with emphasis on mids and highs.
#    - Up to 10 hours of playback time with quick charge feature.
#    - Ear hooks and multiple ear tip sizes included.
#    - price 12000 rupees
#    - discount 5%

# ******
#  Details of Product: StudioElite 500
#    - Premium studio monitor headphones for professional audio work.
#    - Accurate and balanced sound reproduction for critical listening.
#    - Over-ear design with plush memory foam earpads.
#    - Detachable coiled cable and foldable design for convenience.
#    - Gold-plated connectors for optimal signal transmission.
#    - price 50005 rupees
#    - discount 80%
#    - festival offer

# ******
#  Details of Product: RetroVibe 800
#    - Vintage-style wireless headphones with a classic look.
#    - Warm and nostalgic sound signature with modern technology.
#    - Up to 25 hours of wireless playback and optional wired mode.
#    - Adjustable metal sliders and faux-leather ear cushions.
#    - On-ear touch controls for music playback and calls.
#    - price 20151 rupees
#    - discount 20%
# ******
#  Details of Product: GamerXtreme 300
#    - Gaming headphones with immersive 3D audio experience.
#    - Surround sound and positional audio for competitive gaming.
#    - RGB lighting effects with customizable color options.
#    - Noise-canceling microphone with flip-up mute functionality.
#    - Compatible with PC, consoles, and mobile devices.
#    - price 25000 rupees
#    - discount 30%
# ******
#  Details of Product: KidsJamz 100
#    - Child-friendly wired headphones designed for young users.
#    - Volume-limited to protect young ears (85dB max volume).
#    - Fun and colorful designs with adjustable headband.
#    - Lightweight and durable construction for kids on the go.
#    - Built-in shareport for sharing audio with a friend.
#    - price 200 rupees
#    - discount 15%
# ******
#  Details of Product: TravelMate 600
#    - Compact and foldable wireless headphones for travelers.
#    - Active noise cancellation for a peaceful travel experience.
#    - Clear voice calls with dual beamforming microphones.
#    - Up to 20 hours of playback and quick charge feature.
#    - Comes with a hard-shell travel case.
#    - price 600 rupees
#    - discount 2%
# ******
#  Details of Product: AudiophileX 9000
#    - High-fidelity open-back headphones for audiophiles.
#    - Wide soundstage and exceptional detail in music playback.
#    - Premium materials with genuine leather and aluminum accents.
#    - Detachable oxygen-free copper cable with balanced connectors.
#    - Handcrafted design for an exquisite audio experience.
#    - price 90000 rupees
#    - discount 70%
# ******
#  Details of Product: ProComm 200
#     - Communication headphones for professional use.
#     - Clear and precise audio for conference calls and meetings.
#     - Noise-canceling microphone with flexible boom arm.
#     - Adjustable headband and comfortable ear cushions.
#     - USB and 3.5mm connectivity options.
#     - price 6000 rupees
#    - discount 15%
# ******
#  Details of Product: elite buds 5k 
#     - most elite buds you have ever seen.
#     - Clear and precise audio for conference calls and meetings.
#     - Noise-canceling microphone with flexible boom arm.
#     - Adjustable headband and comfortable ear cushions.
#     - USB and 3.5mm connectivity options.
#     - price 100000 rupees
#    - discount 25%
# """






def get_data(collection_name):
    url = os.getenv("STRAPI_CMS_API_URL")
    headers = { 'Authorization': 'Bearer ' + os.getenv("STRAPI_API_KEY") }
    print('calling ::: {}/companies?populate=*&filters[name][$eq]={}'.format(url,collection_name))
    response = requests.get('{}/companies?populate=*&filters[name][$eq]={}'.format(url,collection_name), headers=headers)
    print("\n\ngetting data from strapi .... \n\n",response)
    data = response.json()
    print(data)

    # data = {'data': [{'id': 2, 'attributes': {'createdAt': '2024-01-27T20:28:22.232Z', 'updatedAt': '2024-01-27T20:34:34.246Z', 'publishedAt': '2024-01-27T20:28:27.322Z', 'name': 'jjk', 'contact': {'id': 7, 'email': 'jjk@cc.com', 'number': '4545454546'}, 'products': [{'id': 10, 'name': 'jjkprod', 'url': 'asdfasdf', 'discount': 55, 'description': [{'type': 'paragraph', 'children': [{'text': 'asdf jjk', 'type': 'text'}]}], 'price': 8988}]}}], 'meta': {'pagination': {'page': 1, 'pageSize': 25, 'pageCount': 1, 'total': 1}}}
    if len(data["data"]) != 0 :
        company_data = ''
        name = data["data"][0]["attributes"]["name"]
        if name != collection_name :
            raise ValueError("fetched data and data you are trying to update are different , company name are different")
        company_data = company_data + "****** Contact details of Human Customer service representative from {} Company: \n email : {} \n mobile number : {} \n".format(collection_name , data["data"][0]["attributes"]["contact"]["email"] , data["data"][0]["attributes"]["contact"]["number"])

        for product in data["data"][0]["attributes"]["products"] :
            company_data = company_data + "\n\n****** Details of Product : {productName} \n- discount {productDiscount}% \n- price {productPrice} rupees\n{productDescription}".format(productName = product['name'] , productDiscount= product['discount'] , productPrice = product['price'] ,productDescription= product['description'])

    print("\n\n============================\nplain data \n",company_data)
    return company_data


def get_docs(collection_name):
    data = get_data(collection_name)
    text_splitter = CharacterTextSplitter(
        separator = "******",
        chunk_size=900,
        chunk_overlap=0
    )
    dataDocument = [Document(page_content=data, metadata={"namespace": collection_name})]
    docs = text_splitter.split_documents(dataDocument)
    return docs








def main():
    docs = get_docs("jjk")
    print(docs[0].page_content)

if __name__ == "__main__" :
    main()