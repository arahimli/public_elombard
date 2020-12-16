(function(window, document, $, undefined) {

})(window, document, window.jQuery);
(function(window, document, $, undefined){
    $(function(){
        var autonumeric = jQuery(".autonumber");
        if (autonumeric.length > 0) {
             /****** Spanish-numeric ******/
                new AutoNumeric('#Spanish', 'Spanish');
                /****** NorthAmerican-numeric ******/
                new AutoNumeric('#NorthAmerican', 'NorthAmerican');
                /****** British-numeric ******/
                new AutoNumeric('#British', 'British');
                /****** Swiss-numeric ******/
                new AutoNumeric('#Swiss', 'Swiss');
                /****** Japanese-numeric ******/
                new AutoNumeric('#Japanese', 'Japanese');
                /****** Chinese-numeric ******/
                new AutoNumeric('#Chinese', 'Chinese');
                /****** Brazilian-numeric ******/
                new AutoNumeric('#Brazilian', 'Brazilian');
                /****** Turkish-numeric ******/
                new AutoNumeric('#Turkish', 'Turkish');
                /****** DecimalCharCommaSeparator-numeric ******/
                new AutoNumeric('#DecimalCharCommaSeparator', 'dotDecimalCharCommaSeparator');
                /****** commaDecimalCharDotSeparator-numeric ******/
                new AutoNumeric('#commaDecimalCharDotSeparator', 'commaDecimalCharDotSeparator');
                /****** integer-numeric ******/
                new AutoNumeric('#integer', 'integer');
                /****** integerPos-numeric ******/
                new AutoNumeric('#integerPos', 'integerPos');
                /****** integerNeg-numeric ******/
                new AutoNumeric('#integerNeg', 'integerNeg');
                /****** float-numeric ******/
                new AutoNumeric('#float', 'float');
                /****** floatPos-numeric ******/
                new AutoNumeric('#floatPos', 'floatPos');
                /****** floatNeg-numeric ******/
                new AutoNumeric('#floatNeg', 'floatNeg');
                /****** numeric-numeric ******/
                new AutoNumeric('#numeric', 'numeric');
                /****** numericPos-numeric ******/
                new AutoNumeric('#numericPos', 'numericPos');
                /****** numericNeg-numeric ******/
                new AutoNumeric('#numericNeg', 'numericNeg');
                /****** euro-numeric ******/
                new AutoNumeric('#euro', 'euro');
                /****** euroPos-numeric ******/
                new AutoNumeric('#euroPos', 'euroPos');
                /****** euroNeg-numeric ******/
                new AutoNumeric('#euroNeg', 'euroNeg');
                /****** euroSpace-numeric ******/
                new AutoNumeric('#euroSpace', 'euroSpace');
                /****** euroSpacePos-numeric ******/
                new AutoNumeric('#euroSpacePos', 'euroSpacePos');
                /****** euroSpaceNeg-numeric ******/
                new AutoNumeric('#euroSpaceNeg', 'euroSpaceNeg');
                /****** dollar-numeric ******/
                new AutoNumeric('#dollar', 'dollar');
                /****** dollarPos-numeric ******/
                new AutoNumeric('#dollarPos', 'dollarPos');
                /****** dollarNeg-numeric ******/
                new AutoNumeric('#dollarNeg', 'dollarNeg');
                /****** french-numeric ******/
                new AutoNumeric('#percentageEU2dec', 'percentageEU2dec');
                /****** percentageEU2decPos-numeric ******/
                new AutoNumeric('#percentageEU2decPos', 'percentageEU2decPos');
                /****** percentageEU2decNeg-numeric ******/
                new AutoNumeric('#percentageEU2decNeg', 'percentageEU2decNeg');
                /****** percentageUS2dec-numeric ******/
                new AutoNumeric('#percentageUS2dec', 'percentageUS2dec');
                /****** percentageUS3decPos-numeric ******/
                new AutoNumeric('#percentageUS3decPos', 'percentageUS3decPos');
                /****** percentageUS3decNeg-numeric ******/
                new AutoNumeric('#percentageUS3decNeg', 'percentageUS3decNeg');
        }

    });

})(window, document, window.jQuery);
(function(window, document, $, undefined){

    $(function(){
        var customfile = jQuery(".custom-file-input");
        if (customfile.length > 0) {
                bsCustomFileInput.init();
        }
    });

})(window, document, window.jQuery);
(function(window, document, $, undefined){

    $(function(){
        var c3Chart = jQuery(".c3chart-wrapper");
        if (c3Chart.length > 0) {
                    var c3demo1 = jQuery("#c3demo1");
                    if (c3demo1.length > 0) {
                        var chart = c3.generate({
                            bindto: '#c3demo1',
                            data: {
                                columns: [
                                    ['data1', 30, 200, 100, 400, 150, 250],
                                    ['data2', 50, 20, 10, 40, 15, 25]
                                ],
                                colors: {
                                    data1: '#8E54E9',
                                    data2: '#4776E6'
                                },
                            }
                        });
                    }
                    var c3demo2 = jQuery("#c3demo2");
                    if (c3demo2.length > 0) {
                        var chart = c3.generate({
                            bindto: '#c3demo2',
                            data: {
                                columns: [
                                    ['data1', 300, 350, 300, 0, 0, 0],
                                    ['data2', 130, 100, 140, 200, 150, 50]
                                ],
                                colors: {
                                    data1: '#8E54E9',
                                    data2: '#4776E6'
                                },
                                types: {
                                    data1: 'area',
                                    data2: 'area-spline'
                                }
                            }
                        });
                    }
                    var c3demo3 = jQuery("#c3demo3");
                    if (c3demo3.length > 0) {
                        var chart = c3.generate({
                            bindto: '#c3demo3',
                            data: {
                                columns: [
                                    ['data1', 30, 200, 100, 400, 150, 250],
                                    ['data2', 130, 100, 140, 200, 150, 50],
                                    ['data3', 130, 150, 200, 300, 200, 100]
                                ],
                                colors: {
                                    data1: '#8E54E9',
                                    data2: '#4776E6',
                                    data3: '#ffbc1d'
                                },
                                type: 'bar'
                            },
                            bar: {
                                width: {
                                    ratio: 0.5 // this makes bar width 50% of length between ticks
                                }
                            }
                        });
                    }
                    var c3demo4 = jQuery("#c3demo4");
                    if (c3demo4.length > 0) {
                        var chart = c3.generate({
                            bindto: '#c3demo4',
                            data: {
                                columns: [
                                    ['data1', -30, 200, 200, 400, -150, 250],
                                    ['data2', 130, 100, -100, 200, -150, 50],
                                    ['data3', -230, 200, 200, -300, 250, 250],
                                    ['data4', 100, -50, 150, 200, -300, -100]
                                ],
                                type: 'bar',
                                colors: {
                                    data1: '#8E54E9',
                                    data2: '#4776E6',
                                    data3: '#ffbc1d',
                                    data4: '#25d09a'
                                },
                                groups: [
                                    ['data1', 'data2', 'data3', 'data4']
                                ]
                            },
                            grid: {
                                y: {
                                    lines: [{ value: 0 }]
                                }
                            }
                        });
                    }
                    var c3demo5 = jQuery("#c3demo5");
                    if (c3demo5.length > 0) {
                        var chart = c3.generate({
                            bindto: '#c3demo5',
                            data: {
                                columns: [
                                    ["setosa", 0.2, 0.2, 0.2, 0.2, 0.2, 0.4, 0.3, 0.2, 0.2, 0.1, 0.2, 0.2, 0.1, 0.1, 0.2, 0.4, 0.4, 0.3, 0.3, 0.3, 0.2, 0.4, 0.2, 0.5, 0.2, 0.2, 0.4, 0.2, 0.2, 0.2, 0.2, 0.4, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.2, 0.2, 0.3, 0.3, 0.2, 0.6, 0.4, 0.3, 0.2, 0.2, 0.2, 0.2],
                                    ["versicolor", 1.4, 1.5, 1.5, 1.3, 1.5, 1.3, 1.6, 1.0, 1.3, 1.4, 1.0, 1.5, 1.0, 1.4, 1.3, 1.4, 1.5, 1.0, 1.5, 1.1, 1.8, 1.3, 1.5, 1.2, 1.3, 1.4, 1.4, 1.7, 1.5, 1.0, 1.1, 1.0, 1.2, 1.6, 1.5, 1.6, 1.5, 1.3, 1.3, 1.3, 1.2, 1.4, 1.2, 1.0, 1.3, 1.2, 1.3, 1.3, 1.1, 1.3],
                                    ["virginica", 2.5, 1.9, 2.1, 1.8, 2.2, 2.1, 1.7, 1.8, 1.8, 2.5, 2.0, 1.9, 2.1, 2.0, 2.4, 2.3, 1.8, 2.2, 2.3, 1.5, 2.3, 2.0, 2.0, 1.8, 2.1, 1.8, 1.8, 1.8, 2.1, 1.6, 1.9, 2.0, 2.2, 1.5, 1.4, 2.3, 2.4, 1.8, 1.8, 2.1, 2.4, 2.3, 1.9, 2.3, 2.5, 2.3, 1.9, 2.0, 2.3, 1.8],
                                ],
                                colors: {
                                    setosa: '#8E54E9',
                                    versicolor: '#4776E6',
                                    virginica: '#ffbc1d'
                                },
                                type: 'pie'
                            }
                        });
                    }
                    var c3demo6 = jQuery("#c3demo6");
                    if (c3demo6.length > 0) {
                        var chart = c3.generate({
                            bindto: '#c3demo6',
                            data: {
                                columns: [
                                    ["desktop", 0.2, 0.2, 0.2, 0.2, 0.2, 0.4, 0.3, 0.2, 0.2, 0.1, 0.2, 0.2, 0.1, 0.1, 0.2, 0.4, 0.4, 0.3, 0.3, 0.3, 0.2, 0.4, 0.2, 0.5, 0.2, 0.2, 0.4, 0.2, 0.2, 0.2, 0.2, 0.4, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.2, 0.2, 0.3, 0.3, 0.2, 0.6, 0.4, 0.3, 0.2, 0.2, 0.2, 0.2],
                                    ["tablet", 1.4, 1.5, 1.5, 1.3, 1.5, 1.3, 1.6, 1.0, 1.3, 1.4, 1.0, 1.5, 1.0, 1.4, 1.3, 1.4, 1.5, 1.0, 1.5, 1.1, 1.8, 1.3, 1.5, 1.2, 1.3, 1.4, 1.4, 1.7, 1.5, 1.0, 1.1, 1.0, 1.2, 1.6, 1.5, 1.6, 1.5, 1.3, 1.3, 1.3, 1.2, 1.4, 1.2, 1.0, 1.3, 1.2, 1.3, 1.3, 1.1, 1.3],
                                    ["mobile", 2.5, 1.9, 2.1, 1.8, 2.2, 2.1, 1.7, 1.8, 1.8, 2.5, 2.0, 1.9, 2.1, 2.0, 2.4, 2.3, 1.8, 2.2, 2.3, 1.5, 2.3, 2.0, 2.0, 1.8, 2.1, 1.8, 1.8, 1.8, 2.1, 1.6, 1.9, 2.0, 2.2, 1.5, 1.4, 2.3, 2.4, 1.8, 1.8, 2.1, 2.4, 2.3, 1.9, 2.3, 2.5, 2.3, 1.9, 2.0, 2.3, 1.8],
                                ],
                                colors: {
                                    desktop: '#8E54E9',
                                    tablet: '#4776E6',
                                    mobile: '#ffbc1d'
                                },
                                type: 'donut',
                            },
                            donut: {
                                title: "Browser Statistic"
                            }
                        });
                    }
        }
    });

})(window, document, window.jQuery, document.ready);
(function(window, document, $, undefined){

    $(function(){
        var chartistChart = jQuery(".chartist-wrapper");
        if (chartistChart.length > 0) {

                //simple line chart
                var chartistdemo1 = jQuery("#chartistdemo1");
                if (chartistdemo1.length > 0) {
                    new Chartist.Line('.ct-chart-line', {
                        labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                        series: [
                            [12, 9, 7, 8, 5],
                            [2, 1, 3.5, 7, 3],
                            [1, 3, 4, 5, 6]
                        ]
                    }, {
                        fullWidth: true,
                        chartPadding: {
                            right: 30,
                            left:0
                          },
                          axisY: {
                            offset: 30
                        },
                    });

                }
                var chartistdemo2 = jQuery("#chartistdemo2");
                if (chartistdemo2.length > 0) {
                    new Chartist.Line('.ct-chart-area', {
                        labels: [1, 2, 3, 4, 5, 6, 7, 8],
                        series: [
                            [5, 9, 7, 8, 5, 3, 5, 4]
                        ]
                    }, {
                        low: 0,
                        showArea: true,
                        fullWidth: true,
                        axisY: {
                            offset: 20
                        },
                        chartPadding: {
                            right: 10,
                            left:0
                          }
                    });
                }
                var chartistdemo3 = jQuery("#chartistdemo3");
                if (chartistdemo3.length > 0) {
                    var data = {
                        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                        series: [
                            [6, 4, 8, 7, 6, 4, 8, 7, 6, 4, 8, 7],
                            [4, 3, 7, 6.5, 4, 3, 7, 6.5, 4, 3, 7, 6.5],
                            [8, 3, 1, 6, 8, 3, 1, 6, 8, 3, 1, 6]
                        ]
                    };

                    var options = {
                        seriesBarDistance: 20,
                        axisY: {
                            offset: 20,
                            scaleMinSpace: 15
                        },
                    };



                    var responsiveOptions = [
                        ['screen and (max-width: 640px)', {
                            seriesBarDistance: 0,
                            axisX: {
                                labelInterpolationFnc: function(value) {
                                    return value[0];
                                }
                            }
                        }]
                    ];

                    new Chartist.Bar('.ct-chart-bar', data, options, responsiveOptions);
                }
                var chartistdemo4 = jQuery("#chartistdemo4");
                if (chartistdemo4.length > 0) {
                    new Chartist.Bar('.ct-chart-stacked', {
                        labels: ['Q1', 'Q2', 'Q3', 'Q4'],
                        series: [
                            [800000, 1200000, 1400000, 1300000],
                            [200000, 400000, 500000, 300000],
                            [100000, 200000, 400000, 600000]
                        ]
                    }, {
                        stackBars: true,
                        axisY: {
                            labelInterpolationFnc: function(value) {
                                return (value / 1000) + 'k';
                            }
                        }
                    }).on('draw', function(data) {
                        if (data.type === 'bar') {
                            data.element.attr({
                                style: 'stroke-width: 30px'
                            });
                        }
                    });
                }
                var chartistdemo5 = jQuery("#chartistdemo5");
                if (chartistdemo5.length > 0) {
                    new Chartist.Bar('.ct-chart-horizontalbar', {
                        labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                        series: [
                            [5, 4, 3, 7, 5, 10, 3],
                            [3, 2, 9, 5, 4, 6, 4]
                        ]
                    }, {
                        seriesBarDistance: 10,
                        reverseData: true,
                        horizontalBars: true,
                        axisY: {
                            offset: 50
                        },
                        chartPadding: {
                            right: 20,
                            left:0
                          }
                    });
                }
                var chartistdemo6 = jQuery("#chartistdemo6");
                if (chartistdemo6.length > 0) {
                    var data = {
                        series: [4, 3, 4, 3, 2]
                    };

                    var sum = function(a, b) { return a + b };

                    new Chartist.Pie('.ct-chart-pie', data, {
                        labelInterpolationFnc: function(value) {
                            return Math.round(value / data.series.reduce(sum) * 100) + '%';
                        }
                    });
                }
                var chartistdemo7 = jQuery("#chartistdemo7");
                if (chartistdemo7.length > 0) {
                    new Chartist.Pie('.ct-chart-donut', {
                        series: [20, 10, 30, 40]
                    }, {
                        donut: true,
                        donutWidth: 60,
                        donutSolid: true,
                        startAngle: 270,
                        showLabel: true
                    });
                }
                var chartistdemo8 = jQuery("#chartistdemo8");
                if (chartistdemo8.length > 0) {
                    new Chartist.Pie('.ct-chart-gauge', {
                        series: [20, 10, 30, 40]
                    }, {
                        donut: true,
                        donutWidth: 60,
                        donutSolid: true,
                        startAngle: 270,
                        total: 200,
                        showLabel: true
                    });
                }
                //analytical dashboard chart
                var analytical1 = jQuery("#analytical1");
                if (analytical1.length > 0) {
                    var data = {
                        series: [
                            [6, -5, 7, -6, 4, -3]
                        ]
                    };

                    var options = {
                        high: 10,
                        low: -10,
                        seriesBarDistance: 10,
                        fullWidth: true,
                        showLabel: false,
                        chartPadding: 0,
                        axisX: {
                            showGrid: false,
                            showLabel: false,
                            offset: 0
                        },
                        axisY: {
                            showGrid: false,
                            showLabel: false,
                            offset: 0
                        }
                    };

                    new Chartist.Bar('#analytical1', data, options);
                }
                //analytical dashboard chart
                var analytical2 = jQuery("#analytical2");
                if (analytical2.length > 0) {
                    var data = {
                        series: [
                            [4, -7, 6, -3, 5, -2]
                        ]
                    };

                    var options = {
                        high: 10,
                        low: -10,
                        seriesBarDistance: 10,
                        fullWidth: true,
                        showLabel: false,
                        chartPadding: 0,
                        axisX: {
                            showGrid: false,
                            showLabel: false,
                            offset: 0
                        },
                        axisY: {
                            showGrid: false,
                            showLabel: false,
                            offset: 0
                        }
                    };

                    new Chartist.Bar('#analytical2', data, options);
                }
                //analytical dashboard chart
                var analytical3 = jQuery("#analytical3");
                if (analytical3.length > 0) {
                    var data = {
                        series: [
                            [6, -3, 5, -7, 2, -4]
                        ]
                    };

                    var options = {
                        high: 10,
                        low: -10,
                        seriesBarDistance: 10,
                        fullWidth: true,
                        showLabel: false,
                        chartPadding: 0,
                        axisX: {
                            showGrid: false,
                            showLabel: false,
                            offset: 0
                        },
                        axisY: {
                            showGrid: false,
                            showLabel: false,
                            offset: 0
                        }
                    };

                    new Chartist.Bar('#analytical3', data, options);
                }
                //analytical dashboard chart
                var analytical4 = jQuery("#analytical4");
                if (analytical4.length > 0) {
                    var data = {
                        series: [
                            [5, -3, 6, -8, 3, -5]
                        ]
                    };

                    var options = {
                        high: 10,
                        low: -10,
                        seriesBarDistance: 10,
                        fullWidth: true,
                        showLabel: false,
                        chartPadding: 0,
                        axisX: {
                            showGrid: false,
                            showLabel: false,
                            offset: 0
                        },
                        axisY: {
                            showGrid: false,
                            showLabel: false,
                            offset: 0
                        }
                    };

                    new Chartist.Bar('#analytical4', data, options);
                }
                //analytical dashboard chart
                var analytical5 = jQuery("#analytical5");
                if (analytical5.length > 0) {
                    var data = {
                        series: [
                            [3, -5, 2, -6, 7, -3]
                        ]
                    };

                    var options = {
                        high: 10,
                        low: -10,
                        seriesBarDistance: 10,
                        fullWidth: true,
                        showLabel: false,
                        chartPadding: 0,
                        axisX: {
                            showGrid: false,
                            showLabel: false,
                            offset: 0
                        },
                        axisY: {
                            showGrid: false,
                            showLabel: false,
                            offset: 0
                        }
                    };

                    new Chartist.Bar('#analytical5', data, options);
                }
                //analytical dashboard chart
                var analytical6 = jQuery("#analytical6");
                if (analytical6.length > 0) {
                    var data = {
                        series: [
                            [7, -4, 6, -3, 8, -2]
                        ]
                    };

                    var options = {
                        high: 10,
                        low: -10,
                        seriesBarDistance: 10,
                        fullWidth: true,
                        showLabel: false,
                        chartPadding: 0,
                        axisX: {
                            showGrid: false,
                            showLabel: false,
                            offset: 0
                        },
                        axisY: {
                            showGrid: false,
                            showLabel: false,
                            offset: 0
                        }
                    };

                    new Chartist.Bar('#analytical6', data, options);
                }
        }
    });

})(window, document, window.jQuery);
(function(window, document, $, undefined){

    $(function(){
        var chartJS = jQuery(".chartjs-wrapper");
        if (chartJS.length > 0) {
                    /* Utils */
                    window.chartColors = {
                        red: 'rgb(233, 84, 84)',
                        orange: 'rgb(253, 153, 68)',
                        yellow: 'rgb(255, 188, 29)',
                        green: 'rgb(37, 208, 154)',
                        blue: 'rgb(71, 118, 230)',
                        purple: 'rgb(142, 84, 233)',
                        grey: 'rgb(148, 148, 148)'
                    };

                    (function(global) {
                        var Months = [
                            'January',
                            'February',
                            'March',
                            'April',
                            'May',
                            'June',
                            'July',
                            'August',
                            'September',
                            'October',
                            'November',
                            'December'
                        ];

                        var COLORS = [
                            '#4dc9f6',
                            '#f67019',
                            '#f53794',
                            '#537bc4',
                            '#acc236',
                            '#166a8f',
                            '#00a950',
                            '#58595b',
                            '#8549ba'
                        ];

                        var Samples = global.Samples || (global.Samples = {});
                        var Color = global.Color;

                        Samples.utils = {
                            // Adapted from http://indiegamr.com/generate-repeatable-random-numbers-in-js/
                            srand: function(seed) {
                                this._seed = seed;
                            },

                            rand: function(min, max) {
                                var seed = this._seed;
                                min = min === undefined ? 0 : min;
                                max = max === undefined ? 1 : max;
                                this._seed = (seed * 9301 + 49297) % 233280;
                                return min + (this._seed / 233280) * (max - min);
                            },

                            numbers: function(config) {
                                var cfg = config || {};
                                var min = cfg.min || 0;
                                var max = cfg.max || 1;
                                var from = cfg.from || [];
                                var count = cfg.count || 8;
                                var decimals = cfg.decimals || 8;
                                var continuity = cfg.continuity || 1;
                                var dfactor = Math.pow(10, decimals) || 0;
                                var data = [];
                                var i, value;

                                for (i = 0; i < count; ++i) {
                                    value = (from[i] || 0) + this.rand(min, max);
                                    if (this.rand() <= continuity) {
                                        data.push(Math.round(dfactor * value) / dfactor);
                                    } else {
                                        data.push(null);
                                    }
                                }

                                return data;
                            },

                            labels: function(config) {
                                var cfg = config || {};
                                var min = cfg.min || 0;
                                var max = cfg.max || 100;
                                var count = cfg.count || 8;
                                var step = (max - min) / count;
                                var decimals = cfg.decimals || 8;
                                var dfactor = Math.pow(10, decimals) || 0;
                                var prefix = cfg.prefix || '';
                                var values = [];
                                var i;

                                for (i = min; i < max; i += step) {
                                    values.push(prefix + Math.round(dfactor * i) / dfactor);
                                }

                                return values;
                            },

                            months: function(config) {
                                var cfg = config || {};
                                var count = cfg.count || 12;
                                var section = cfg.section;
                                var values = [];
                                var i, value;

                                for (i = 0; i < count; ++i) {
                                    value = Months[Math.ceil(i) % 12];
                                    values.push(value.substring(0, section));
                                }

                                return values;
                            },

                            color: function(index) {
                                return COLORS[index % COLORS.length];
                            },

                            transparentize: function(color, opacity) {
                                var alpha = opacity === undefined ? 0.5 : 1 - opacity;
                                return Color(color).alpha(alpha).rgbString();
                            }
                        };

                        // DEPRECATED
                        window.randomScalingFactor = function() {
                            return Math.round(Samples.utils.rand(-100, 100));
                        };

                        // INITIALIZATION

                        Samples.utils.srand(Date.now());

                    }(this));
                    /*Custom Points*/
                    var customTooltips = function(tooltip) {
                        $(this._chart.canvas).css("cursor", "pointer");
                        var positionY = this._chart.canvas.offsetTop;
                        var positionX = this._chart.canvas.offsetLeft;
                        $(".chartjs-tooltip").css({
                            opacity: 0,
                        });
                        if (!tooltip || !tooltip.opacity) {
                            return;
                        }
                        if (tooltip.dataPoints.length > 0) {
                            tooltip.dataPoints.forEach(function(dataPoint) {
                                var content = [dataPoint.xLabel, dataPoint.yLabel].join(": ");
                                var $tooltip = $("#tooltip-" + dataPoint.datasetIndex);

                                $tooltip.html(content);
                                $tooltip.css({
                                    opacity: 1,
                                    top: positionY + dataPoint.y + "px",
                                    left: positionX + dataPoint.x + "px",
                                });
                            });
                        }
                    };
                    var color = Chart.helpers.color;
                    var lineChartData = {
                        labels: ["January", "February", "March", "April", "May", "June", "July"],
                        datasets: [{
                            label: "My First dataset",
                            backgroundColor: color(window.chartColors.purple).alpha(0.2).rgbString(),
                            borderColor: window.chartColors.purple,
                            pointBackgroundColor: window.chartColors.purple,
                            data: [
                                randomScalingFactor(),
                                randomScalingFactor(),
                                randomScalingFactor(),
                                randomScalingFactor(),
                                randomScalingFactor(),
                                randomScalingFactor(),
                                randomScalingFactor()
                            ]
                        }, {
                            label: "My Second dataset",
                            backgroundColor: color(window.chartColors.blue).alpha(0.2).rgbString(),
                            borderColor: window.chartColors.blue,
                            pointBackgroundColor: window.chartColors.blue,
                            data: [
                                randomScalingFactor(),
                                randomScalingFactor(),
                                randomScalingFactor(),
                                randomScalingFactor(),
                                randomScalingFactor(),
                                randomScalingFactor(),
                                randomScalingFactor()
                            ]
                        }]
                    };
                    //simple line chart
                    var chartjsdemo1 = jQuery("#chartjsdemo1");
                    if (chartjsdemo1.length > 0) {
                        var MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
                        var config = {
                            type: 'line',
                            data: {
                                labels: ["January", "February", "March", "April", "May", "June", "July"],
                                datasets: [{
                                    label: "Facebook",
                                    borderColor: window.chartColors.blue,
                                    backgroundColor: window.chartColors.blue,
                                    data: [
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor()
                                    ],
                                }, {
                                    label: "Twitter",
                                    borderColor: window.chartColors.green,
                                    backgroundColor: window.chartColors.green,
                                    data: [
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor()
                                    ],
                                }, {
                                    label: "LinkedIn",
                                    borderColor: window.chartColors.purple,
                                    backgroundColor: window.chartColors.purple,
                                    data: [
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor()
                                    ],
                                }, {
                                    label: "Google+",
                                    borderColor: window.chartColors.yellow,
                                    backgroundColor: window.chartColors.yellow,
                                    data: [
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor()
                                    ],
                                }]
                            },
                            options: {
                                responsive: true,
                                maintainAspectRatio: false,
                                title: {
                                    display: false,
                                    text: "Line Chart - Stacked Area"
                                },
                                tooltips: {
                                    mode: 'index',
                                },
                                hover: {
                                    mode: 'index'
                                },
                                legend: {
                                    labels: {
                                        fontColor: color(window.chartColors.grey).alpha(0.8).rgbString(),
                                        fontFamily: 'Roboto',
                                        fontSize: 12,
                                    }
                                },
                                scales: {
                                    xAxes: [{
                                        scaleLabel: {
                                            display: false,
                                            labelString: 'Month',
                                            fontColor: color(window.chartColors.grey).alpha(1).rgbString(),
                                            fontFamily: 'Roboto',
                                            fontSize: 14
                                        },
                                        ticks: {
                                            fontColor: color(window.chartColors.grey).alpha(0.8).rgbString(),
                                            fontFamily: 'Roboto',
                                            fontSize: 12,
                                            stepSize: 1,
                                            beginAtZero: true
                                        }
                                    }],
                                    yAxes: [{
                                        stacked: true,
                                        scaleLabel: {
                                            display: false,
                                            labelString: 'Price',
                                            fontColor: color(window.chartColors.grey).alpha(1).rgbString(),
                                            fontFamily: 'Roboto',
                                            fontSize: 14
                                        },
                                        ticks: {
                                            fontColor: color(window.chartColors.grey).alpha(0.8).rgbString(),
                                            fontFamily: 'Roboto',
                                            fontSize: 12
                                        }
                                    }]
                                }
                            }
                        };
                        var ctx1 = document.getElementById("chartjsdemo1").getContext("2d");
                        window.myLine1 = new Chart(ctx1, config);
                    }
                    var chartjsdemo2 = jQuery("#chartjsdemo2");
                    if (chartjsdemo2.length > 0) {
                        // Line chart
                        var config2 = {
                            type: 'line',
                            data: {
                                labels: ["January", "February", "March", "April", "May", "June", "July"],
                                datasets: [{
                                    label: "Unfilled",
                                    fill: false,
                                    backgroundColor: window.chartColors.yellow,
                                    borderColor: window.chartColors.yellow,
                                    data: [
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor()
                                    ],
                                }, {
                                    label: "Dashed",
                                    fill: false,
                                    backgroundColor: window.chartColors.blue,
                                    borderColor: window.chartColors.blue,
                                    borderDash: [5, 5],
                                    data: [
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor()
                                    ],
                                }, {
                                    label: "Filled",
                                    backgroundColor: window.chartColors.purple,
                                    borderColor: window.chartColors.purple,
                                    data: [
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor()
                                    ],
                                    fill: true,
                                }]
                            },
                            options: {
                                responsive: true,
                                maintainAspectRatio: false,
                                title: {
                                    display: false,
                                    text: 'Line Chart - Line styles'
                                },
                                tooltips: {
                                    mode: 'index',
                                    intersect: false,
                                },
                                hover: {
                                    mode: 'nearest',
                                    intersect: true
                                },
                                legend: {
                                    labels: {
                                        fontColor: color(window.chartColors.grey).alpha(0.8).rgbString(),
                                        fontFamily: 'Roboto',
                                        fontSize: 12
                                    }
                                },
                                scales: {
                                    xAxes: [{
                                        display: true,
                                        scaleLabel: {
                                            display: false,
                                            labelString: 'Month',
                                            fontColor: color(window.chartColors.grey).alpha(1).rgbString(),
                                            fontFamily: 'Roboto',
                                            fontSize: 14
                                        },
                                        ticks: {
                                            fontColor: color(window.chartColors.grey).alpha(0.8).rgbString(),
                                            fontFamily: 'Roboto',
                                            fontSize: 12,
                                            stepSize: 1,
                                            beginAtZero: true
                                        }
                                    }],
                                    yAxes: [{
                                        display: true,
                                        scaleLabel: {
                                            display: false,
                                            labelString: 'Value',
                                            fontColor: color(window.chartColors.grey).alpha(1).rgbString(),
                                            fontFamily: 'Roboto',
                                            fontSize: 14
                                        },
                                        ticks: {
                                            fontColor: color(window.chartColors.grey).alpha(0.8).rgbString(),
                                            fontFamily: 'Roboto',
                                            fontSize: 12
                                        }
                                    }]
                                }
                            }
                        };
                        var ctx2 = document.getElementById("chartjsdemo2").getContext("2d");
                        window.myLine2 = new Chart(ctx2, config2);
                    }
                    var chartjsdemo3 = jQuery("#chartjsdemo3");
                    if (chartjsdemo3.length > 0) {
                        // Donut chart
                        var config3 = {
                            type: 'doughnut',
                            data: {
                                datasets: [{
                                    data: [
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                    ],
                                    backgroundColor: [
                                        window.chartColors.red,
                                        window.chartColors.purple,
                                        window.chartColors.yellow,
                                        window.chartColors.green,
                                        window.chartColors.blue,
                                    ],
                                    label: 'Dataset 1'
                                }],
                                labels: [
                                    "Red",
                                    "Purple",
                                    "Yellow",
                                    "Green",
                                    "Blue"
                                ]
                            },
                            options: {
                                responsive: true,
                                maintainAspectRatio: false,
                                legend: {
                                    position: 'bottom',
                                    labels: {
                                        fontColor: color(window.chartColors.grey).alpha(0.8).rgbString(),
                                        fontFamily: 'Roboto',
                                        fontSize: 12
                                    }
                                },
                                title: {
                                    display: false,
                                    text: 'Doughnut Chart'
                                },
                                animation: {
                                    animateScale: true,
                                    animateRotate: true
                                }
                            }
                        };
                        var ctx3 = document.getElementById("chartjsdemo3").getContext("2d");
                        window.myLine3 = new Chart(ctx3, config3);
                    }
                    var chartjsdemo4 = jQuery("#chartjsdemo4");
                    if (chartjsdemo4.length > 0) {
                        // Combo
                        var timeFormat = 'MM/DD/YYYY HH:mm';

                        function newDateString(days) {
                            return moment().add(days, 'd').format(timeFormat);
                        }
                        var color = Chart.helpers.color;
                        var config4 = {
                            type: 'bar',
                            data: {
                                labels: [
                                    newDateString(0),
                                    newDateString(1),
                                    newDateString(2),
                                    newDateString(3),
                                    newDateString(4),
                                    newDateString(5),
                                    newDateString(6)
                                ],
                                datasets: [{
                                    type: 'bar',
                                    label: 'Dataset 1',
                                    backgroundColor: color(window.chartColors.purple).alpha(1).rgbString(),
                                    borderColor: window.chartColors.purple,
                                    data: [
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor()
                                    ],
                                }, {
                                    type: 'bar',
                                    label: 'Dataset 2',
                                    backgroundColor: color(window.chartColors.blue).alpha(1).rgbString(),
                                    borderColor: window.chartColors.blue,
                                    data: [
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor()
                                    ],
                                }, {
                                    type: 'line',
                                    label: 'Dataset 3',
                                    backgroundColor: color(window.chartColors.yellow).alpha(1).rgbString(),
                                    borderColor: window.chartColors.yellow,
                                    fill: false,
                                    data: [
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor()
                                    ],
                                }, ]
                            },
                            options: {
                                maintainAspectRatio: false,
                                responsive: true,
                                title: {
                                    display: false,
                                    text: "Combo Time Scale"
                                },
                                legend: {
                                    labels: {
                                        fontColor: color(window.chartColors.grey).alpha(0.8).rgbString(),
                                        fontFamily: 'Roboto',
                                        fontSize: 12
                                    }
                                },
                                scales: {
                                    xAxes: [{
                                        type: "time",
                                        display: true,
                                        time: {
                                            format: timeFormat
                                        },
                                        ticks: {
                                            fontColor: color(window.chartColors.grey).alpha(0.8).rgbString(),
                                            fontFamily: 'Roboto',
                                            fontSize: 12
                                        }
                                    }],
                                    yAxes: [{
                                        ticks: {
                                            fontColor: color(window.chartColors.grey).alpha(0.8).rgbString(),
                                            fontFamily: 'Roboto',
                                            fontSize: 12
                                        }
                                    }]
                                },
                            }
                        };
                        var ctx4 = document.getElementById("chartjsdemo4").getContext("2d");
                        window.myLine4 = new Chart(ctx4, config4);
                    }
                    var chartjsdemo5 = jQuery("#chartjsdemo5");
                    if (chartjsdemo5.length > 0) {
                        var chartEl = document.getElementById("chartjsdemo5");
                        var chart = new Chart(chartEl, {
                            type: "line",
                            data: lineChartData,
                            options: {
                                maintainAspectRatio: false,
                                responsive: true,
                                title: {
                                    display: false,
                                    text: "Custom Tooltips using Data Points"
                                },
                                legend: {
                                    labels: {
                                        fontColor: color(window.chartColors.grey).alpha(0.8).rgbString(),
                                        fontFamily: 'Roboto',
                                        fontSize: 12
                                    }
                                },
                                tooltips: {
                                    enabled: false,
                                    mode: 'index',
                                    intersect: false,
                                    custom: customTooltips
                                },
                                scales: {
                                    xAxes: [{
                                        ticks: {
                                            fontColor: color(window.chartColors.grey).alpha(0.8).rgbString(),
                                            fontFamily: 'Roboto',
                                            fontSize: 12
                                        }
                                    }],
                                    yAxes: [{
                                        ticks: {
                                            fontColor: color(window.chartColors.grey).alpha(0.8).rgbString(),
                                            fontFamily: 'Roboto',
                                            fontSize: 12
                                        }
                                    }]
                                },
                            }
                        });
                    }
                    var chartjsdemo6 = jQuery("#chartjsdemo6");
                    if (chartjsdemo6.length > 0) {
                        // chart basic
                        var config6 = {
                            type: 'line',
                            data: {
                                labels: ["January", "February", "March", "April", "May", "June", "July"],
                                datasets: [{
                                    label: "My First dataset",
                                    backgroundColor: window.chartColors.purple,
                                    borderColor: window.chartColors.purple,
                                    data: [
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor()
                                    ],
                                    fill: false,
                                }, {
                                    label: "My Second dataset",
                                    fill: false,
                                    backgroundColor: window.chartColors.blue,
                                    borderColor: window.chartColors.blue,
                                    data: [
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor()
                                    ],
                                }]
                            },
                            options: {
                                maintainAspectRatio: false,
                                responsive: true,
                                title: {
                                    display: false,
                                    text: 'Line Chart - Basic'
                                },
                                tooltips: {
                                    mode: 'index',
                                    intersect: false,
                                },
                                hover: {
                                    mode: 'nearest',
                                    intersect: true
                                },
                                legend: {
                                    labels: {
                                        fontColor: color(window.chartColors.grey).alpha(0.8).rgbString(),
                                        fontFamily: 'Roboto',
                                        fontSize: 12
                                    }
                                },
                                scales: {
                                    xAxes: [{
                                        display: true,
                                        scaleLabel: {
                                            display: false,
                                            labelString: 'Month',
                                            fontColor: color(window.chartColors.grey).alpha(1).rgbString(),
                                            fontFamily: 'Roboto',
                                            fontSize: 14
                                        },
                                        ticks: {
                                            fontColor: color(window.chartColors.grey).alpha(0.8).rgbString(),
                                            fontFamily: 'Roboto',
                                            fontSize: 12
                                        }
                                    }],
                                    yAxes: [{
                                        display: true,
                                        scaleLabel: {
                                            display: false,
                                            labelString: 'Value',
                                            fontColor: color(window.chartColors.grey).alpha(1).rgbString(),
                                            fontFamily: 'Roboto',
                                            fontSize: 14
                                        },
                                        ticks: {
                                            fontColor: color(window.chartColors.grey).alpha(0.8).rgbString(),
                                            fontFamily: 'Roboto',
                                            fontSize: 12
                                        }
                                    }]
                                }
                            }
                        };
                        var ctx6 = document.getElementById("chartjsdemo6").getContext("2d");
                        window.myLine6 = new Chart(ctx6, config6);
                    }
                    var chartjsdemo7 = jQuery("#chartjsdemo7");
                    if (chartjsdemo7.length > 0) {
                        var config7 = {
                            type: 'line',
                            data: {
                                labels: ["January", "February", "March", "April", "May", "June", "July"],
                                datasets: [{
                                    label: "dataset - big points",
                                    data: [
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor()
                                    ],
                                    backgroundColor: window.chartColors.purple,
                                    borderColor: window.chartColors.purple,
                                    fill: false,
                                    borderDash: [5, 5],
                                    pointRadius: 15,
                                    pointHoverRadius: 10,
                                }, {
                                    label: "dataset - individual point sizes",
                                    data: [
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor()
                                    ],
                                    backgroundColor: window.chartColors.blue,
                                    borderColor: window.chartColors.blue,
                                    fill: false,
                                    borderDash: [5, 5],
                                    pointRadius: [2, 4, 6, 18, 0, 12, 20],
                                }, {
                                    label: "dataset - large pointHoverRadius",
                                    data: [
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor()
                                    ],
                                    backgroundColor: window.chartColors.green,
                                    borderColor: window.chartColors.green,
                                    fill: false,
                                    pointHoverRadius: 30,
                                }, {
                                    label: "dataset - large pointHitRadius",
                                    data: [
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor(),
                                        randomScalingFactor()
                                    ],
                                    backgroundColor: window.chartColors.yellow,
                                    borderColor: window.chartColors.yellow,
                                    fill: false,
                                    pointHitRadius: 20,
                                }]
                            },
                            options: {
                                maintainAspectRatio: false,
                                responsive: true,
                      
                                hover: {
                                    mode: 'index'
                                },
                                legend: {
                                    position: 'bottom',
                                    labels: {
                                        fontColor: color(window.chartColors.grey).alpha(0.8).rgbString(),
                                        fontFamily: 'Roboto',
                                        fontSize: 12
                                    }
                                },
                                scales: {
                                    xAxes: [{
                                        display: true,
                                        scaleLabel: {
                                            display: false,
                                            labelString: 'Month',
                                            fontColor: color(window.chartColors.grey).alpha(1).rgbString(),
                                            fontFamily: 'Roboto',
                                            fontSize: 14
                                        },
                                        ticks: {
                                            fontColor: color(window.chartColors.grey).alpha(0.8).rgbString(),
                                            fontFamily: 'Roboto',
                                            fontSize: 12
                                        }
                                    }],
                                    yAxes: [{
                                        display: true,
                                        scaleLabel: {
                                            display: false,
                                            labelString: 'Value',
                                            fontColor: color(window.chartColors.grey).alpha(1).rgbString(),
                                            fontFamily: 'Roboto',
                                            fontSize: 14
                                        },
                                        ticks: {
                                            fontColor: color(window.chartColors.grey).alpha(0.8).rgbString(),
                                            fontFamily: 'Roboto',
                                            fontSize: 12
                                        }
                                    }]
                                },
                                title: {
                                    display: false,
                                    text: 'Line Chart - Different point sizes'
                                }
                            }
                        };
                        var ctx7 = document.getElementById("chartjsdemo7").getContext("2d");
                        window.myLine7 = new Chart(ctx7, config7);
                    }
                    var chartjsdemo8 = jQuery("#chartjsdemo8");
                    if (chartjsdemo8.length > 0) {
                        // Stacked bar chart
                        var barChartData = {
                            labels: ["January", "February", "March", "April", "May", "June", "July"],
                            datasets: [{
                                label: 'Dataset 1',
                                backgroundColor: window.chartColors.purple,
                                data: [
                                    randomScalingFactor(),
                                    randomScalingFactor(),
                                    randomScalingFactor(),
                                    randomScalingFactor(),
                                    randomScalingFactor(),
                                    randomScalingFactor(),
                                    randomScalingFactor()
                                ]
                            }, {
                                label: 'Dataset 2',
                                backgroundColor: window.chartColors.blue,
                                data: [
                                    randomScalingFactor(),
                                    randomScalingFactor(),
                                    randomScalingFactor(),
                                    randomScalingFactor(),
                                    randomScalingFactor(),
                                    randomScalingFactor(),
                                    randomScalingFactor()
                                ]
                            }, {
                                label: 'Dataset 3',
                                backgroundColor: window.chartColors.yellow,
                                data: [
                                    randomScalingFactor(),
                                    randomScalingFactor(),
                                    randomScalingFactor(),
                                    randomScalingFactor(),
                                    randomScalingFactor(),
                                    randomScalingFactor(),
                                    randomScalingFactor()
                                ]
                            }]
                        };
                        var ctx8 = document.getElementById("chartjsdemo8").getContext("2d");
                        window.myBar = new Chart(ctx8, {
                            type: 'bar',
                            data: barChartData,
                            options: {
                                maintainAspectRatio: false,
                                responsive: true,
                                title: {
                                    display: false,
                                    text: "Bar Chart - Stacked"
                                },
                                tooltips: {
                                    mode: 'index',
                                    intersect: false
                                },
                                
                                legend: {
                                    labels: {
                                        fontColor: color(window.chartColors.grey).alpha(0.8).rgbString(),
                                        fontFamily: 'Roboto',
                                        fontSize: 12
                                    }
                                },
                                scales: {
                                    xAxes: [{
                                        stacked: true,
                                        ticks: {
                                            fontColor: color(window.chartColors.grey).alpha(0.8).rgbString(),
                                            fontFamily: 'Roboto',
                                            fontSize: 12
                                        }
                                    }],
                                    yAxes: [{
                                        stacked: true,
                                        ticks: {
                                            fontColor: color(window.chartColors.grey).alpha(0.8).rgbString(),
                                            fontFamily: 'Roboto',
                                            fontSize: 12
                                        }
                                    }]
                                }
                            }
                        });
                    }
                    
        }
    });

})(window, document, window.jQuery);
(function(window, document, $, undefined){

$(function(){
    var comingsoon = $('.comingsoon')
    if (comingsoon.length > 0) {
        var second = 1000,
        minute = second * 60,
        hour = minute * 60,
        day = hour * 24;
        let countDown = new Date('dec 30, 2019 00:00:00').getTime(),
        x = setInterval(function() {
        let now = new Date().getTime(),
        distance = countDown - now;
        document.getElementById('days').innerText = Math.floor(distance / (day)),
        document.getElementById('hours').innerText = Math.floor((distance % (day)) / (hour)),
        document.getElementById('minutes').innerText = Math.floor((distance % (hour)) / (minute)),
        document.getElementById('seconds').innerText = Math.floor((distance % (minute)) / second);

    }, second)
}
});

})(window, document, window.jQuery);

(function(window, document, $, undefined){

    $(function(){
        var dataTable = jQuery(".datatable-wrapper");
        if (dataTable.length > 0) {
            $('#datatable').DataTable({
                "bLengthChange": false,
                "searching": false,
                "bPaginate":true,
                "bSortable": true,
                "pageLength": 100,
                });
        }
    });

})
(window, document, window.jQuery);
(function(window, document, $, undefined){

    $(function(){
        var dualListBox = jQuery(".duallistbox");
        if (dualListBox.length > 0) {
            $('#duallistbox').bootstrapDualListbox({
                nonSelectedListLabel: 'Non-selected',
                selectedListLabel: 'Selected',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });
        }
    });

})(window, document, window.jQuery);
(function(window, document, $, undefined){

    $(function(){
        var dualListBox = jQuery("#tableedit");
        if (dualListBox.length > 0) {
        $('#tableedit').Tabledit({
            deleteButton: false,
            saveButton: false,
            autoFocus: false,
            buttons: {
                edit: {
                    class: 'btn btn-sm btn-primary',
                    html: '<span class="fa fa-pencil"></span> &nbsp EDIT',
                    action: 'edit'
                }
            },
            columns: {
                identifier: [0, 'id'],
                editable: [[1, 'car'], [2, 'color']]
            }
        });
    }
});

})(window, document, window.jQuery);
(function(window, document, $, undefined){

    $(function(){
        var eventCalendar = jQuery(".event-calendar");
        if (eventCalendar.length > 0) {
            $('#external-events .fc-event').each(function() {

                // store data so the calendar knows to render an event upon drop
                $(this).data('event', {
                    title: $.trim($(this).text()), // use the element's text as the event title
                    stick: true, // maintain when user navigates (see docs on the renderEvent method)
                    className: $(this).data('color')
                });

                // make the event draggable using jQuery UI
                $(this).draggable({
                    zIndex: 999,
                    revert: true,      // will cause the event to go back to its
                    revertDuration: 0  //  original position after the drag
                });

            });

            $('#event-calendar').fullCalendar({
                header: {
                    left: 'prev,next today',
                    center: 'title',
                    right: 'month,agendaWeek,agendaDay'
                },
                editable: true,
                droppable: true,
                drop: function() {
                    // is the "remove after drop" checkbox checked?
                    if ($('#drop-remove').is(':checked')) {
                      // if so, remove the element from the "Draggable Events" list
                      $(this).remove();
                    }
                  },
                events: [{
                        title: 'Simple Event',
                        start: '2019-02-22',
                        end: '2019-02-25',
                        className: 'fc-event-danger'
                    },
                    {
                        title: 'Google',
                        url: 'https://www.google.com/',
                        start: '2019-02-18',
                        className: 'fc-event-success'
                    },
                    {
                        title: 'Family Vacation',
                        start: '2019-02-14',
                        end: '2019-02-18',
                        className: 'fc-event-primary'
                    }
                ]
            });
        }
    });

})(window, document, window.jQuery);
(function(window, document, $, undefined){

    $(function(){
        var eventListCalendar = jQuery(".event-list-calendar");
        if (eventListCalendar.length > 0) {
            $('#event-list-calendar').fullCalendar({
                header: {
                    left: 'prev,next today',
                    center: 'title',
                    right: 'listDay,listWeek,month'
                },
                views: {
                    listDay: { buttonText: 'list day' },
                    listWeek: { buttonText: 'list week' }
                },
                height: 650,
                defaultView: 'listWeek',
                defaultDate: '2018-09-12',
                navLinks: true, // can click day/week names to navigate views
                editable: true,
                eventLimit: true, // allow "more" link when too many events
                events: [{
                        title: 'All Day Event',
                        start: '2018-09-01'
                    },
                    {
                        title: 'Long Event',
                        start: '2018-09-07',
                        end: '2018-09-10'
                    },
                    {
                        id: 999,
                        title: 'Repeating Event',
                        start: '2018-09-09T16:00:00'
                    },
                    {
                        id: 999,
                        title: 'Repeating Event',
                        start: '2018-09-16T16:00:00'
                    },
                    {
                        title: 'Conference',
                        start: '2018-09-11',
                        end: '2018-09-13'
                    },
                    {
                        title: 'Meeting',
                        start: '2018-09-12T10:30:00',
                        end: '2018-09-12T12:30:00'
                    },
                    {
                        title: 'Lunch',
                        start: '2018-09-12T12:00:00'
                    },
                    {
                        title: 'Meeting',
                        start: '2018-09-12T14:30:00'
                    },
                    {
                        title: 'Happy Hour',
                        start: '2018-09-12T17:30:00'
                    },
                    {
                        title: 'Dinner',
                        start: '2018-09-12T20:00:00'
                    },
                    {
                        title: 'Birthday Party',
                        start: '2018-09-13T07:00:00'
                    },
                    {
                        title: 'Click for Google',
                        url: 'http://google.com/',
                        start: '2018-09-28'
                    }
                ]
            });
        }
    });

})(window, document, window.jQuery);
(function(window, document, $, undefined){

    $(function(){
        var exportTable = jQuery(".export-table-wrapper");
        if (exportTable.length > 0) {
            $("#export-table").tableExport({
                headers: true,
                footers: true,
                formats: ["xlsx", "csv", "txt"],
                bootstrap: true,
                exportButtons: true,
                position: "top"                
            });
        }
    });

})
(window, document, window.jQuery);
(function(window, document, $, undefined){

    $(function(){
        var magnific = jQuery(".magnific-wrapper");
        if (magnific.length > 0) {
                $('.view').magnificPopup({
                    type: 'image'
                    // other options
                });
                $(document).ready(function() {
                    $('.view2').magnificPopup({
                        disableOn: 700,
                        type: 'iframe',
                        mainClass: 'mfp-fade',
                        removalDelay: 160,
                        preloader: false,
                        fixedContentPos: false
                    });
                });
                $('.view1').magnificPopup({
                    type: 'image',
                    gallery: {
                        enabled: true
                    },
                });
        }
    });

})(window, document, window.jQuery);
(function(window, document, $, undefined){

    $(function(){
        var mapaelMap = jQuery(".mapaelmap-wrapper");
        if (mapaelMap.length > 0) {
                        // World Map
                        $(mapaelMap).mapael({
                            map: {
                                name: "world_countries"
                            }
                        });
        }
    });

})(window, document, window.jQuery);
(function(window, document, $, undefined){

    $(function(){
        var morrisJS = jQuery(".morris-wrapper");
        if (morrisJS.length > 0) {
                    // morris line chart
                    var morrisdemo1 = jQuery("#morrisdemo1");
                    if (morrisdemo1.length > 0) {
                        Morris.Line({
                            element: morrisdemo1,
                            data: [
                                { y: '2006', a: 40, b: 30 },
                                { y: '2007', a: 75, b: 65 },
                                { y: '2008', a: 50, b: 40 },
                                { y: '2009', a: 75, b: 65 },
                                { y: '2010', a: 50, b: 40 },
                                { y: '2011', a: 75, b: 65 },
                                { y: '2012', a: 60, b: 50 }
                            ],
                            xkey: 'y',
                            ykeys: ['a', 'b'],
                            labels: ['Series A', 'Series B'],
                            lineColors: ['#4776E6', '#8E54E9'],
                            resize: true,
                            padding: 20,
                            grid: false,
                            gridTextFamily: 'Roboto',
                            gridTextSize: 10
                        });
                    }
                    // morris line chart
                    var morrisdemo2 = jQuery("#morrisdemo2");
                    if (morrisdemo2.length > 0) {
                        Morris.Area({
                            element: morrisdemo2,
                            data: [
                                { y: '2006', a: 40, b: 30 },
                                { y: '2007', a: 75, b: 65 },
                                { y: '2008', a: 50, b: 40 },
                                { y: '2009', a: 75, b: 65 },
                                { y: '2010', a: 50, b: 40 },
                                { y: '2011', a: 75, b: 65 },
                                { y: '2012', a: 60, b: 50 }
                            ],
                            xkey: 'y',
                            ykeys: ['a', 'b'],
                            labels: ['Series A', 'Series B'],
                            lineColors: ['#4776E6', '#8E54E9'],
                            resize: true,
                            fillOpacity: 0.4,
                            padding: 20,
                            grid: false,
                            gridTextFamily: 'Roboto',
                            gridTextSize: 10
                        });
                    }
                    // morris bar chart
                    var morrisdemo3 = jQuery("#morrisdemo3");
                    if (morrisdemo3.length > 0) {
                        Morris.Bar({
                            element: morrisdemo3,
                            data: [
                                { y: '2006', a: 100, b: 90 },
                                { y: '2007', a: 75, b: 65 },
                                { y: '2008', a: 50, b: 40 },
                                { y: '2009', a: 75, b: 65 },
                                { y: '2010', a: 50, b: 40 },
                                { y: '2011', a: 75, b: 65 },
                                { y: '2012', a: 100, b: 90 }
                            ],
                            xkey: 'y',
                            ykeys: ['a', 'b'],
                            labels: ['Series A', 'Series B'],
                            barColors: ['#4776E6', '#8E54E9'],
                            resize: true,
                            fillOpacity: 0.4,
                            padding: 15,
                            grid: false,
                            gridTextFamily: 'Roboto',
                            gridTextSize: 10
                        });
                    }
                    // morris donut chart
                    var morrisdemo4 = jQuery("#morrisdemo4");
                    if (morrisdemo4.length > 0) {
                        Morris.Donut({
                            element: morrisdemo4,
                            data: [
                                { label: "Direct Visits", value: 12 },
                                { label: "Redirect Visits", value: 30 },
                                { label: "Referral Visits", value: 20 }
                            ],
                            colors: ['#45aaf2', '#e3324c', '#fbaf54']
                        });
                    }
                    // morris stacked bar chart
                    var morrisdemo5 = jQuery("#morrisdemo5");
                    if (morrisdemo5.length > 0) {
                        Morris.Bar({
                            element: morrisdemo5,
                            data: [
                                { y: '2006', a: 100, b: 90 },
                                { y: '2007', a: 75, b: 65 },
                                { y: '2008', a: 50, b: 40 },
                                { y: '2009', a: 75, b: 65 },
                                { y: '2010', a: 50, b: 40 },
                                { y: '2011', a: 75, b: 65 },
                                { y: '2012', a: 100, b: 90 }
                            ],
                            xkey: 'y',
                            ykeys: ['a', 'b'],
                            labels: ['Series A', 'Series B'],
                            barColors: ['#4776E6', '#8E54E9'],
                            resize: true,
                            fillOpacity: 0.4,
                            padding: 15,
                            grid: false,
                            gridTextFamily: 'Roboto',
                            gridTextSize: 10,
                            stacked: true
                        });
                    }
                    // morris donut chart
                    var morrisecommerce1 = jQuery("#morrisecommerce1");
                    if (morrisecommerce1.length > 0) {
                        Morris.Donut({
                            element: morrisecommerce1,
                            data: [
                                { label: "Total sales", value: 680 },
                                { label: "Open campaign", value: 800 },
                                { label: "Daily sales", value: 500 }
                            ],
                            colors: ['#45aaf2', '#8E54E9', '#eceef3']
                        });
                    }
                    
                    // morris cardealer1
                    var cardealer1 = jQuery("#cardealer1");
                    if (cardealer1.length > 0) {
                        Morris.Donut({
                            element: cardealer1,
                            data: [
                                { label: "New cars", value: 680 },
                                { label: "Used cars", value: 800 }
                            ],
                            colors: ['#f7b731', '#2bcbba']
                        });
                    }
                    
        }
    });

})(window, document, window.jQuery);
(function(window, document, $, undefined){

    $(function(){
        var nestable = jQuery(".nestable-wrapper");
        if (nestable.length > 0) {
                var updateOutput = function(e) {
                    var list = e.length ? e : $(e.target),
                        output = list.data('output');
                    if (window.JSON) {
                        output.val(window.JSON.stringify(list.nestable('serialize'))); //, null, 2));
                    } else {
                        output.val('JSON browser support required for this demo.');
                    }
                };

                // activate Nestable for list 1
                $('#nestable').nestable({
                        group: 1
                    })
                    .on('change', updateOutput);

                // activate Nestable for list 2
                $('#nestable2').nestable({
                        group: 1
                    })
                    .on('change', updateOutput);

                // output initial serialised data
                updateOutput($('#nestable').data('output', $('#nestable-output')));
                updateOutput($('#nestable2').data('output', $('#nestable2-output')));

                $('#nestable-menu').on('click', function(e) {
                    var target = $(e.target),
                        action = target.data('action');
                    if (action === 'expand-all') {
                        $('.dd').nestable('expandAll');
                    }
                    if (action === 'collapse-all') {
                        $('.dd').nestable('collapseAll');
                    }
                });
        }
    });

})(window, document, window.jQuery);
(function(window, document, $, undefined){

    $(function(){
        var owlCarousel = jQuery(".owl-wrapper");
        if (owlCarousel.length > 0) {
                var owlslider = $('.owl-carousel');
                owlslider.each(function () {
                    var $this = $(this),
                        $items = ($this.data('items')) ? $this.data('items') : 1,
                        $loop = ($this.attr('data-loop')) ? $this.data('loop') : true,
                        $navdots = ($this.data('nav-dots')) ? $this.data('nav-dots') : false,
                        $navarrow = ($this.data('nav-arrow')) ? $this.data('nav-arrow') : false,
                        $autoplay = ($this.attr('data-autoplay')) ? $this.data('autoplay') : true,
                        $autospeed = ($this.attr('data-autospeed')) ? $this.data('autospeed') : 5000,
                        $smartspeed = ($this.attr('data-smartspeed')) ? $this.data('smartspeed') : 1000,
                        $autohgt = ($this.data('autoheight')) ? $this.data('autoheight') : false,
                        $space = ($this.attr('data-space')) ? $this.data('space') : 30;
        
                        $(this).owlCarousel({
                            loop: $loop,
                            items: $items,
                            responsive: {
                              0:{items: $this.data('xx-items') ? $this.data('xx-items') : 1},
                              480:{items: $this.data('xs-items') ? $this.data('xs-items') : 1},
                              768:{items: $this.data('sm-items') ? $this.data('sm-items') : 2},
                              980:{items: $this.data('md-items') ? $this.data('md-items') : 3},
                              1200:{items: $this.data('lg-items') ? $this.data('lg-items') : 4},
                              1400:{items: $this.data('xl-items') ? $this.data('lg-items') : 5},
                            },
                            dots: $navdots,
                            autoplayTimeout:$autospeed,
                            smartSpeed: $smartspeed,
                            autoHeight:$autohgt,
                            margin:$space,
                            nav: $navarrow,
                            navText:["<i class='fa fa-angle-left fa-2x'></i>","<i class='fa fa-angle-right fa-2x'></i>"],
                            autoplay: $autoplay,
                            autoplayHoverPause: true
                        });
                   });
        }
    });

})(window, document, window.jQuery);
(function(window, document, $, undefined){

    $(function(){
        var popOvers = jQuery(".popover-wrapper");
        if (popOvers.length > 0) {
            $('[data-toggle="popover"]').popover()
        }
    });

})(window, document, window.jQuery);
(function(window, document, $, undefined){

    $(function(){
        jQuery(".loader").fadeOut('slow');
    });

})(window, document, window.jQuery);
(function(window, document, $, undefined){

    $(function(){
        var quillEditor = jQuery(".quill-editor");
        if (quillEditor.length > 0) {
                var toolbarOptions = [
                    ['bold', 'italic', 'underline', 'strike'],
                    ['blockquote', 'code-block'],

                    [{ 'header': 1 }, { 'header': 2 }],
                    [{ 'list': 'ordered' }, { 'list': 'bullet' }],
                    [{ 'script': 'sub' }, { 'script': 'super' }],
                    [{ 'indent': '-1' }, { 'indent': '+1' }],
                    [{ 'direction': 'rtl' }],
                ];
                var editor = new Quill('#editor', {
                    modules: {
                        toolbar: toolbarOptions
                    },
                    theme: 'snow'
                });
        }
    });

})(window, document, window.jQuery);
(function(window, document, $, undefined){

    $(function(){
        var rangeslider = jQuery(".rangeslider-wrapper");
        if (rangeslider.length > 0) {
                //slider-1
                $("#slider-1").ionRangeSlider();
                //slider-2
                $("#slider-2").ionRangeSlider({
                    min: 100,
                    max: 1000,
                    from: 550
                });
                //slider-3
                $("#slider-3").ionRangeSlider({
                    type: "double",
                    grid: true,
                    min: 0,
                    max: 1000,
                    from: 200,
                    to: 800,
                    prefix: "$"
                });
                //slider-4
                $("#slider-4").ionRangeSlider({
                    type: "double",
                    grid: true,
                    min: -1000,
                    max: 1000,
                    from: -500,
                    to: 500
                });
                //slider-5
                $("#slider-5").ionRangeSlider({
                    type: "double",
                    grid: true,
                    min: -1000,
                    max: 1000,
                    from: -500,
                    to: 500,
                    step: 250
                });
                //slider-6
                $("#slider-6").ionRangeSlider({
                    type: "double",
                    grid: true,
                    min: -12.8,
                    max: 12.8,
                    from: -3.2,
                    to: 3.2,
                    step: 0.1
                });
                //slider-7
                $("#slider-7").ionRangeSlider({
                    type: "double",
                    grid: true,
                    from: 1,
                    to: 5,
                    values: [0, 10, 100, 1000, 10000, 100000, 1000000]
                });
                //slider-8
                $("#slider-8").ionRangeSlider({
                    grid: true,
                    from: 5,
                    values: [
                        "zero", "one",
                        "two", "three",
                        "four", "five",
                        "six", "seven",
                        "eight", "nine",
                        "ten"
                    ]
                });
                //slider-9
                $("#slider-9").ionRangeSlider({
                    grid: true,
                    from: 3,
                    values: [
                        "January", "February", "March",
                        "April", "May", "June",
                        "July", "August", "September",
                        "October", "November", "December"
                    ]
                });
                //slider-10
                $("#slider-10").ionRangeSlider({
                    grid: true,
                    min: 1000,
                    max: 1000000,
                    from: 100000,
                    step: 1000,
                    prettify_enabled: false
                });
                //slider-11
                $("#slider-11").ionRangeSlider({
                    grid: true,
                    min: 1000,
                    max: 1000000,
                    from: 200000,
                    step: 1000,
                    prettify_enabled: true
                });
                //slider-12
                $("#slider-12").ionRangeSlider({
                    grid: true,
                    min: 1000,
                    max: 1000000,
                    from: 300000,
                    step: 1000,
                    prettify_enabled: true,
                    prettify_separator: "."
                });
                //slider-13
                $("#slider-13").ionRangeSlider({
                    grid: true,
                    min: 1000,
                    max: 1000000,
                    from: 400000,
                    step: 1000,
                    prettify_enabled: true,
                    prettify: function(num) {
                        return (Math.random() * num).toFixed(0);
                    }
                });
                //slider-14
                $("#slider-14").ionRangeSlider({
                    type: "double",
                    grid: true,
                    min: 0,
                    max: 10000,
                    from: 1000,
                    step: 9000,
                    prefix: "$"
                });
                //slider-15
                $("#slider-15").ionRangeSlider({
                    type: "single",
                    grid: true,
                    min: -90,
                    max: 90,
                    from: 0,
                    postfix: "°"
                });
                //slider-16
                $("#slider-16").ionRangeSlider({
                    grid: true,
                    min: 18,
                    max: 70,
                    from: 30,
                    prefix: "Age ",
                    max_postfix: "+"
                });
                //slider-17
                $("#slider-17").ionRangeSlider({
                    type: "double",
                    min: 100,
                    max: 200,
                    from: 145,
                    to: 155,
                    prefix: "Weight: ",
                    postfix: " million pounds",
                    decorate_both: true
                });
                //Slider-inter-1
                var $update = $(".js-update-43");
                $("#slider-inter_1").ionRangeSlider({
                    type: "single",
                    min: 0,
                    max: 100,
                    from: 50,
                    keyboard: true,
                    onStart: function(data) {
                        console.log("onStart");
                    },
                    onChange: function(data) {
                        console.log("onChange");
                    },
                    onFinish: function(data) {
                        console.log("onFinish");
                    },
                    onUpdate: function(data) {
                        console.log("onUpdate");
                    }
                });
                var slider = $("#slider-inter_1").data("ionRangeSlider");
                $update.on("click", function() {
                    slider.update({
                        from: 10
                    });
                });
        }
    });

})(window, document, window.jQuery);
(function(window, document, $, undefined){

    $(function(){
        var scrollbar = jQuery(".scrollbar");
        if (scrollbar.length > 0) {
                $('.scroll_dark').mCustomScrollbar({
                  theme:"minimal-dark",
                  setHeight: false,
                  mouseWheel: {
                    normalizeDelta: true,
                    scrollAmount: '200px',
                    contentTouchScroll: true,
                    deltaFactor: '200px'
                  },
                  advanced: {
                    autoScrollOnFocus: 'a[tabindex]'
                  }
                });
                $('.scroll_light').mCustomScrollbar({
                  theme:"minimal",
                  setHeight: false,
                  mouseWheel: {
                    normalizeDelta: true,
                    scrollAmount: '200px',
                    contentTouchScroll: true,
                    eltaFactor: '200px'
                  },
                  advanced: {
                    autoScrollOnFocus: 'a[tabindex]'
                  }
                });
        }
    });

})(window, document, window.jQuery);
(function(window, document, $, undefined){

    $(function(){
        var select = jQuery(".select-wrapper");
        if (select.length > 0) {
                    $('.js-basic-single').select2();
                    $('.js-basic-multiple').select2();
                    $(".bs-select-1").val()
                    $(".bs-input").tagsinput('items')
        }
    });

})(window, document, window.jQuery);
(function(window, document, $, undefined){

    $(function(){
        var sidebarNav = jQuery(".sidebar-nav");
        if (sidebarNav.length > 0) {
                $('#sidebarNav').metisMenu();
        }
    });

})(window, document, window.jQuery);
(function(window, document, $, undefined){

    $(function(){
        var sparkline = jQuery(".sparkline-wrapper");
        if (sparkline.length > 0) {
                function Sparkline() {
                    var sparklinedemo1 = jQuery("#sparklinedemo1");
                    if (sparklinedemo1.length > 0) {
                        $(sparklinedemo1).sparkline([20, 30, 25, 40, 40, 50, 56, 37, 50], {
                            type: 'line',
                            width: '100%',
                            height: '200',
                            lineWidth: 2,
                            spotRadius: 0,
                            chartRangeMax: 50,
                            lineColor: 'rgba(71, 118, 230, 0.5)',
                            fillColor: 'rgba(71, 118, 230, 0.3)',
                            highlightLineColor: 'rgba(0,0,0,.1)',
                            highlightSpotColor: 'rgba(0,0,0,.2)',
                        });
                        $(sparklinedemo1).sparkline([10, 35, 30, 60, 50, 45, 30, 24, 30], {
                            type: 'line',
                            width: '100%',
                            height: '200',
                            lineWidth: 2,
                            spotRadius: 0,
                            chartRangeMax: 40,
                            lineColor: 'rgba(142, 84, 233, 0.5)',
                            fillColor: 'rgba(142, 84, 233, 0.3)',
                            composite: true,
                            highlightLineColor: 'rgba(0,0,0,.1)',
                            highlightSpotColor: 'rgba(0,0,0,.2)',
                        });
                    }
                    var sparklinedemo2 = jQuery("#sparklinedemo2");
                    if (sparklinedemo2.length > 0) {
                        $(sparklinedemo2).sparkline([20, 30, 25, 40, 40, 50, 56, 37, 50], {
                            type: 'line',
                            width: '100%',
                            height: '200',
                            lineWidth: 2,
                            spotRadius: 0,
                            chartRangeMax: 50,
                            lineColor: 'rgba(71, 118, 230, 1)',
                            fillColor: 'transparent',
                            highlightLineColor: 'rgba(0,0,0,.1)',
                            highlightSpotColor: 'rgba(0,0,0,.2)'
                        });
                        $(sparklinedemo2).sparkline([10, 35, 30, 60, 50, 45, 30, 24, 30], {
                            type: 'line',
                            width: '100%',
                            height: '200',
                            lineWidth: 2,
                            spotRadius: 0,
                            chartRangeMax: 40,
                            lineColor: 'rgba(142, 84, 233, 1)',
                            fillColor: 'transparent',
                            composite: true,
                            highlightLineColor: 'rgba(0,0,0,1)',
                            highlightSpotColor: 'rgba(0,0,0,1)'
                        });
                    }
                    var sparklinedemo3 = jQuery("#sparklinedemo3");
                    if (sparklinedemo3.length > 0) {
                        $(sparklinedemo3).sparkline([5, 8, 6, 7, 3, 5, 6, 8, 2, 8, 5, 10, 11, 10, 1, 6, 5, 7, 8, 10, 8, 12, 7, 9, 5, 6, 10, 7, 8, 5, 6, 8, 5, 9, 3, 7, 1, 6, 4, 8, 4, 9, 10, 13, 7, 8, 6, 4, 11, 5, 6, 4, 7, 10, 4, 7, 4, 9], {
                            type: 'bar',
                            height: '200',
                            barWidth: '10',
                            barSpacing: '3',
                            barColor: '#4776E6'
                        });
                    }
                    
                    //chart widget end

                    var sparklinedemo4 = jQuery("#sparklinedemo4");
                    if (sparklinedemo4.length > 0) {
                        $(sparklinedemo4).sparkline([5, 8, 6, 7, 3, 5, 6, 8, 4, 8, 5, 10, 11, 10, 5, 6, 5, 7, 8, 10], {
                            type: 'line',
                            width: '100%',
                            height: '200',
                            lineColor: 'rgba(142, 84, 233, 0.5)',
                            fillColor: 'rgba(142, 84, 233, 0.3)',
                            highlightLineColor: 'rgba(0,0,0,.1)',
                            highlightSpotColor: 'rgba(0,0,0,.2)'
                        });
                        $(sparklinedemo4).sparkline([5, 8, 6, 7, 3, 5, 6, 8, 2, 8, 5, 10, 11, 10, 5, 6, 5, 7, 8, 10], {
                            type: 'bar',
                            height: '200',
                            barWidth: '10',
                            barSpacing: '5',
                            composite: true,
                            barColor: '#4776E6'
                        });
                    }
                    var sparklinedemo5 = jQuery("#sparklinedemo5");
                    if (sparklinedemo5.length > 0) {
                        $(sparklinedemo5).sparkline([40, 30, 20, 10], {
                            type: 'pie',
                            width: '200',
                            height: '165',
                            sliceColors: ['#4776E6', '#8E54E9', '#ffbc1d', '#25d09a']
                        });
                    }

                };

                Sparkline();

                var resize;
                $window.resize(function(e) {
                    clearTimeout(resize);
                    resize = setTimeout(function() {
                        Sparkline();

                    }, 300);
                });
        }
    });

})(window, document, window.jQuery);
(function(window, document, $, undefined){

    $(function(){
        var summernote = jQuery(".summernote");
        if (summernote.length > 0) {
                $('#summernote').summernote({
                    tabsize: 2,
                    height: 250
                });
        }
    });

})(window, document, window.jQuery);
(function(window, document, $, undefined){

    $(function(){
$('#sweetalert-01').click(function(e) {
    swal({
        text: 'Any fool can use a computer',
        showCloseButton: false,
        showCancelButton: true,
    })
});


$('#sweetalert-02').click(function(e) {
    swal(
        'The Internet?',
        'That thing is still around?',
        'question'
    )
});

$('#sweetalert-03').click(function(e) {
    swal({
        type: 'error',
        title: 'Oops...',
        text: 'Something went wrong!',
        footer: '<a href>Why do I have this issue?</a>',
    })
});

$('#sweetalert-04').click(function(e) {
    swal({
        imageUrl: 'assets/img/widget/06.jpg',
        imageHeight: 596,
        imageAlt: 'A tall image'
    })
});

$('#sweetalert-05').click(function(e) {
    swal({
        title: '<i>HTML</i> <u>example</u>',
        type: 'info',
        html: 'You can use <b>bold text</b>, ' +
            '<a href="//github.com">links</a> ' +
            'and other HTML tags',
        showCloseButton: true,
        showCancelButton: true,
        focusConfirm: false,
        confirmButtonText: '<i class="fa fa-thumbs-up"></i> Great!',
        confirmButtonAriaLabel: 'Thumbs up, great!',
        cancelButtonText: '<i class="fa fa-thumbs-down"></i>',
        cancelButtonAriaLabel: 'Thumbs down',
        confirmButtonClass: 'btn btn-success',
        cancelButtonClass: 'btn btn-danger'
    })
});

$('#sweetalert-06').click(function(e) {
    swal({
        position: 'top-end',
        type: 'success',
        title: 'Your work has been saved',
        showConfirmButton: false,
        timer: 1500
    })
});

$('#sweetalert-07').click(function(e) {
    swal({
        title: 'Custom animation with Animate.css',
        animation: false,
        customClass: 'animated tada'
    })
});

$('#sweetalert-08').click(function(e) {
    swal({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        type: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, delete it!',
        confirmButtonClass: 'btn btn-success',
        cancelButtonClass: 'btn btn-danger',
    }).then((result) => {
        if (result.value) {
            swal(
                'Deleted!',
                'Your file has been deleted.',
                'success'
            )
        }
    })
});

$('#sweetalert-09').click(function(e) {
    swal({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        type: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, delete it!',
        cancelButtonText: 'No, cancel!',
        confirmButtonClass: 'btn btn-success',
        cancelButtonClass: 'btn btn-danger',
        buttonsStyling: true,
        reverseButtons: true
    }).then((result) => {
        if (result.value) {
            swal(
                'Deleted!',
                'Your file has been deleted.',
                'success'
            )
        } else if (
            // Read more about handling dismissals
            result.dismiss === swal.DismissReason.cancel
        ) {
            swal(
                'Cancelled',
                'Your imaginary file is safe :)',
                'error'
            )
        }
    })
});

$('#sweetalert-10').click(function(e) {
    swal({
        title: 'Sweet!',
        text: 'Modal with a custom image.',
        imageUrl: 'https://unsplash.it/400/200',
        imageWidth: 400,
        imageHeight: 200,
        imageAlt: 'Custom image',
        animation: false
    })
});

$('#sweetalert-11').click(function(e) {
    swal({
        title: 'Custom width, padding, background.',
        width: 600,
        padding: 100,
    })
});

$('#sweetalert-12').click(function(e) {
    swal({
        title: 'Auto close alert!',
        text: 'I will close in 5 seconds.',
        timer: 5000,
        onOpen: () => {
            swal.showLoading()
        }
    }).then((result) => {
        if (
            // Read more about handling dismissals
            result.dismiss === swal.DismissReason.timer
        ) {
            console.log('I was closed by the timer')
        }
    })
});


$('#sweetalert-13').click(function(e) {
    swal({
        title: 'Ù‡Ù„ ØªØ±ÙŠØ¯ Ø§Ù„Ø§Ø³ØªÙ…Ø±Ø§Ø±ØŸ',
        confirmButtonText: 'Ù†Ø¹Ù…',
        cancelButtonText: 'Ù„Ø§',
        showCancelButton: true,
        showCloseButton: true,
        confirmButtonClass: 'btn btn-success',
        cancelButtonClass: 'btn btn-danger',
        target: document.getElementById('rtl-container')
    })
});

$('#sweetalert-14').click(function(e) {
    swal({
        title: 'Submit email to run ajax request',
        input: 'email',
        showCancelButton: true,
        confirmButtonText: 'Submit',
        showLoaderOnConfirm: true,
        preConfirm: (email) => {
            return new Promise((resolve) => {
                setTimeout(() => {
                    if (email === 'taken@example.com') {
                        swal.showValidationError(
                            'This email is already taken.'
                        )
                    }
                    resolve()
                }, 2000)
            })
        },
        allowOutsideClick: () => !swal.isLoading()
    }).then((result) => {
        if (result.value) {
            swal({
                type: 'success',
                title: 'Ajax request finished!',
                html: 'Submitted email: ' + result.value
            })
        }
    })
});

$('#sweetalert-15').click(function(e) {
    swal.setDefaults({
        input: 'text',
        confirmButtonText: 'Next &rarr;',
        showCancelButton: true,
        confirmButtonClass: 'btn btn-success',
        cancelButtonClass: 'btn btn-danger',
        progressSteps: ['1', '2', '3']
    })

    var steps = [{
            title: 'Question 1',
            text: 'Chaining swal2 modals is easy'
        },
        'Question 2',
        'Question 3'
    ]

    swal.queue(steps).then((result) => {
        swal.resetDefaults()

        if (result.value) {
            swal({
                title: 'All done!',
                html: 'Your answers: <pre>' +
                    JSON.stringify(result.value) +
                    '</pre>',
                confirmButtonText: 'Lovely!'
            })
        }
    })
});

$('#sweetalert-16').click(function(e) {
    const ipAPI = 'https://api.ipify.org?format=json'
    swal.queue([{
        title: 'Your public IP',
        confirmButtonText: 'Show my public IP',
        text: 'Your public IP will be received ' +
            'via AJAX request',
        showLoaderOnConfirm: true,
        preConfirm: () => {
            return fetch(ipAPI)
                .then(response => response.json())
                .then(data => swal.insertQueueStep(data.ip))
                .catch(() => {
                    swal.insertQueueStep({
                        type: 'error',
                        title: 'Unable to get your public IP'
                    })
                })
        }
    }])
});

});

})(window, document, window.jQuery);
(function(window, document, $, undefined){

    $(function(){
        $("#checkAll").click(function () {
            $('input:checkbox').not(this).prop('checked', this.checked);
        });
});

})(window, document, window.jQuery);
(function(window, document, $, undefined){

    $(function(){
$(function () {
    var i = -1;
    var toastCount = 0;
    var $toastlast;

    var getMessage = function () {
        var msgs = ['My name is Inigo Montoya. You killed my father. Prepare to die!',
            '<div><input class="input-small" value="textbox"/>&nbsp;<a href="http://johnpapa.net" target="_blank">This is a hyperlink</a></div><div><button type="button" id="okBtn" class="btn btn-primary">Close me</button><button type="button" id="surpriseBtn" class="btn" style="margin: 0 8px 0 8px">Surprise me</button></div>',
            'Are you the six fingered man?',
            'Inconceivable!',
            'I do not think that means what you think it means.',
            'Have fun storming the castle!'
        ];
        i++;
        if (i === msgs.length) {
            i = 0;
        }

        return msgs[i];
    };

    var getMessageWithClearButton = function (msg) {
        msg = msg ? msg : 'Clear itself?';
        msg += '<br /><br /><button type="button" class="btn clear">Yes</button>';
        return msg;
    };

    $('#closeButton').on("click", function () {
        if($(this).is(':checked')) {
            $('#addBehaviorOnToastCloseClick').prop('disabled', false);
        } else {
            $('#addBehaviorOnToastCloseClick').prop('disabled', true);
            $('#addBehaviorOnToastCloseClick').prop('checked', false);
        }
    });

    $('#showtoast').on("click", function () {
        var shortCutFunction = $("#toastTypeGroup input:radio:checked").val();
        var msg = $('#message').val();
        var title = $('#title').val() || '';
        var $showDuration = $('#showDuration');
        var $hideDuration = $('#hideDuration');
        var $timeOut = $('#timeOut');
        var $extendedTimeOut = $('#extendedTimeOut');
        var $showEasing = $('#showEasing');
        var $hideEasing = $('#hideEasing');
        var $showMethod = $('#showMethod');
        var $hideMethod = $('#hideMethod');
        var toastIndex = toastCount++;
        var addClear = $('#addClear').prop('checked');

        toastr.options = {
            closeButton: $('#closeButton').prop('checked'),
            debug: $('#debugInfo').prop('checked'),
            newestOnTop: $('#newestOnTop').prop('checked'),
            progressBar: $('#progressBar').prop('checked'),
            rtl: $('#rtl').prop('checked'),
            positionClass: $('#positionGroup input:radio:checked').val() || 'toast-top-right',
            preventDuplicates: $('#preventDuplicates').prop('checked'),
            onclick: null
        };

        if ($('#addBehaviorOnToastClick').prop('checked')) {
            toastr.options.onclick = function () {
                alert('You can perform some custom action after a toast goes away');
            };
        }

        if ($('#addBehaviorOnToastCloseClick').prop('checked')) {
            toastr.options.onCloseClick = function () {
                alert('You can perform some custom action when the close button is clicked');
            };
        }

        if ($showDuration.val().length) {
            toastr.options.showDuration = parseInt($showDuration.val());
        }

        if ($hideDuration.val().length) {
            toastr.options.hideDuration = parseInt($hideDuration.val());
        }

        if ($timeOut.val().length) {
            toastr.options.timeOut = addClear ? 0 : parseInt($timeOut.val());
        }

        if ($extendedTimeOut.val().length) {
            toastr.options.extendedTimeOut = addClear ? 0 : parseInt($extendedTimeOut.val());
        }

        if ($showEasing.val().length) {
            toastr.options.showEasing = $showEasing.val();
        }

        if ($hideEasing.val().length) {
            toastr.options.hideEasing = $hideEasing.val();
        }

        if ($showMethod.val().length) {
            toastr.options.showMethod = $showMethod.val();
        }

        if ($hideMethod.val().length) {
            toastr.options.hideMethod = $hideMethod.val();
        }

        if (addClear) {
            msg = getMessageWithClearButton(msg);
            toastr.options.tapToDismiss = false;
        }
        if (!msg) {
            msg = getMessage();
        }

        $('#toastrOptions').text('Command: toastr["'
                + shortCutFunction
                + '"]("'
                + msg
                + (title ? '", "' + title : '')
                + '")\n\ntoastr.options = '
                + JSON.stringify(toastr.options, null, 2)
        );

        var $toast = toastr[shortCutFunction](msg, title); // Wire up an event handler to a button in the toast, if it exists
        $toastlast = $toast;

        if(typeof $toast === 'undefined'){
            return;
        }

        if ($toast.find('#okBtn').length) {
            $toast.delegate('#okBtn', 'click', function () {
                alert('you clicked me. i was toast #' + toastIndex + '. goodbye!');
                $toast.remove();
            });
        }
        if ($toast.find('#surpriseBtn').length) {
            $toast.delegate('#surpriseBtn', 'click', function () {
                alert('Surprise! you clicked me. i was toast #' + toastIndex + '. You could perform an action here.');
            });
        }
        if ($toast.find('.clear').length) {
            $toast.delegate('.clear', 'click', function () {
                toastr.clear($toast, { force: true });
            });
        }
    });

    function getLastToast(){
        return $toastlast;
    }
    $('#clearlasttoast').on("click", function () {
        toastr.clear(getLastToast());
    });
    $('#cleartoasts').on("click", function () {
        toastr.clear();
    });
})

});

})(window, document, window.jQuery);
(function(window, document, $, undefined){

    $(function(){
        var tootlTips = jQuery(".tooltip-wrapper");
        if (tootlTips.length > 0) {
            $('[data-toggle="tooltip"]').tooltip();
        }
    });

})(window, document, window.jQuery);
(function(window, document, $, undefined){

    $(function(){
$.validator.setDefaults({
    submitHandler: function() {
        alert("submitted!");
    }
});

$(document).ready(function() {
    $("#signupForm").validate({
        rules: {
            fname: "required",
            lname: "required",
            uname: {
                required: true,
                minlength: 2
            },
            upassword: {
                required: true,
                minlength: 5
            },
            uconfirm_password: {
                required: true,
                minlength: 5,
                equalTo: "#password"
            },
            uemail: {
                required: true,
                email: true
            },
            uagree: "required"
        },
        messages: {
            fname: "Please enter your firstname",
            lname: "Please enter your lastname",
            uname: {
                required: "Please enter a username",
                minlength: "Your username must consist of at least 2 characters"
            },
            upassword: {
                required: "Please provide a password",
                minlength: "Your password must be at least 5 characters long"
            },
            uconfirm_password: {
                required: "Please provide a password",
                minlength: "Your password must be at least 5 characters long",
                equalTo: "Please enter the same password as above"
            },
            uemail: "Please enter a valid email address",
            uagree: "Please accept our policy"
        },
        errorElement: "em",
        errorPlacement: function(error, element) {
            // Add the `help-block` class to the error element
            error.addClass("help-block");

            if (element.prop("type") === "checkbox") {
                error.insertAfter(element.parent("label"));
            } else {
                error.insertAfter(element);
            }
        },
        highlight: function(element, errorClass, validClass) {
            $(element).parents(".col-sm-5").addClass("has-error").removeClass("has-success");
        },
        unhighlight: function(element, errorClass, validClass) {
            $(element).parents(".col-sm-5").addClass("has-success").removeClass("has-error");
        }
    });

    $("#signupForm1").validate({
        rules: {
            firstname1: "required",
            lastname1: "required",
            username1: {
                required: true,
                minlength: 2
            },
            password1: {
                required: true,
                minlength: 5
            },
            confirm_password1: {
                required: true,
                minlength: 5,
                equalTo: "#password1"
            },
            email1: {
                required: true,
                email: true
            },
            agree1: "required"
        },
        messages: {
            firstname1: "Please enter your firstname",
            lastname1: "Please enter your lastname",
            username1: {
                required: "Please enter a username",
                minlength: "Your username must consist of at least 2 characters"
            },
            password1: {
                required: "Please provide a password",
                minlength: "Your password must be at least 5 characters long"
            },
            confirm_password1: {
                required: "Please provide a password",
                minlength: "Your password must be at least 5 characters long",
                equalTo: "Please enter the same password as above"
            },
            email1: "Please enter a valid email address",
            agree1: "Please accept our policy"
        },
        errorElement: "em",
        errorPlacement: function(error, element) {
            // Add the `help-block` class to the error element
            error.addClass("help-block");

            // Add `has-feedback` class to the parent div.form-group
            // in order to add icons to inputs
            element.parents(".col-sm-5").addClass("has-feedback");

            if (element.prop("type") === "checkbox") {
                error.insertAfter(element.parent("label"));
            } else {
                error.insertAfter(element);
            }

            // Add the span element, if doesn't exists, and apply the icon classes to it.
            if (!element.next("span")[0]) {
                $("<span class='fa fa-times form-control-feedback pr-2'></span>").insertAfter(element);
            }
        },
       
        highlight: function(element, errorClass, validClass) {
            $(element).parents(".col-sm-5").addClass("has-error").removeClass("has-success");
            $(element).next("span").addClass("fa fa-times").removeClass("fa fa-check");
        },
        unhighlight: function(element, errorClass, validClass) {
            $(element).parents(".col-sm-5").addClass("has-success").removeClass("has-error");
            ($(element)).next("span").addClass("fa fa-check").removeClass("fa fa-times");
        }
    });

    $("#signupForm3").validate({
        rules: {
            firstname: "required",
            lastname: "required",
            username: {
                required: true,
                minlength: 2
            },
            password: {
                required: true,
                minlength: 5
            },
            confirm_password: {
                required: true,
                minlength: 5,
                equalTo: "#password"
            },
            email: {
                required: true,
                email: true
            },
            agree: "required"
        },
        messages: {
            firstname: "Please enter your firstname",
            lastname: "Please enter your lastname",
            username: {
                required: "Please enter a username",
                minlength: "Your username must consist of at least 2 characters"
            },
            password: {
                required: "Please provide a password",
                minlength: "Your password must be at least 5 characters long"
            },
            confirm_password: {
                required: "Please provide a password",
                minlength: "Your password must be at least 5 characters long",
                equalTo: "Please enter the same password as above"
            },
            email: "Please enter a valid email address",
            agree: "Please accept our policy"
        },
        errorPlacement: function(error, element) {
            error.addClass("ui red pointing label transition");
            error.insertAfter(element.parent());
        },
        highlight: function(element, errorClass, validClass) {
            $(element).parents(".row").addClass(errorClass);
        },
        unhighlight: function(element, errorClass, validClass) {
            $(element).parents(".row").removeClass(errorClass);
        }
    });

});

});

})(window, document, window.jQuery);
(function(window, document, $, undefined){

    $(function(){
        window.addEventListener('load', function() {
            // Fetch all the forms we want to apply custom Bootstrap validation styles to
            var forms = document.getElementsByClassName('needs-validation');
            // Loop over them and prevent submission
            var validation = Array.prototype.filter.call(forms, function(form) {
              form.addEventListener('submit', function(event) {
                if (form.checkValidity() === false) {
                  event.preventDefault();
                  event.stopPropagation();
                }
                form.classList.add('was-validated');
              }, false);
            });
          }, false);

          getSelectorFromElement: function getSelectorFromElement(element) {
            var selector = element.getAttribute('data-target');
        
            if (!selector || selector === '#') {
              selector = element.getAttribute('href') || '';
            }
        
            try {
              return document.querySelector(selector) ? selector : null;
            } catch (err) {
              return null;
            }
        }
   
    $('.mobile-toggle').on('click', function() {
        $('body').toggleClass('sidebar-toggled');
      });

      $(document).on('click', '.mega-menu.dropdown-menu', function (e) {
        e.stopPropagation();
      });

      $('.sidebar-toggle').on('click', function() {
        $('body').toggleClass('sidebar-mini');
        $('.app-navbar').toggleClass('expand');
      });

      $('.app-navbar').hover(function() {
        if($('body').hasClass('sidebar-mini')) {
          $('.navbar-header').toggleClass('expand');
        }
      });

      $('.search').on('click', function() {
        $('.search-wrapper').fadeIn(200);
      });

       //Search Box Close 
       $('.close-btn').on('click', function() {
        $('.search-wrapper').fadeOut(200);
      });
    });
})(window, document, window.jQuery);