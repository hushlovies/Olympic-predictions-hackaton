<style scoped>

.inner-div {
  text-align: center;
  max-width: 900px;
}
img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.bold_title{
  margin:30px;
  color:#0081C8;
}
</style>

<template>
  <div class="container text-black bg-white mx-auto mt-10 text-center">
    <h1 class="text-2xl font-bold mb-4 pt-7">Analyse</h1>
    <div class="inner-div mx-auto">
      <p class="mt-10">
        Here are some data graphs generated using the notebook. They include the top 10 countries participating in the Olympics and the age and gender distribution of the athletes. For more details, please refer to the notebook.
      </p>
      <div class="mx-auto my-4">
        <img src="../assets/images/carte.png" alt="Carte" class="mx-auto">
      </div>
      <div class="mx-auto my-4">
        <img src="../assets/images/medal2.png"  class="mx-auto">
      </div>
      <div class="mx-auto my-4">
        <img :src="plotUrl" alt="Top 10 Countries Participated In Olympics" class="mx-auto">
      </div>
      <div class="mx-auto my-4">
        <img src="../assets/images/ageDist.png" alt="Age Distribution" class="mx-auto">
      </div>
      <div class="mx-auto my-4">
        <img src="../assets/images/season.png" alt="Season Distribution" class="mx-auto">
      </div>
      <div class="mx-auto my-4">
        <img src="../assets/images/distSex.png" alt="participation of sex in both seasons" class="mx-auto">
      </div>
      <div class="mx-auto my-4">
        <img src="../assets/images/womenPart.png" alt="women olymlpic participation" class="mx-auto">
      </div>
      <br><br>
      <div class="mx-auto my-4">
        <p>Some countries were not represented on the map. That is why we did the manual mapping. (ie. China and Russia)</p>
        <img src="../assets/images/map_clusters 1.png"  class="mx-auto">
      </div>
      <div class="mx-auto my-4">
        <img src="../assets/images/top_countries_per_million 1.png"  class="mx-auto">
      </div>
      <div class="mx-auto my-4">
        <img src="../assets/images/top_countries.png"  class="mx-auto">
      </div>
      <h1 class="text-2xl font-bold mb-4 pt-7">Compte rendu</h1>
      <div class="text-left mt-10 p-10 border">
        <div class="grid grid-cols-2 gap-4 flex justify-center ">
          <p><strong class="bold_title">Performance aux Jeux olympiques par pays</strong><br>Ces graphiques  fournissent une analyse complète des performances des pays aux Jeux Olympiques, en considérant divers aspects tels que le nombre global de médailles, le regroupement des pays en fonction des mesures de performance et les performances normalisées par population.</p>
        <p><strong class="bold_title">Préparation des données</strong><br>Nettoyage et cartographie des données :<br>Pour garantir l'exactitude de notre analyse, nous avons cartographié manuellement les noms de pays afin de corriger les divergences et d'inclure des entités historiques comme l'Union soviétique. Cette étape était cruciale pour créer un ensemble de données cohérent pour l’analyse.</p>
        </div>
        
        <br>
        <p><strong class="bold_title">Regroupement des pays par performance</strong><br>Nous avons utilisé le clustering K-Means pour regrouper les pays en fonction de leurs mesures de performance olympique. Les fonctionnalités prises en compte pour le clustering comprenaient :
            <li>Nombre total de médailles</li>
            <li>Nombre de médailles d'or, d'argent et de bronze</li>
            <li>Position dans le classement</li>
            <li>Nombre de fois que le pays a été classé parmi les 10 premiers</li>
          Résultats:<br>
          Les données groupées ont été visualisées sur une carte, montrant la répartition géographique des groupes de performances olympiques. Cette visualisation a mis en évidence les régions dotées de fortes traditions olympiques et celles qui connaissent des succès émergents.
        </p>
        <br>
          <p> 
          <strong class="bold_title">Top 20 des pays par nombre de médailles</strong><br>
          Cette visualisation permet de mettre en valeur les nations phares de l'histoire olympique, y compris celles qui n'existent plus et ne sont donc pas exposés sur la carte, comme l'Union soviétique.
        </p>
        <br>
        
        
        <p><strong class="bold_title">Performance par million d'habitants</strong><br>Pour normaliser les performances par population, nous avons calculé le nombre de médailles remportées par million d'habitants. La limite de cette analyse est qu’elle privilégie les petits pays ayant une performance par habitant élevée : Liechtenstein, Saint Marin, Bahamas. <br>La combinaison de ces analyses permet une compréhension complète des performances olympiques: <br>En corrigeant les écarts de données et en prenant en compte diverses mesures de performance, nous fournissons une vue complète du succès olympique mondial.</p>
      </div>
      
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      plotUrl: ''
    };
  },
  mounted() {
    this.fetchPlot();
  },
  methods: {
    fetchPlot() {
      fetch('http://localhost:5000/plot')
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.blob();
        })
        .then(blob => {
          const objectURL = URL.createObjectURL(blob);
          this.plotUrl = objectURL;
        })
        .catch(error => {
          console.error('Error fetching plot:', error);
        });
    }
  }
};
</script>