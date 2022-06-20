from bs4 import BeautifulSoup
from urllib.request import urlopen
import ast

url = "http://sintegra.sefaz.to.gov.br/sintegra/servlet/wpsico01"

response = urlopen(url)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')
encontrando = soup.find('input', attrs={'name':'GXState'})
test = encontrando['value']
print(test)
dicionario = ast.literal_eval(test)
print(dicionario)


GXState = {
    "_EventName":"E'CNPJ'.",
    "_EventGridId":"",
    "_EventRowId":"",
    "GPXRECAPTCHA1_Sitekey":"6LdVbykTAAAAAHKqhQKW5pIB0ipX5PH2A8ewgg_e",
    "GPXRECAPTCHA1_Response":"03AGdBq266crwmSknGQ4tcanfY-ab1-UR4IACn6xQduY50dHdlW8-fnE9mHyH0KnshXuA9g_-_KE44UWh_oUqpH_bhuB8QE6obESYvKtntdcfQdoRyvAy3rRbVrIkACm1iATHMS4PhKfpKvH6WN9fkO4URLTcdpU6fA8wZPD2uSxgHNKbPpdRMcrFWdJ-_0CTZyOgsNsnEECw6srUWxzRyG9KTjklCGvKoZfcaehonLGFpgeXNJ9sAZxNaWfISW1WRx1HNKJRvhIai0PwQgrjdJb3RnVXixUhR3s3jG-Hn6MwLMgY3ZwPyT-FimRKm_GzSHi0Z_IFfE3U8dDyxvei2ACLzIq2ASKuxW_JbKWRI1x6z7bZ59-7iW7R7WmEglPbTtjuP-LVyZDMxqyYEqqfhh7eGMO5EP5bXgQMsbDcC3VJJ017d_NYZsRmF_FkY1imTqEsTsTCYvWOvUgwtIgPMDJZt3eNzjEfCnd_rJv-YD1mr634Cd8q1qoVuTpYC53AXOiC_3c1Xwagb9PwsMxIxAxzEbZhON0jbnmTmdkEay2ARaoolDrNU5nQ",
    "GX_FocusControl":"vCPF",
    "GX_AJAX_KEY":"62FF7BFF1334FF2D5E5E36FFFFFFFF64",
    "AJAX_SECURITY_TOKEN":"654357b1b5c4c3fd550e62984df99cc8981dfed39672d003c633c54be6fdb062",
    "GX_CMP_OBJS":{},
    "sCallerURL":"/",
    "GX_CLI_NAV":"true",
    "GX_RES_PROVIDER":"com.genexus.webpanels.GXResourceProvider","GX_THEME":"sefaz",
    "_MODE":"",
    "Mode":"",
    "IsModified":"1",
    "GPXRECAPTCHA1_Theme":"light",
    "GPXRECAPTCHA1_Visible":1
}