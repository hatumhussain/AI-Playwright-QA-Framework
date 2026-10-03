
import pytest
from pathlib import Path
from datetime import datetime
from ai.failure_analyzer import analyze_failure


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            screenshots_dir = Path("screenshots")
            screenshots_dir.mkdir(exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{item.name}_{timestamp}.png"
            screenshot_path = screenshots_dir / filename

            try:
                page.screenshot(
                    path=str(screenshot_path),
                    full_page=True
                )
                print(f"\nScreenshot saved: {screenshot_path}")
            except Exception as e:
                print(f"\nScreenshot failed: {e}")

        print("\n===== AI FAILURE ANALYSIS =====")

        try:
            error_message = str(report.longrepr)
            analysis = analyze_failure(
                item.name,
                error_message
            )
            print(analysis)

        except Exception as e:
            print(f"AI analysis skipped: {e}")