       	#!usr//bin/env python
       	# --coding: utf-8 --
        n = int(input())
	ano = int(n) 365
	mes = int(n) - (int(ano) * 365)) / 30
	dia = int(n) - (int(ano) * 365) - (int(mes) * 30) 
        
        print (int(ano), “ano(s)”)
        print (int(mes), “mes(es)”)
        print (int(dias), “dia(s)”)
