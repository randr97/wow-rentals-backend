import random
import string

import openai

openai.api_key = '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'


def get_random_string(length):
    # With combination of lower and upper case
    return ''.join(random.choice(string.ascii_letters) for i in range(length))


def get_text_from_ai(object_name):
    prompt = "Generate a description for an object:"
    prompt_with_object = f"{prompt} The object is a {object_name}."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt_with_object,
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].text.strip()


def get_vehicle_class_from_ai(object_name):
    vc = ' '.join([
        'Sedan', 'SUV', 'Truck', 'Compact Car', 'Luxury Car',
        'Convertible', 'Sports Car', 'Minivan', 'Electric Car', 'Hybrid'
    ])
    prompt = f"Which of the following vehicle classes i.e.: {vc} does the vehicle: {object_name} belong to"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].text.strip()
