# Python-mécatronique: Python scientifique au département mécatronique de l'ENS Rennes

Les instructions ci-dessous ont été élaborées pour que tout mécatronicien et toute mécatronicienne ait accès à un environnement logiciel Python scientifique standardisé et fonctionnel.

Plus tard, vous pourrez faire évoluer votre installation initiale de Miniforge au gré de vos besoins. Il n'y aura pas de problème pour changer de 'distribution' Python (ou de système d'exploitation) plus tard: vous ne serez pas enfermé.e.s dans un seul système, et vous pourrez déménager vos programmes et les utiliser ailleurs.

Dans nos propres travaux au laboratoire, nous nous basons essentiellement sur les principales bibliothèques de l'écosystème Python scientifique: NumPy-SciPy-Matplotlib-Xarray-tqdm-pyserial.

## Installation de l'environnement Miniforge

*avec Jupyter Notebook, Python scientifique et quelques bibliothèques logicielles spécifiques. Python 3.12 et NumPy 2.x*

__Important:__ Installez Miniforge avec les paramètres recommandés par défaut, __sans__ privilèges administrateur.*

__Avertissement (notamment pour Windows):__ Si le nom de votre dossier utilisateur contient une espace et/ou un caractère "spécial", l'installation risque de ne pas aboutir. Créez un nouvel utilisateur Windows sans espace ni caractère spécial dans le nom. (Personnellement, j'avais `C:\Users\Martinus Werts\` j'ai dû créer utilisateur 'Werts' pour avoir `C:\Users\Werts\` )

Voici les [instructions, conseils et consignes](mektro_installation_scientific_python_gfm.md). (Il y a aussi une version [PDF](mektro_installation_scientific_python_gfm.pdf)).

## Quelques exemples

Nous avons ici deux exemples de notebooks Jupyter que vous pouvez télécharger et essayer avec votre Python Miniforge.

- [Example 1 - A Rankine cycle with CoolProp.ipynb](./Example%201%20-%20A%20Rankine%20cycle%20with%20CoolProp.ipynb) - Téléchargement direct: [(clic-droit)](https://raw.githubusercontent.com/mhvwerts/Python-mecatronique/master/Example%201%20-%20A%20Rankine%20cycle%20with%20CoolProp.ipynb)
- [Example 2 - Scipy special functions and PyFVTool.ipynb](./Example%202%20-%20Scipy%20special%20functions%20and%20PyFVTool.ipynb) - Téléchargement direct: [(clic-droit)](https://raw.githubusercontent.com/mhvwerts/Python-mecatronique/master/Example%202%20-%20Scipy%20special%20functions%20and%20PyFVTool.ipynb)


