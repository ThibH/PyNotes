import os
import json
from uuid import uuid4

from package.api.constants import NOTES_DIR


class Note:
    def __init__(self, title="", content="", uuid=None):
        self.uuid = str(uuid4())
        self.title = title
        self._content = content

    def __repr__(self):
        return f"{self.title} ({self.uuid})"

    def __str__(self):
        return self.title

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if isinstance(value, str):
            self._content = value
        else:
            raise TypeError("Valeur invalide (besoin d'une chaîne de caractères).")

    def delete(self):
        os.remove(self.path)
        if os.path.exists(self.path):
            return False
        return True

    @property
    def path(self):
        return os.path.join(NOTES_DIR, self.uuid + ".json")

    def save(self):
        if not os.path.exists(NOTES_DIR):
            os.makedirs(NOTES_DIR)

        data = {"title": self.title, "content": self.content}
        with open(self.path, "w") as f:
            json.dump(data, f, indent=4)

if __name__ == '__main__':
    n = Note(title="Ceci est une note", content="Ceci est un contenu")
    n.uuid = "Entrez l'uuid d'une note existante sur le disque."
    n.delete()
