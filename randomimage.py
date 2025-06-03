#Chloe Lei
#2/21/25

#init
#Start by importing the necessary libraries
from PIL import Image
import requests
from io import BytesIO
import random
icecream =["https://tinyurl.com/5sdym299","https://tinyurl.com/4pfmm4sh","https://tinyurl.com/3z9a4a5v","https://tinyurl.com/3uf2zrmt","https://tinyurl.com/cw5xec5k"]
#func
#Define a function called open_image with a url parameter for the image address
def open_image(url):
    response = requests.get(url) #HTTP Request is made
    img = Image.open(BytesIO(response.content))
    img.show()

#Call your function with an image URL
def icecream_rec():
    print("Welcome to our Ice cream recommendations!")
    while True:
        choice=input("Would you like to be recommended an ice cream? (yes or no) ")
        if choice== "yes":
            num=random.randint(0,4)
            if num==0:
                open_image(icecream[0])
                print("""Chocolate ice cream is a rich and creamy treat. It has a bittersweet taste and can actually be healthy
                depending on the type of chocolate ice cream you eat.""")
            if num==1:
                open_image(icecream[1])
                print("""Coffee ice cream has a rich and robust flavor. It is generally sweeter than your usual
                    dark bitter esspresso, but still retains the same bold flavor of coffee.""")
            if num==2:
                open_image(icecream[2])
                print("""Mint Chocolate Chip ice cream is a perfect balance of sweet and refreshing. The minty taste
                    from the ice cream itself balances well with the sharp and rich taste of the chocolate.""")
            if num==3:
                open_image(icecream[3])
                print("""Hazelnut ice cream is the perfect blance of sweet, creamy, and nutty. Not only do you get a rich
                chocolate taste, you also get that rich, nutty flavor from the hazelnut itself.""")
            if num==4:
                open_image(icecream[4])
                print("""What's better than strawberry ice cream? Strawberry Cheesecake ice cream. This dessert is
                    everything a person could want. A sweet base, tart jam, and bites of cheesecake in it,
                    who doesn't love an indulgent dessert?""")
        if choice=="no":
            break

#main
icecream_rec()

#Citations
#Demyanchuk, A. (n.d.). Chocolate Ice Cream Recipe. Alyonascooking. August 21, 2029. https://www.alyonascooking.com/wp-content/uploads/2019/08/chocolate-ice-cream-recipe-19-585x878.jpg
#Coffee ice cream recipe: 5 tips for making coffee ice cream. (n.d.). Masterclass. October 16, 2023. https://images.ctfassets.net/3s5io6mnxfqz/49Bmb64tKoH5Y2t22xNDQT/56c35b070824165e889e5035d7fee2bb/AdobeStock_293699678.jpeg?w=828
#Yay or Nay: Mint Chocolate Chip Ice Cream. (n.d.). Sunwayechomedia. August 4, 2021. https://cdn.cpnscdn.com/static.coupons.com/ext/kitchme/images/recipes/800x1200/easy-mint-chocolate-chip-ice-cream_17741.jpg
#The Best Hazelnut Ice Cream. (n.d.). July 22, 2023. Elmundoeats. https://www.elmundoeats.com/wp-content/uploads/2023/07/Ice-cream-cone-in-a-glass.jpg
#Best Strawberry Cheesecake Ice Cream. (n.d.). Thefirstyearblog. https://thefirstyearblog.com/wp-content/uploads/2022/07/Strawberry-Cheesecake-Ice-Cream-Square-1.png

