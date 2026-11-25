my-arithmetic-nylphen
=====================

``my-arithmetic-nylphen`` est une petite bibliothèque Python d'arithmétique
réalisée dans le cadre du TP *Mise en place d'un pipeline CI/CD avec Docker,
GitHub et GitLab* (Master informatique 1, Université de La Rochelle).

Elle sert de support à un pipeline complet :

* tests unitaires et couverture de code à chaque modification
  (GitLab CI et GitHub Actions, couverture publiée sur Coveralls) ;
* versions calculées à partir des tags git (``hatch-vcs``) ;
* déploiement simulé des versions stables (tags) et non stables
  (branche ``develop``) ;
* documentation générée par Sphinx et publiée sur Read the Docs.

Installation
------------

.. code-block:: console

   $ pip install my-arithmetic-nylphen

Exemple
-------

.. code-block:: python

   >>> from my_arithmetic_nylphen import pgcd
   >>> pgcd(12, 18)
   6

.. toctree::
   :maxdepth: 2
   :caption: Sommaire

   api
