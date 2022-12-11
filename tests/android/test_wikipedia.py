from selene import have, be
from selene.support.shared import browser
from allure import step as title

from qa_guru_python_20_mobile_2_appium.model import app


def test_search():
    app.given_opened()

    with title('Search for content'):
        browser.element('Search Wikipedia').tap()
        browser.element('#search_src_text').type('BrowserStack')

        browser.all('#page_list_item_title').should(have.size_greater_than(0))
        browser.element('«Software company based in India»').should(be.visible)

    with title('Click element'):
        browser.element('«Software company based in India»').tap()
        browser.element('«History»').should(be.visible)

    with title('Click link'):
        browser.element('//android.view.View[@content-desc="Internet Explorer"]').tap()
        browser.element('#link_preview_secondary_button').should(have.text('OPEN IN NEW TAB'))

    with title('Open article'):
        browser.element('#link_preview_primary_button').tap()
        browser.element('.android.view.View').should(have.text('Internet Explorer'))
        browser.element('«Web browser by Microsoft for Windows/Windows Server released in 1995»').should(be.visible)
