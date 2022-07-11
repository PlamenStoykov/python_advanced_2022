from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        result = []
        for i in range(pages):
            result.append([])
        self.photos = result

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label):
        chosen_page = None
        chosen_slot = None
        for index, page in enumerate(self.photos):
            if len(page) < 4:
                page.append(label)
                chosen_page = index
                chosen_slot = len(page) - 1
                return f"{label} photo added successfully on page {chosen_page + 1} slot {chosen_slot + 1}"
        return f"No more free slots"

    def display(self):

        separator = 11 * '-'
        result = separator + '\n'
        for page in self.photos:
            result += ' '.join(['[]' for _ in page]) + '\n'
            result += separator + '\n'
        return result.strip()

