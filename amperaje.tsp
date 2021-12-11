--Reinciamos el keithley
reset()
--Lo ajustamos para medir corriente directa
dmm.measure.func = dmm.FUNC_DC_CURRENT
--Lo ajustamos a un rango de 10A
dmm.measure.range = 10
--Ajustamos la medida de nplc a 1.0
dmm.measure.nplc = 1.0
--Limpiamos la pantalla
display.clear()
--Desplegamos en pantalla completa la medicion
display.changescreen(display.SCREEN_HOME_LARGE_READING)
--Leemos la medicion
print(dmm.measure.read())