import allure
import pytest

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """hook attaches a native Playwright screenshot to Allure on failure."""
    outcome = yield
    report = outcome.get_result()
    
    # only failures that happen during the actual test execution ('call') phase
    if report.when == "call" and report.failed:
        # Check if our custom maps_page fixture was used in the test
        if "maps_page" in item.funcargs:
            # Extract the raw Playwright page object from our Page Object class wrapper
            page = item.funcargs["maps_page"].page
            
            # attach the screenshot natively
            allure.attach(
                page.screenshot(type="png"),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )