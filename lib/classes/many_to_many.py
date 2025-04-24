class Article:
    _all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters long")
        self._title = title  # set directly since we want to make it immutable
        self.author = author
        self.magazine = magazine
        Article._all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("Title cannot be changed")  # Explicit immutability

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Author):

            self._author = value
        else:
            raise TypeError("Author must be an instance of Author")

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value
        else:
            raise TypeError("Magazine must be an instance of Magazine")

    @classmethod
    def all(cls):
        return cls._all


class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Author name must be a string")
        if len(name) == 0:
            raise ValueError("Author name must be longer than 0 characters")
        self._name = name  # Use _name to make it private

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Cannot modify author's name")


    def articles(self):
        return [article for article in Article.all() if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list(set(mag.category for mag in self.magazines()))


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            raise ValueError("Name must be a string between 2 and 16 characters long")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise ValueError("Category must be a non-empty string")



    def articles(self):
        return [article for article in Article.all() if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        from collections import Counter
        authors = [article.author for article in self.articles()]
        counts = Counter(authors)
        result = [author for author, count in counts.items() if count > 2]
        return result if result else None
