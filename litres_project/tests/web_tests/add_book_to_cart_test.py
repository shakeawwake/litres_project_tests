import allure
from litres_project.data.data import Book
from litres_project.pages.web.book_page import book_page


@allure.epic('Add book to cart')
@allure.label("owner", "shakeawwake")
@allure.feature("Checking whether a book has been added to cart")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_adding_book_to_cart():
    book = Book(
        name='Стоя под радугой',
        author='Фэнни Флэгг',
        url='fenni-flegg/stoya-pod-radugoy-8685881/',
        price='359 ₽'
    )

    with allure.step("Open the book page"):
        book_page.open(book)

    with allure.step("Adding the selected book to the cart"):
        book_page.adding_book_to_cart()

    with allure.step("Checking that the book has been added to the cart"):
        book_page.book_must_be_added_to_cart(book)


@allure.epic('Add book to cart')
@allure.label("owner", "shakeawwake")
@allure.feature("Checking whether a books has been added to cart")
@allure.label('microservice', 'WEB')
@allure.tag('regress', 'web', 'normal')
@allure.severity('normal')
@allure.label('layer', 'web')
def test_adding_books_to_cart():
    book1 = Book(
        name='Стоя под радугой',
        author='Фэнни Флэгг',
        url='fenni-flegg/stoya-pod-radugoy-8685881/',
        price='359 ₽'
    )

    book2 = Book(
        name='Жареные зеленые помидоры в кафе «Полустанок»',
        author='Фэнни Флэгг',
        url='fenni-flegg/zharenye-zelenye-pomidory-v-kafe-polustanok-130519/',
        price='379 ₽'
    )

    with allure.step("Open the first book page"):
        book_page.open(book1)

    with allure.step("Adding the selected book to the cart"):
        book_page.adding_book_to_cart()

    with allure.step("Open the second book page"):
        book_page.open(book2)

    with allure.step("Adding the selected book to the cart"):
        book_page.adding_book_to_cart()

    with allure.step("Checking that the books has been added to the cart"):
        book_page.books_must_be_added_to_cart(book1, book2)
