from playwright.sync_api import Playwright, sync_playwright, expect\
    
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=3000)
    context = browser.new_context(storage_state="state.json")
    page = context.new_page()
    context.tracing.start(screenshots=True,snapshots=True)
    page.goto("https://membean.com/dashboard")
    page.locator("id=startTrainingBtn").click()
    page.get_by_role("button", name="5 min.", exact=True).click()
    expect(page.locator("css=question")).to_be_visible()
    print(page.locator("css=question"))
    page.get_by_role("button", name="I’m done").click
    context.tracing.stop(path="trace.zip")
    context.close()
    browser.close()