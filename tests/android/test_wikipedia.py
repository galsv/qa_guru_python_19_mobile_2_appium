from selene import have, be
from selene.support.shared import browser
from allure import step as title

from qa_guru_python_20_mobile_2_appium.model import app


def test_search():
    app.given_opened()

    with title('Search for content'):
        browser.element('Search Wikipedia').tap()
        browser.element('#search_src_text').type('BrowserStack')

    with title('Content should be found'):
        browser.all('#page_list_item_title').should(have.size_greater_than(0))
        browser.element('«Software company based in India»').should(be.visible)

