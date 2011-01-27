Author
------
* Maxime Gaudin

Purpose
-------
Exporting xml files to latex can be boring and a pretty common task (especially if your teachers are old school nomenclature's lover).
That's why I designed a little tool that export automaticaly your xml to a latex-friendly form.

Features
--------
* Handle 

Example
-------
Let's say you have to export this file :
	<annuaire>
		<personne>
			<nom>GAUDIN</nom>
			<prenom>Maxime</prenom>
			<email>gaudin.maxime@gmail.com</email>
		</personne>
		
		<personne>
			<nom>ST-GEORGES</nom>
			<prenom>Julie</prenom>
			<email>XXX@gmail.com</email>
		</personne>
	</annuaire>

Just call my script with : python xml2latex yourFile.xml, and then it produces (automatically):


Nothing complicated but so useful !

Better exemple
--------------
As you can see, the previous exemple works perfectly but is no so latex friendly (in an array for instance). 
That's why you have to 2 use cases :
- You have to convert xml file not written for that purpose : Then get prepared to hack latex
- You have to write a xml fil espacially for being converted to latex : Yeah, it will be cake walk !

Indeed, xml2latex supports attributes and the last xml will be better if written like :
	<annuaire>
		<personne lastName="GAUDIN" surname="Maxime" email="gaudin.maxime@gmail.com"/>
		<personne lastName="ST-GEORGES" surname="Julie" email="XXX@gmail.com"/> 
	</annuaire>

That's better, let's see the result :

