zdanie = input ("Wpisz zdanie/ciąg znaków, które chcesz edytować: ")
zdanie = str (zdanie)
do_zmiany = input ("Wprowadź znak/ciąg znaków, które chcesz zamienić: ")
do_zmiany = str (do_zmiany)
zmiana = input ("Wprowadź znak/ciąg znaków, które chcesz wstawić: ")
zmiana = str (zmiana)
print (zdanie.replace(do_zmiany , zmiana , ))
import sys
sys.exit();