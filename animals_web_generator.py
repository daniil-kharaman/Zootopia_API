from data_fetcher import fetch_data

def serialize_animal(animal_obj):
    '''Formats information about the animal fetched from the endpoint into html type'''
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


def main():
    name = input('Enter a name of an animal: ').strip()
    animals = fetch_data(name)
    result = ''
    for animal in animals:
        result += serialize_animal(animal)
    with open('animals_template.html', 'r') as file:
        data = file.read()
    formatted_data = data.replace('__REPLACE_ANIMALS_INFO__', result)
    if len(animals) == 0:
        '<h1>My Animal Repository</h1>'
        formatted_data = formatted_data.replace('<h1>My Animal Repository</h1>',
                                                f"<h1>The animal {name} doesn't exist</h1>")
    with open('animals.html', 'w') as file:
        file.write(formatted_data)
    print('Website was successfully generated to the file animals.html.')


if __name__ == '__main__':
    main()