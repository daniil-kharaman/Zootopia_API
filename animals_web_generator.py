import requests

URL = 'https://api.api-ninjas.com/v1/animals'
API_KEY = 'FK7SfqcRurie9/3b0BD0zw==eBitGH8yUszBhhSn'


def serialize_animal(animal_obj):
    output = ''
    output += '<li class="cards__item">'
    output += f'<div class="card__title">{animal_obj['name'].capitalize()}</div>'
    output += '<p class="card__text">'
    if 'diet' in animal_obj['characteristics']:
        output += f'<strong>Diet:</strong> {animal_obj['characteristics']['diet'].capitalize()}<br/>\n'
    if 'locations' in animal_obj:
        output += f'<strong>Location:</strong> {', '.join(animal_obj['locations']).title()}<br/>\n'
    if 'type' in animal_obj['characteristics']:
        output += f'<strong>Type:</strong> {animal_obj['characteristics']['type'].capitalize()}<br/>\n'
    output += '</p>'
    output += '</li>'
    return output


def get_animals(url, key):
    params = {
        'name': 'fox'
    }
    headers = {
        'X-Api-Key': key
    }
    response = requests.get(url, params=params, headers=headers)
    parsed_response = response.json()
    return parsed_response


def main():
    animals = get_animals(URL, API_KEY)
    result = ''
    for animal in animals:
        result += serialize_animal(animal)
    with open('animals_template.html', 'r') as file:
        data = file.read()
    formatted_data = data.replace('__REPLACE_ANIMALS_INFO__', result)
    with open('animals.html', 'w') as file:
        file.write(formatted_data)


if __name__ == '__main__':
    main()