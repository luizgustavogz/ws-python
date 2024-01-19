# json.dump e json.load com arquivos
import json
import os

FILE_NAME = 'Aula177.json'
FILE_ABSOLUT_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        FILE_NAME
    )
)

string_json = '''
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
'''
