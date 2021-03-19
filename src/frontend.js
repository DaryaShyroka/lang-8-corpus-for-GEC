var app = new Vue({
    el: "#app",
    data() {
      return {
        searchData: {
          "corpusType": -1,  //0-unannotated, 1-annotated, -1 -both (any)
          "agreementType": -1, //0 = 3 no's, 1 = 1 yes, 2 no's, 2 = 2 yeses 1 no, 3 = 3 yeses (if agreementType=-1, means any agreement type)
          "sentenceType": -1, //0-original, 1-corrected, -1 -both (any)
          "wordRange": [-1, -1], //based on 'sentenceType', sentences with word range in 10-20 inclusively (if wordRange = [-1,-1], means any word range)
          "nCorrections": -1, //sentences with n corrections (-1 means any)
          "sex": -1, //0-male, 1-female, 2-other (-1 means any)
          "occupation": -1, //(-1 means all :) )
          "location": -1, //(-1 means all :) )
          "Lpoints": [-1, -1] //Lpoints in the given range inclusively ([-1,-1] means any)
        },
        corpusType: {
          "description": 'make search from annotated/unannotated or both corpus',
          "data": {
            "Both": -1,
            "Unannotated corpus": 0,
            "Annotated corpus": 1
          }
        },
        agreementType: {
          "description": 'If corpus is annotated, then pick one of the agreement types if neccessary: 0 - all three annotators marked the correction as wrong, 1 - one annotator marked the correction as correct and 2 marked as wrong, 2 - two annotators marked as correct and 1 annotator marked as wrong, 3 - all three annotators marked as correct',
          "data": {
            "all/any": -1,
            "all 'yes'": 3,
            "all 'no'": 0,
            "1 'yes', 2 'no'": 1,
            "2 'yes', 1 'no'": 2
          }

        },
        sentenceType: {
          "description": "Apply the word range above to both/orignal/corrected sentences",
          "data": {
            "Both": -1,
            "Original": 0,
            "Corrected": 1
          }
        },
        sex: {
          "description": "Gender of the sentence authors",
          "data": {
            'all/any': -1,
            'male': 0,
            'female': 1,
            'other': 2
          }
        },
        occupation: {
          "description": "Occupation of the sentence authors",
          "data": {
            "all/any": -1,
            "Artist": 0,
            "Designer": 1,
            "Engineer": 2,
            "Housewife/ Househusband": 3,
            "Office worker": 4,
            "Programmer": 5,
            "Student": 6,
            "Teacher": 7,
            "Other": 8
          }
        },
        location: {
          "description": "Location of the sentence authors",
          "data": {
            'all/any': -1,
            'Japan': 0,
            'China': 1,
            'Taiwan': 2,
            'Vietnam': 3,
            'Russia': 4,
            'Korea': 5,
            'Brazil': 6,
            'U.S.A': 7,
            'France': 8,
            'Spain': 9
          }
        },
        anyWordRange: false,
        anyNcorrections: false,
        anyLpoints: false
      }
    },
    methods: {
      search(e) {
        e.preventDefault();
        console.log(this.searchData)
        // axios
        //   .get('http://localhost:9999/corpus?size=' + this.size)
        //   .then(response => {
        //     this.corpus = response.data
        //   })
        //   .catch(error => {
        //     console.log(error)
        //     this.errored = true
        //   })
        //   .finally(() => this.loading = false)
      },
      drawChart1() {
        var data = google.visualization.arrayToDataTable([
          ['Task', 'Annotated/Unannotated corpus'],
          ['Annotated', 7500],
          ['Unannotated', 74000]
        ]);

        var options = {
          title: 'Annotated/Unannotated corpus'
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart1'));

        chart.draw(data, options);
      },

      drawChart2() {
        var data = google.visualization.arrayToDataTable([
          ['Task', 'Correct/Incorrect sentences'],
          ['Correct sentences', 6000],
          ['Incorrect sentences', 1500]
        ]);

        var options = {
          title: 'Correct/Incorrect sentences in annotated corpus'
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart2'));

        chart.draw(data, options);
      },

      drawBarChart1() {
        // data.addRows([
        //   [{ v: [8, 0, 0, 0], f: 'Artist' }, 1, .25, 2],
        //   [{ v: [9, 0, 0, 0], f: 'Designer' }, 2, .5, 2],
        //   [{ v: [10, 0, 0, 0], f: 'Engineer' }, 3, 1, 2],
        //   [{ v: [11, 0, 0, 0], f: 'Housewife/ Househusband' }, 4, 2.25, 2],
        //   [{ v: [12, 0, 0, 0], f: 'Office worker' }, 5, 2.25, 2],
        //   [{ v: [13, 0, 0, 0], f: 'Programmer' }, 6, 3, 2],
        //   [{ v: [14, 0, 0, 0], f: 'Student' }, 7, 4, 2],
        //   [{ v: [15, 0, 0, 0], f: 'Teacher' }, 8, 5.25, 2],
        //   [{ v: [16, 0, 0, 0], f: 'Other' }, 9, 7.5, 2]
        // ]);

        var data = google.visualization.arrayToDataTable([
          ['Sentence count distribution by occupation', 'Total', 'Annotated', 'Correct'],
          ['Artist', 1000, 400, 200],
          ['Engineer', 1170, 460, 250],
          ['Housewife/ Househusband', 660, 1120, 300],
          ['Office worker', 1030, 540, 350],
          ['Programmer', 1030, 540, 350],
          ['Student', 1030, 540, 350],
          ['Teacher', 1030, 540, 350],
          ['Other', 1030, 540, 350]
        ]);

        var options = {
          chart: {
            title: 'Comparision by occupation',
            subtitle: 'Sentence count distribution by occupation',
          }
        };

        var chart = new google.charts.Bar(document.getElementById('barchart1'));

        chart.draw(data, google.charts.Bar.convertOptions(options));
      },

      drawRegionsMap() {
        var data = google.visualization.arrayToDataTable([
          ['Country', 'users'],
          ['Japan', 1000],
          ['China', 800],
          ['Taiwan', 700],
          ['Vietnam', 700],
          ['Russia', 600],
          ['Korea', 500],
          ['Brazil', 470],
          ['United States', 450],
          ['France', 400],
          ['Spain', 300]
        ]);

        var options = {};

        var chart = new google.visualization.GeoChart(document.getElementById('regions_div'));

        chart.draw(data, options);
      }
    },
    watch: {
      'searchData.corpusType': function (newVal, oldVal) {
        if (newVal == 0) {
          this.searchData.agreementType = -1
        }
      },

      anyNcorrections: function (newN, oldN) {
        if (newN == true) {
          this.searchData.nCorrections = -1
        }
      },
      anyWordRange: function (newWR, oldWR) {
        if (newWR == true) {
          this.searchData.wordRange = [-1, -1]
        }
      },
      anyLpoints: function (newLP, oldLP) {
        if (newLP == true) {
          this.searchData.Lpoints = [-1, -1]
        }
      }
    }
  })

  google.charts.load('current', {
    'packages': ['geochart', 'corechart', 'bar'],
    'mapsApiKey': 'AIzaSyD-9tSrke72PouQMnMX-a7eZSW0jkFMBWY'
  });
  google.charts.setOnLoadCallback(app.drawChart1);
  google.charts.setOnLoadCallback(app.drawChart2);
  google.charts.setOnLoadCallback(app.drawBarChart1);
  google.charts.setOnLoadCallback(app.drawRegionsMap);