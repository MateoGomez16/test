from playwright.sync_api import sync_playwright

def run_monthly() -> None:

    print("Hello, World!")

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto("https://portal.zondahome.com/")
            data = page.inner_text("body")
            print(f"Contenido de la página: {data[:200]}...")  # solo 200 caracteres
            browser.close()
    except Exception as e:
        print(f"Error en el scraping: {str(e)}")

    # Aquí va tu código de descarga y procesamiento
run_monthly()