import datetime
import logging
import azure.functions as func
from playwright.sync_api import sync_playwright

app = func.FunctionApp()

@app.function_name(name="mytimer")
@app.timer_trigger(schedule="*/5 * * * * *",  # Cada minuto
                   arg_name="mytimer",
                   run_on_startup=False)
def run_monthly(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    
    if mytimer.past_due:
        logging.info('The timer is past due!')
    
    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    print("Hello, World!")
"""
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto("https://portal.zondahome.com/")
            data = page.inner_text("body")
            logging.info(f"Contenido de la página: {data[:200]}...")  # solo 200 caracteres
            browser.close()
    except Exception as e:
        logging.error(f"Error en el scraping: {str(e)}")

    # Aquí va tu código de descarga y procesamiento
"""
