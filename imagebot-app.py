import requests
import base64
import json
import random
import time

#Set API key
HYPERBOLIC_API_KEY = "YOUR_API_KEY_HERE"

#Set API endpoint and headers
url = "https://api.hyperbolic.xyz/v1/image/generation"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {HYPERBOLIC_API_KEY}"
}

#List of prompts
prompts = [
    {"prompt": "a photo of an astronaut riding a horse on mars", "filename": "astronaut_on_mars.jpg"},
    {"prompt": "a futuristic cityscape with sleek skyscrapers and flying cars", "filename": "futuristic_cityscape.jpg"},
    {"prompt": "a surrealist painting of a melting clock", "filename": "melting_clock.jpg"},
    {"prompt": "a scenic landscape of a misty mountain range", "filename": "misty_mountains.jpg"},
    {"prompt": "A futuristic cityscape with sleek skyscrapers and flying cars", "filename": "futuristic_cityscape.jpg"},
    {"prompt": "A scenic landscape of a misty mountain range", "filename": "misty_mountains.jpg"},
    {"prompt": "A surrealist painting of a melting clock", "filename": "melting_clock.jpg"},
    {"prompt": "A photo of an astronaut riding a horse on Mars", "filename": "astronaut_on_mars.jpg"},
    {"prompt": "A futuristic underwater city with glowing sea creatures", "filename": "underwater_city.jpg"},
    {"prompt": "A fantasy landscape with dragons and medieval castles", "filename": "fantasy_landscape.jpg"},
    {"prompt": "A futuristic robot standing on a cliff overlooking a city", "filename": "futuristic_robot.jpg"},
    {"prompt": "A scenic landscape of a serene lake at sunset", "filename": "serene_lake.jpg"},
    {"prompt": "A surrealist painting of a dreamlike world with strange creatures", "filename": "dreamlike_world.jpg"},
    {"prompt": "A photo of a person standing on the edge of a massive waterfall", "filename": "waterfall.jpg"},
    {"prompt": "A futuristic cityscape with towering skyscrapers and advanced technology", "filename": "advanced_cityscape.jpg"},
    {"prompt": "A fantasy landscape with unicorns and rainbows", "filename": "unicorn_landscape.jpg"},
    {"prompt": "A futuristic space station orbiting a distant planet", "filename": "space_station.jpg"},
    {"prompt": "A scenic landscape of a rolling hillside with wildflowers", "filename": "rolling_hills.jpg"},
    {"prompt": "A surrealist painting of a world with distorted gravity", "filename": "distorted_gravity.jpg"},
    {"prompt": "A photo of a person floating in mid-air with a cityscape behind them", "filename": "floating_person.jpg"},
    {"prompt": "A futuristic cityscape with advanced transportation systems", "filename": "advanced_transportation.jpg"},
    {"prompt": "A fantasy landscape with mermaids and underwater kingdoms", "filename": "mermaid_landscape.jpg"},
    {"prompt": "A futuristic laboratory with scientists working on advanced technology", "filename": "futuristic_laboratory.jpg"},
    {"prompt": "A scenic landscape of a peaceful forest with a stream running through it", "filename": "peaceful_forest.jpg"},
    {"prompt": "A surrealist painting of a world with strange and fantastical creatures", "filename": "fantastical_creatures.jpg"},
    {"prompt": "A photo of a person standing on the surface of the Moon", "filename": "moon_surface.jpg"},
    {"prompt": "A futuristic cityscape with towering skyscrapers and advanced architecture", "filename": "advanced_architecture.jpg"},
    {"prompt": "A fantasy landscape with wizards and magical kingdoms", "filename": "wizard_landscape.jpg"},
    {"prompt": "A futuristic underwater laboratory with scientists studying marine life", "filename": "underwater_laboratory.jpg"},
    {"prompt": "A scenic landscape of a majestic mountain range with snow-capped peaks", "filename": "majestic_mountains.jpg"},
    {"prompt": "A surrealist painting of a world with distorted time and space", "filename": "distorted_time.jpg"},
    {"prompt": "A photo of a person flying through the air with a cityscape behind them", "filename": "flying_person.jpg"},
    {"prompt": "A futuristic cityscape with advanced sustainable energy systems", "filename": "sustainable_energy.jpg"},
    {"prompt": "A fantasy landscape with elves and ancient forests", "filename": "elf_landscape.jpg"},
    {"prompt": "A futuristic space exploration vehicle landing on a distant planet", "filename": "space_exploration.jpg"},
    {"prompt": "A scenic landscape of a serene ocean beach at sunset", "filename": "serene_beach.jpg"},
    {"prompt": "A surrealist painting of a world with strange and fantastical architecture", "filename": "fantastical_architecture.jpg"},
    {"prompt": "A photo of a person standing on the edge of a massive canyon", "filename": "canyon_edge.jpg"},
    {"prompt": "A futuristic cityscape with advanced transportation systems and flying cars", "filename": "advanced_transportation.jpg"},
    {"prompt": "A fantasy landscape with dwarves and underground kingdoms", "filename": "dwarf_landscape.jpg"},
    {"prompt": "A futuristic laboratory with scientists working on advanced artificial intelligence", "filename": "ai_laboratory.jpg"},
    {"prompt": "A scenic landscape of a peaceful meadow with wildflowers", "filename": "peaceful_meadow.jpg"},
    {"prompt": "A surrealist painting of a world with distorted reality", "filename": "distorted_reality.jpg"},
    {"prompt": "A photo of a person floating in mid-air with a futuristic cityscape behind them", "filename": "floating_person.jpg"},
    {"prompt": "A futuristic cityscape with advanced sustainable energy systems and green architecture", "filename": "sustainable_city.jpg"},
    {"prompt": "A fantasy landscape with vampires and dark castles", "filename": "vampire_landscape.jpg"},
    {"prompt": "A futuristic space station orbiting a distant planet with advanced technology", "filename": "space_station.jpg"},
    {"prompt": "A scenic landscape of a serene lake at sunrise", "filename": "serene_lake.jpg"},
    {"prompt": "A surrealist painting of a world with strange and fantastical creatures", "filename": "fantastical_creatures.jpg"},
    {"prompt": "A photo of a person standing on the surface of Mars", "filename": "mars_surface.jpg"},
    {"prompt": "A futuristic cityscape with advanced transportation systems and hyperloops", "filename": "hyperloop_city.jpg"},
    {"prompt": "A fantasy landscape with werewolves and full moons", "filename": "werewolf_landscape.jpg"},
    {"prompt": "A futuristic laboratory with scientists working on advanced biotechnology", "filename": "biotech_laboratory.jpg"},
    {"prompt": "A scenic landscape of a peaceful forest with a stream running through it", "filename": "peaceful_forest.jpg"},
    {"prompt": "A surrealist painting of a world with distorted time and space", "filename": "distorted_time.jpg"},
    {"prompt": "A photo of a person flying through the air with a futuristic cityscape behind them", "filename": "flying_person.jpg"},
    {"prompt": "A futuristic cityscape with advanced sustainable energy systems and eco-friendly architecture", "filename": "eco_friendly_city.jpg"},
    {"prompt": "A fantasy landscape with giants and mythical creatures", "filename": "giant_landscape.jpg"},
    {"prompt": "A futuristic space exploration vehicle landing on a distant planet", "filename": "space_exploration.jpg"},
    {"prompt": "A scenic landscape of a serene ocean beach at sunset", "filename": "serene_beach.jpg"},
    {"prompt": "A surrealist painting of a world with strange and fantastical architecture", "filename": "fantastical_architecture.jpg"},
    {"prompt": "A photo of a person standing on the edge of a massive canyon", "filename": "canyon_edge.jpg"},
    {"prompt": "A futuristic cityscape with advanced transportation systems and flying cars", "filename": "advanced_transportation.jpg"},
    {"prompt": "A fantasy landscape with magical creatures and enchanted forests", "filename": "magical_landscape.jpg"},
    {"prompt": "A futuristic laboratory with scientists working on advanced nanotechnology", "filename": "nanotech_laboratory.jpg"},
    {"prompt": "A scenic landscape of a peaceful mountain lake with a reflection of the surrounding mountains", "filename": "peaceful_lake.jpg"},
    {"prompt": "A surrealist painting of a world with distorted reality and strange creatures", "filename": "distorted_reality.jpg"},
    {"prompt": "A photo of a person floating in mid-air with a futuristic cityscape behind them", "filename": "floating_person.jpg"},
    {"prompt": "A futuristic cityscape with advanced sustainable energy systems and green architecture", "filename": "sustainable_city.jpg"}
    # Add more prompts here...
]


def send_request(data, filename):
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        image_data = response.json()["images"][0]["image"]
        decoded_image = base64.b64decode(image_data)
        with open(filename, "wb") as f:
            f.write(decoded_image)
        print(f"Image saved to {filename}")
    else:
        print(f"Failed to generate image: {response.text}")


def generate_image():
    prompt = random.choice(prompts)
    print(f"Selected Prompt: {prompt['prompt']}")
    data = {
        "model_name": "SDXL1.0-base",
        "prompt": prompt["prompt"],
        "height": 1024,
        "width": 1024,
        "backend": "auto"
    }
    send_request(data, prompt["filename"])
    delay = random.randint(60, 120)  # Random delay between 1-2 minutes
    print(f"Waiting for {delay} seconds...")
    time.sleep(delay)


while True:
    generate_image()
