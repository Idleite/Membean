from playwright.sync_api import Playwright, sync_playwright, expect


# def run(playwright: Playwright) -> None:
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    context.tracing.start(screenshots=True,snapshots=True)
    page.goto("https://membean.com/login")
    page.get_by_role("link", name="google logo Sign In with").click()
    page.get_by_label("Email or phone").fill("hesses2027@hillelyeshiva.org")
    page.get_by_label("Email or phone").press("Enter")
    page.get_by_label("Enter your password").fill("Goyanks12345")
    page.get_by_label("Enter your password").press("Enter")
    
    expect(page.get_by_role("link", name="Start Training")).to_be_visible()
    storage = context.storage_state(path="state.json")
    # ---------------------
    context.tracing.stop(path="trace.zip")
    context.close()
    browser.close()


# with sync_playwright() as playwright:
#     run(playwright)
