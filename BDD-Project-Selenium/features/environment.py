from browser import Browser


def before_all(context):
    print("Setting the browser to start!!")
    context.browser = Browser()
