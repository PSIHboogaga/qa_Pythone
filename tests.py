import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_set_book_genre_set_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    @pytest.mark.parametrize('name, genre', [['Гордость и предубеждение и зомби', 'Ужасы'], ['Что делать, если ваш кот хочет вас убить', 'Ужасы']])
    def test_get_book_genre_get_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_get_books_with_specific_genre_get_books(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        assert 'Что делать, если ваш кот хочет вас убить' in collector.get_books_with_specific_genre('Ужасы')

    def test_get_books_genre_get_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert 'Гордость и предубеждение и зомби' and 'Что делать, если ваш кот хочет вас убить' in collector.get_books_genre()

    def test_get_books_for_children_show_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        collector.add_new_book('Что делать, если хочешь какать')
        collector.set_book_genre('Что делать, если хочешь какать', 'Мультфильмы')
        assert 'Что делать, если хочешь какать' in collector.get_books_for_children()

    def test_add_book_in_favorites_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Что делать, если хочешь какать')
        collector.add_book_in_favorites('Что делать, если хочешь какать')
        assert 'Что делать, если хочешь какать' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Что делать, если хочешь какать')
        collector.add_book_in_favorites('Что делать, если хочешь какать')
        collector.delete_book_from_favorites('Что делать, если хочешь какать')
        assert 'Что делать, если хочешь какать' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_get_list(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Что делать, если хочешь какать')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Что делать, если хочешь какать')
        assert 'Что делать, если хочешь какать' and 'Что делать, если ваш кот хочет вас убить' in collector.get_list_of_favorites_books()

    def test_add_new_book_len_name_longer_then_forty(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ваш кот хочет вас убить, расчленить и съесть')
        assert 'Что делать, если ваш кот хочет вас убить, расчленить и съесть' not in collector.get_books_genre()

    def test_delete_fake_book_from_favorites_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Что делать, если хочешь какать')
        collector.add_book_in_favorites('Что делать, если хочешь какать')
        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        assert 'Что делать, если хочешь какать' in collector.get_list_of_favorites_books()
