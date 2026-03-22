from utils.driver import launch_browser

def before_all(context):
    context.playwright, context.browser, context.context, context.page = launch_browser()

def after_all(context):
    context.browser.close()
    context.playwright.stop()

# def before_step(context, step):
#     context.page.wait_for_timeout(500)

def after_step(context, step):
    # context.page.wait_for_timeout(500)
    if step.status == "failed":
        context.page.screenshot(path=f"screenshots/{step.name}.png")