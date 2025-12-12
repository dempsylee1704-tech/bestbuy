import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def read_data(file_path):
    with open(file_path, "r") as fileobj:
        template_html = fileobj.read()
        return template_html

template_html = read_data("animals_template.html")

animals_data = load_data('animals_data.json')

animals_output = ""

for animal in animals_data:
    animals_output += '<li class="cards__item">\n'
    if "name" in animal:
        animals_output += f"Name: {animal['name']}<br/>\n"

    if "characteristics" in animal and "diet" in animal["characteristics"]:
        animals_output += f"Diet: {animal['characteristics']['diet']}<br/>\n"

    if "locations" in animal and len(animal["locations"]) > 0:
        animals_output += f"Location: {animal['locations'][0]}<br/>\n"

    if "type" in animal:
        animals_output += f"Type: {animal['type']}<br/>\n"
    animals_output += '</li>\n'

final_html = template_html.replace("__REPLACE_ANIMALS_INFO__", animals_output)

with open("animals.html", "w") as file:
    file.write(final_html)

print(final_html)