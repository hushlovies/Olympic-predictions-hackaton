
<template>
  <div class="container bg-white text-black mx-auto mt-10">
    <h1 class="text-2xl font-bold mb-4 pt-7">Prediction</h1>
    <div>
      <img src="../assets/images/modeles.png" alt="modeles" class="mx-auto" />
      <img src="../assets/images/report1.png" alt="report1" class="mx-auto my-10" />
      <img src="../assets/images/report2.png" alt="report2" class="mx-auto my-10" />
  </div>
  <div class="mx-10 text-left">
    <p class="smTitle my-5">Compte rendu</p>
    <p class="paraTitle" >Classe 0 (Gagner 0 médaille):</p>
    <ul>
      <li><strong>Précision: 0.93 </strong>: Cela signifie que 93% des prédictions de non-gagnants de médaille (classe 0) sont correctes. </li>
      <li> <strong>Rappel: 0.98 </strong>: Cela indique que 98% des athlètes qui n'ont effectivement pas gagné de médaille ont été correctement identifiés.  </li>
      <li><strong>F1-Score: 0.96 </strong>:Le F1-score, qui combine précision et rappel, est très élevé, indiquant une performance robuste pour identifier les non-gagnants de médaille.  </li>
      <li><strong>Support: 46,256</strong>: Cela représente le nombre d'athlètes dans la classe 0 dans le jeu de données.
 </li>
    </ul>
    <p class="paraTitle">Classe 1 (Gagner une médaille): </p>
    <ul>
      <li><strong>Précision: 0.86 </strong>:Cela signifie que 86% des prédictions de gagnants de médaille (classe 1) sont correctes.  </li>
      <li><strong>Rappel: 0.56 </strong>: Cela indique que seulement 56% des athlètes qui ont effectivement gagné une médaille ont été correctement identifiés, ce qui montre que le modèle manque presque la moitié des gagnants. </li>
      <li><strong>F1-Score: 0.68 </strong>:Le F1-score, plus bas que pour la classe 0, reflète le faible rappel pour les gagnants de médaille.  </li>
      <li><strong>Support: 7,968 </strong>: Cela représente le nombre d'athlètes dans la classe 1 dans le jeu de données. </li>
    </ul>
    <p class="paraTitle" >Précision Globale: 0.92</p>
    <ul>
      <li>Le modèle identifie correctement 92% des athlètes, toutes classes confondues, ce qui est une bonne performance globale. </li>
    </ul>
    <p class="paraTitle">Moyenne Macro: </p>
    <ul>
      <li><strong>Précision: 0.89 </strong> </li>
      <li><strong>Rappel: 0.77 </strong> </li>
      <li><strong>F1-Score: 0.82 </strong> </li>
      <li>Ces valeurs sont les moyennes arithmétiques des métriques de précision, rappel et F1-score pour les deux classes, offrant une vue équilibrée de la performance.  </li>
    </ul>
    <p class="paraTitle">Moyenne Pondérée:</p>
    <ul>
      <li><strong>Précision: 0.92 </strong></li>
      <li><strong>Rappel: 0.92 </strong></li>
      <li><strong>F1-Score: 0.91 </strong></li>
      <li>Ces valeurs sont pondérées par le nombre d'athlètes dans chaque classe, ce qui donne plus de poids à la performance sur la classe majoritaire (classe 0).</li>
    </ul>
    <p class="paraTitle">Interprétation et Recommandations </p>
    <ul>
      <li><strong>Classe 0 (Gagner 0 médaille)</strong>: Le modèle est très efficace pour identifier les athlètes qui n'ont pas gagné de médaille, avec une précision et un rappel élevés, et un F1-score de 0.96. </li>
      <li><strong>Classe 1 (Gagner une médaille)</strong>:La performance est moins bonne pour identifier les gagnants de médaille. Le rappel de 0.56 est particulièrement préoccupant, car il montre que presque la moitié des gagnants ne sont pas correctement identifiés par le modèle. La précision est de 0.86, ce qui est acceptable, mais le F1-score de 0.68 montre qu'il y a de la place pour des améliorations significatives.  </li>

    </ul>
    <p class="paraTitle">Recommandations : </p>
    <ul>
      <li><strong>Améliorer le Rappel pour la Classe 1</strong>: Travailler sur des techniques pour augmenter le rappel des gagnants de médaille, par exemple en ajustant le seuil de classification ou en utilisant des méthodes de rééchantillonnage comme le suréchantillonnage des gagnants de médaille. </li>
      <li><strong>Équilibrage des Classes</strong>: Le déséquilibre entre les classes (beaucoup plus d'athlètes sans médaille que d'athlètes avec médaille) semble affecter la performance. Des techniques comme le suréchantillonnage des instances de la classe minoritaire (gagnants de médaille) ou le sous-échantillonnage de la classe majoritaire (non-gagnants de médaille) pourraient être envisagées.</li>

    </ul>
    <p class="paraTitle">Analyse des Erreurs </p>
    <ul>
      <li>Une analyse approfondie des erreurs de classification pourrait révéler des motifs ou des caractéristiques spécifiques aux athlètes gagnants de médaille qui ne sont pas bien capturés par le modèle actuel. Cela pourrait inclure l'exploration de nouvelles caractéristiques ou l'ajustement des algorithmes utilisés.</li>

    </ul>
    <br>
    <p>En résumé, bien que le modèle performe bien pour prédire les athlètes qui ne gagnent pas de médaille, des efforts doivent être faits pour améliorer l'identification des gagnants de médaille afin d'obtenir une meilleure balance et une efficacité globale accrue du modèle. </p>
  </div>
  <br><br>
  </div>
 
</template>

<style>
.smTitle{
  font-weight: bold;
  font-size: 30px;
}
ul li{
 margin-left: 10px; 
}
.paraTitle{
  font-size: 20px;
  margin: 10px 0;
}
</style>