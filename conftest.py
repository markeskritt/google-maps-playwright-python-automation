import allure
import pytest

# hook for screenshot on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """hook attaches a native Playwright screenshot to Allure on failure."""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        if "maps_page" in item.funcargs:
            page = item.funcargs["maps_page"].page
            # attach the screenshot natively
            allure.attach(
                page.screenshot(type="png"),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )