Author
------
* Maxime Gaudin

Purpose
-------
Exporting xml files to latex' arrays can be very boring, time consuming and a pretty common task (especially if your teachers are old school nomenclature's lover).
That's why I designed a little tool that export automaticaly your xml to a latex-friendly form.

Another pretty cool feature is the automatic preambule generation, see the Usage below.

Usage
-----
	usage: python xml2latex.py [args] [option]
	
	List of arguments :
	    --input (-i) : Specifies the input file.
	
	   List of options :
	       --output (-o) : Specifies the output file. (Default : stdout)
	       --print-preambule (-p) : Generate preambule. (Default : True)
	       --print-code (-c) : Generate code. (Default : True)
	       --help (-h) : Print this text.
	
	Author : Maxime Gaudin (2011)

Example
-------
** DON'T FORGET TO LOOK AT THE BETTER EXEMPLE SECTION BELOW **

Let's say you have to export this file :
	<annuaire>
		<somebody>
			<lastName>GAUDIN</lastName>
			<surname>Maxime</surname>
			<email>gaudin.maxime@gmail.com</email>
		</somebody>
		
		<somebody>
			<lastName>ST-GEORGES</lastName>
			<surname>Julie</surname>
			<email>XXX@gmail.com</email>
		</somebody>
	</annuaire>

Just call my script with : python xml2latex -c -i yourFile.xml, and then it produces (automatically):
	\begin{annuaire}
		\begin{somebody}
			\lastName{GAUDIN}
			\surname{Maxime}
			\email{gaudin.maxime@gmail.com}
		\end{somebody}
		\begin{somebody}
			\lastName{ST-GEORGES}
			\surname{Julie}
			\email{XXX@gmail.com}
		\end{somebody}
	\end{annuaire}


Nothing complicated but so useful !

Better exemple
--------------
As you can see, the previous exemple works perfectly but is no so latex friendly (if you scheduled to use it in an array for instance). 
In fact, you have 2 use cases :

- You have to convert xml file not written for that purpose : Then get prepared to hack latex
- You have to write a xml file espacially for being converted to latex : Yeah, it will be cake walk !

Indeed, xml2latex handles attributes and the last xml will be better if written like :
	<annuaire>
		<somebody lastName="GAUDIN" surname="Maxime" email="gaudin.maxime@gmail.com"/>
		<somebody lastName="ST-GEORGES" surname="Julie" email="XXX@gmail.com"/> 
	</annuaire>

That's better, let's see the result :

	\begin{annuaire}
		\somebody{GAUDIN}{Maxime}{gaudin.maxime@gmail.com}
		\somebody{ST-GEORGES}{Julie}{XXX@gmail.com}
	\end{annuaire}

BTW, it also handles empty markups like : 
	<jumpline/> 
use them to format your document !

A Last One
----------
Obviously, it handles syntax like :
	<annuaire>
		<somebody lastName="GAUDIN" surname="Maxime">gaudin.maxime@gmail.com</somebody>
		<somebody lastName="ST-GEORGES" surname="Julie">XXX@gmail.com</somebody> 
	</annuaire>

and produces :
	\begin{annuaire}
		\somebody{GAUDIN}{Maxime}{gaudin.maxime@gmail.com}
		\somebody{ST-GEORGES}{Julie}{XXX@gmail.com}
	\end{annuaire}
Advices
-------
* Use LaTex
* Contribute
* Mail me :D

