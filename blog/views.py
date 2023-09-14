from django.shortcuts import render
from datetime import date


all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Greg",
        "date": date(2021, 9, 13),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Greg",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Greg",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when "
                   "walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "new-discoveries",
        "image": "discovery.jpg",
        "author": "Greg",
        "date": date(2023, 5, 20),
        "title": "Exciting New Discoveries",
        "excerpt": "I recently stumbled upon some exciting discoveries. Read "
                   "on to learn more!",
        "content": """
            I recently embarked on a journey of exploration, and to my amazement, I stumbled upon a treasure trove of exciting discoveries. The world around us is filled with wonder and surprises waiting to be unveiled.

            As I ventured into uncharted territory, my curiosity led me to a place where the past and the future converged. Ancient artifacts whispered stories of civilizations long gone, while cutting-edge technologies hinted at the incredible possibilities that lie ahead.

            It's fascinating how a single moment of revelation can ignite the spark of inspiration. These discoveries have not only deepened my appreciation for the world we inhabit but have also motivated me to share these remarkable findings with you.

            In the following pages, I'll take you on a journey through these exciting revelations. We'll delve into the mysteries of history, embrace the marvels of modern innovation, and celebrate the boundless potential of the human spirit.

            Join me in this captivating exploration, and let's embark on an adventure together as we unveil the secrets of these exciting new discoveries.
        """
    },
    {
        "slug": "journey-to-the-stars",
        "image": "stars.jpg",
        "author": "Greg",
        "date": date(2023, 7, 15),
        "title": "Journey to the Stars",
        "excerpt": "Venture beyond our world and explore the mysteries of the "
                   "universe. Buckle up for an astronomical journey!",
        "content": """
            Have you ever looked up at the night sky and wondered about the vast expanse of the cosmos? I certainly have. It's a humbling experience to contemplate the universe and our place within it.

            In my recent journey to the stars, I had the opportunity to explore celestial wonders that defy imagination. From distant galaxies to the intricate dance of planets, every corner of the cosmos holds its own unique story.

            Join me on this extraordinary voyage as we venture beyond our world and delve into the mysteries of the universe. We'll witness the birth of stars, ponder the existence of black holes, and contemplate the possibility of life beyond Earth.

            Buckle up for an astronomical journey that will expand your horizons and leave you in awe of the majesty of the cosmos. The universe is waiting to be discovered, and our journey to the stars begins now.
        """
    },
    {
        "slug": "culinary-adventures",
        "image": "food.jpg",
        "author": "Greg",
        "date": date(2023, 9, 5),
        "title": "Culinary Adventures",
        "excerpt": "Explore the diverse world of flavors and embark on a mouthwatering culinary journey with me.",
        "content": """
            Food has a remarkable way of bringing people together and telling stories of cultures and traditions. It's a universal language that transcends borders, and my culinary adventures have allowed me to savor the richness of this world.

            From bustling street markets to Michelin-starred restaurants, I've had the pleasure of exploring a wide array of cuisines. Each dish tells a unique tale, from the spicy aromas of Southeast Asia to the savory delights of European bistros.

            In this gastronomic journey, I invite you to join me as we discover the diverse world of flavors. We'll dive into the art of cooking, meet talented chefs, and uncover the hidden gems of the culinary world.

            Whether you're a seasoned food enthusiast or just curious to explore new tastes, prepare to embark on a mouthwatering adventure that will tantalize your senses and leave you craving for more.
        """
    },
    {
        "slug": "wonders-of-nature",
        "image": "nature.jpg",
        "author": "Greg",
        "date": date(2023, 10, 12),
        "title": "Wonders of Nature",
        "excerpt": "Nature is a masterpiece, and I'll take you on a journey to witness its breathtaking beauty and hidden secrets.",
        "content": """
            The natural world is a masterpiece, and every corner of our planet holds breathtaking beauty and hidden secrets waiting to be uncovered. In my quest to explore the wonders of nature, I've witnessed the awe-inspiring landscapes and encountered remarkable creatures that inhabit our Earth.

            From the towering peaks of majestic mountains to the serene depths of pristine oceans, nature's grandeur knows no bounds. Join me as we embark on a journey to marvel at the Northern Lights, stand in awe of ancient forests, and dive into the vibrant ecosystems beneath the waves.

            But our exploration goes beyond the surface. We'll delve into the intricate relationships that sustain life on our planet, from the smallest pollinators to the largest predators. Nature is a web of interconnected stories, and I'll guide you through this intricate tapestry.

            Prepare to be captivated by the wonders of nature, and let's celebrate the remarkable beauty and resilience of our planet together.
        """
    },
    {
        "slug": "innovations-of-tomorrow",
        "image": "innovation.jpg",
        "author": "Greg",
        "date": date(2023, 11, 8),
        "title": "Innovations of Tomorrow",
        "excerpt": "Step into the future and explore the cutting-edge innovations that are shaping our world.",
        "content": """
            The future is an exciting frontier filled with innovation and progress. In my exploration of the innovations of tomorrow, I've had the privilege of witnessing groundbreaking technologies and visionary ideas that are reshaping our world.

            From artificial intelligence that's transforming industries to sustainable solutions that address global challenges, the possibilities are limitless. Join me on a journey to meet the brilliant minds behind these innovations and explore the impact they're having on society.

            We'll delve into the realms of space exploration, renewable energy, and healthcare advancements. Together, we'll step into the future and envision the possibilities that lie ahead.

            If you're curious about what tomorrow holds and want to be on the cutting edge of progress, this is your invitation to explore the innovations that are shaping our world and defining the future.
        """
    }
]



def get_date(post):
    return post['date']

def starting_page(request):
    # sort
    sorted_posts = sorted(all_posts, key=get_date, reverse=True)
    latest_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html',
                  {'posts': latest_posts})


def posts(request):
    return render(request, 'blog/all-posts.html',
                  {'all_posts': all_posts})


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html',
                  {'post': identified_post})
