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
            anyLpoints: false,
            sentPairs: [],
            url: '/corpus/request/'
        }
    },
    methods: {
        getCorpus(e) {
            e.preventDefault();
            wr = ''
            lp = ''
            if (this.searchData.wordRange[0] == -1 && this.searchData.wordRange[1] == -1) {
                wr = '&wordRange=' + -1
            }
            else {
                wr = '&wordRange=[' + this.searchData.wordRange[0] + ',' + this.searchData.wordRange[1] + "]"
            }
            if (this.searchData.Lpoints[0] == -1 && this.searchData.Lpoints[1] == -1) {
                lp = '&Lpoints=' + -1
            } else {
                lp = '&Lpoints=[' + this.searchData.Lpoints[0] + ',' + this.searchData.Lpoints[1] + "]"
            }

            urlParams = '?corpusType=' + this.searchData.corpusType +
                '&agreementType=' + this.searchData.agreementType +
                '&sentenceType=' + this.searchData.sentenceType +
                wr +
                '&nCorrections=' + this.searchData.nCorrections +
                '&sex=' + this.searchData.sex +
                '&occupation=' + this.searchData.occupation +
                '&location=' + this.searchData.location +
                lp

            axios
                .get(this.url + urlParams)
                .then(response => {

                })
                .catch(error => {
                    console.log(error)
                    this.errored = true
                })
                .finally(() => this.loading = false)
        },
        drawChart1() {
            var data = google.visualization.arrayToDataTable([
                ['Task', 'Annotated/Unannotated corpus'],
                ['Annotated', 550],
                ['Unannotated', 74572]
            ]);

            var options = {
                title: 'Annotated/Unannotated corpus'
            };

            var chart = new google.visualization.PieChart(document.getElementById('piechart1'));

            chart.draw(data, options);
        },

        drawChart2() {
            var data = google.visualization.arrayToDataTable([
                ['Task', 'Sentences with/without agreement'],
                ['With agreement', 353],
                ['Without agreement', 197]
            ]);

            var options = {
                title: 'Sentences with/without agreement'
            };

            var chart = new google.visualization.PieChart(document.getElementById('piechart2'));

            chart.draw(data, options);
        },

        drawBarChart1() {
            var data = google.visualization.arrayToDataTable([
                ['Journal distribution by occupation', 'journals'],
                ['Student', 7520],
                ['Office worker', 3393],
                ['Other', 2648],
                ['Engineer', 1733],
                ['Designer', 444],
                ['Housewife/ Househusband', 438],
                ['Artist', 332],
                ['Teacher', 319],
                ['Programmer', 282]
            ]);

            var options = {
                chart: {
                    title: 'Journal counts',
                    subtitle: 'Journal counts distribution by occupation',
                }
            };

            var chart = new google.charts.Bar(document.getElementById('barchart1'));

            chart.draw(data, google.charts.Bar.convertOptions(options));
        },

        drawRegionsMap() {
            var data = google.visualization.arrayToDataTable([
                ['Country', 'users'],
                ['Japan', 17677],
                ['China', 5354],
                ['Taiwan', 1077],
                ['Spain', 1061],
                ['Russia', 1047],
                ['Vietnam', 1047],
                ['South Korea', 1034],
                ['Brazil', 905],
                ['Belgium', 702],
                ['United States', 633],
                ['France', 386],
                ['Australia', 378],
                ['Mexico', 357],
                ['Indonesia', 279],
                ['Italy', 228],
                ['Germany', 218],
                ['Panama', 160],
                ['Hong Kong', 133],
                ['Romania', 128],
                ['United Kingdom', 116],
                ['Netherlands', 116],
                ['Thailand', 112],
                ['Colombia', 99],
                ['Hungary', 94],
                ['Ukraine', 91],
                ['Norway', 76],
                ['Jordan', 76],
                ['Chile', 67],
                ['India', 53],
                ['Afghanistan', 48],
                ['Iran', 45],
                ['Peru', 43],
                ['Canada', 41],
                ['Venezuela', 39]
            ]);

            var options = {}

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