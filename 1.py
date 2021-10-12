try:
   chislo = int (input ('Введите число: '))
   ss = int (input ('Введите целевую систему счисления: '))
except ValueError:
      print ('Ошибка') 
else:
    
    if chislo < 0:
      print ('Ошибка')
    else:

      b = ' '

      def dvoich(chislo, b):
         while chislo > 0:
              b = str (chislo % 2) + b
              chislo = chislo // 2
         print (b)
         return chislo, b 


      def vosmir(chislo, b):
         while chislo>0:
              b = str (chislo % 8) + b
              chislo = chislo // 8
         print (b)
         return chislo, b 
    
      if ss == 2:
        dvoich(chislo, b)
      elif ss == 8:
        vosmir(chislo, b)
      else: 
        print ('Ошибка')