import allure
import yaml

from pages.login_page import LoginPage


@allure.feature('Страница авторизации')
class TestLoginPage:
    """Тесты для страницы авторизации"""
    with open("./config.yaml") as f:
        data = yaml.safe_load(f)

    email = data["email"]
    password = data["password"]
    wr_email = data["incorrect_email"]
    wr_password = data["incorrect_password"]
    url_login = data["url_login"]

    @allure.title('Проверка заголовка')
    def test_login_page(self, driver):
        login_page = LoginPage(driver, self.url_login)
        login_page.open()
        assert login_page.get_title() == 'Авторизация', "Page not found"

    @allure.title('Проверка корректной авторизации')
    def test_correct_fill(self, driver):
        login_page = LoginPage(driver, self.url_login)
        login_page.open()
        url = login_page.correct_fill_all_fields(self.email, self.password)
        assert url == 'https://goaqua.ru/my-account/', "Correct authorization failed"

    @allure.title('Проверка некорректной авторизации')
    def test_incorrect_fill(self, driver):
        login_page = LoginPage(driver, self.url_login)
        login_page.open()
        text = login_page.incorrect_fill_all_fields(self.wr_email, self.wr_password)
        assert text == 'Неправильно заполнены поля E-Mail и/или пароль!', "Incorrect authorization failed"
