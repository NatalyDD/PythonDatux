def consultapdolar():
    import requests
    url="https://api.apis.net.pe/v1/tipo-cambio-sunat"
    respuesta=requests.get(url)
    res=respuesta.json()
    dolar_compra = res['compra']
    dolar_venta = res['venta']
    origen = res ['origen']
    moneda = res ['moneda']
    fecha = res ['fecha']
    print("El valor de compra del dolar es: ",dolar_compra)
    print("El valor de venta del dolar es: ",dolar_venta)
    print("Esta se información se extrajo de: ",origen)
    print("Moneda evaluada: ",moneda)
    print("Fecha de consulta: ",fecha)

