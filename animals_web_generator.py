from data_fetcher import fetch_data

def serialize_animal(animal_obj):

    """Formats information about the animal fetched from the endpoint into html type"""

    #added try except
    try:
        output = ''
        output += '<li class="cards__item">'
        output += f'<div class="card__title">{animal_obj["name"].capitalize()}</div>'
        output += '<p class="card__text">'
        if 'diet' in animal_obj['characteristics']:
            output += f'<strong>Diet:</strong> {animal_obj["characteristics"]["diet"].capitalize()}<br/>\n'
        if 'locations' in animal_obj:
            output += f'<strong>Location:</strong> {', '.join(animal_obj["locations"]).title()}<br/>\n'
        if 'type' in animal_obj["characteristics"]:
            output += f'<strong>Type:</strong> {animal_obj["characteristics"]["type"].capitalize()}<br/>\n'
        output += '</p>'
        output += '</li>'
        return output
    except KeyError:
        print('Impossible to serialize.')

#new functions
def get_data_for_the_formatting(animals):
    result = ''
    if len(animals) == 0:
        return result
    for animal in animals:
        # added the check
        try:
            result += serialize_animal(animal)
        except TypeError:
            print(f"{animal} has the wrong format and was not serialized")
    return result


def read_html_file(result, name):
    with open('animals_template.html', 'r') as file:
        data = file.read()
    if len(result) == 0:
        formatted_data = data.replace('__REPLACE_ANIMALS_INFO__',
                                                f"<h1>The animal {name} doesn't exist</h1>")
    else:
        formatted_data = data.replace('__REPLACE_ANIMALS_INFO__', result)
    return formatted_data


def write_html_file(formatted_data):
    with open('animals.html', 'w') as file:
        file.write(formatted_data)
    print('Website was successfully generated to the file animals.html.')


def main():
    name = input('Enter a name of an animal: ').strip()
    animals = fetch_data(name)
    if animals is None:
        return
    result = get_data_for_the_formatting(animals)
    formatted_data = read_html_file(result, name)
    write_html_file(formatted_data)

if __name__ == '__main__':
    main()
