

    Тест на добавление двух книг
    def test_add_new_book_add_two_books(self):
        
Тест на установление жанра книги
    def test_set_book_genre_set_genre(self):
       
Параметризованный тест на вывод жанра книги по её имени
    @pytest.mark.parametrize('book_name, book_genre', [['Гордость и предубеждение и зомби', 'Ужасы'], ['Что делать, если ваш кот хочет вас убить', 'Ужасы']])
    def test_get_book_genre_get_genre(self, book_name, book_genre):
 

Тест на вывод списка книг с определённым жанром
    def test_get_books_with_specific_genre_get_books(self):

   
Тест на вывод  текущего словаря
    def test_get_books_genre_get_books(self):
      

Тест на вывод книг, которые подходят детям
    def test_get_books_for_children_show_books_for_children(self):
        
Тест на добавление книги в избранное
    def test_add_book_in_favorites_book_in_favorites(self):
      
Тест на удаление книги из избранного
    def test_delete_book_from_favorites_delete_book_from_favorites(self):
     
Тест на получение списка избранных книг
    def test_get_list_of_favorites_books_get_list(self):

Негативный тест на добавление книги с названием более 40 символов   
    def test_add_new_book_len_name_longer_then_forty(self):
   
Негативный тест на удаление несуществующей книги из избранного
    def test_delete_fake_book_from_favorites_delete_book_from_favorites(self):
        



