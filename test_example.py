from playwright.sync_api import Page, expect
import pytest

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {"storage_state": "auth.json"}


def test_example(page: Page) -> None:
    page.goto("https://membean.com")
    expect(page.get_by_text('You are on the High School word list.')).to_be_visible()
    
 