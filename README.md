xml2latex
=========

Author
------
* Maxime Gaudin

Purpose
-------
Exporting xml files to latex can be boring and a pretty common task (especially if your teachers are old school nomenclature's lover).
That's why I designed a little tool that export automaticaly your xml to a latex-friendly form.

Example
-------
Let's say you have to export this file :
	<annuaire>
		<personne>
			<nom>HEUTE</nom>
			<prenom>Thomas</prenom>
			<email>webmaster@xmlfacile.com</email>
		</personne>
		
		<personne>
			<nom>CANTAT</nom>
			<prenom>Bertrand</prenom>
			<email>noir@desir.fr</email>
		</personne>
	</annuaire>

Just call my script with : python xml2latex yourFile.xml, and then it produces (automatically):

\begin{annuaire}
	\begin{personne}
		\nom{HEUTE}
		\prenom{Thomas}
		\email{webmaster@xmlfacile.com}
	\end{personne}
	\begin{personne}
		\nom{CANTAT}
		\prenom{Bertrand}
		\email{noir@desir.fr}
	\end{personne}
\end{annuaire}

Nothing complicated but so useful !

