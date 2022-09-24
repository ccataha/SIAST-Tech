$(function () {
    initCounters();
    initCharts();
});

//Widgets count plugin
function initCounters() {
    $('.count-to').countTo();
}
// #C252E1 Medium orchid #E0D9F6 Lavender white #586AE2 Royal Blue #6ECBF5 Light Sky Blue #2A2356 Midnight Blue
//Charts
function initCharts() {
    //Chart Bar
    $('.chart.chart-bar').sparkline(undefined, {
        type: 'bar',
        barColor: '#7868da',
        negBarColor: '#fb4364',
        barWidth: '4px',
        height: '45px'
    });

    //Chart Pie
    $('.chart.chart-pie').sparkline(undefined, {
        type: 'pie',
        height: '50px',
        sliceColors: ['#fb4364', '#3aaaec', '#7868da', '#313037']
    });
    
    var COLORS = { 
        Orchid: "#c252e1",  
        Lavenderwhite: "#e0d9f6",  
        RoyalBlue: "#586ae2", 
        SkyBlue: "#6ecbf5", 
        MidnightBlue: "#2a2356" 
    };
    
    //Chart Line
    $('.chart.chart-line').sparkline(undefined, {
        type: 'line',
        width: '60px',
        height: '45px',
        lineColor: '#3aaaec',
        lineWidth: 1.3,
        fillColor: 'rgba(0,0,0,0)',
        spotColor: 'rgba(255,255,255,0.40)',
        maxSpotColor: 'rgba(255,255,255,0.40)',
        minSpotColor: 'rgba(255,255,255,0.40)',
        spotRadius: 3,
        highlightSpotColor: '#3aaaec'
    });

    $('#linecustom1').sparkline('html',{
        height: '55px',
        width: '100%',
        lineColor: COLORS.Orchid,
        fillColor: COLORS.Orchid,
        minSpotColor: true,
        maxSpotColor: true,
        spotColor: COLORS.Orchid,
        spotRadius: 0
    });

    $('#linecustom2').sparkline('html',{
        height: '55px',
        width: '100%',
        lineColor: COLORS.RoyalBlue,
        fillColor: COLORS.RoyalBlue,
        minSpotColor: true,
        maxSpotColor: true,
        spotColor: COLORS.RoyalBlue,
        spotRadius: 0
    });

    $('#linecustom3').sparkline('html',{	
        height: '55px',
        width: '100%',
        lineColor: COLORS.SkyBlue,
        fillColor: COLORS.SkyBlue,
        minSpotColor: true,
        maxSpotColor: true,
        spotColor: COLORS.SkyBlue,
        spotRadius: 0
    });

    $('#linecustom4').sparkline('html',{
        height: '55px',
        width: '100%',
        lineColor: COLORS.MidnightBlue,
        fillColor: COLORS.MidnightBlue,
        minSpotColor: true,
        maxSpotColor: true,
        spotColor: COLORS.MidnightBlue,
        spotRadius: 0
    });

    $('#linecustom5').sparkline('html',{
        height: '55px',
        width: '100%',
        lineColor: COLORS.Orchid,
        fillColor: COLORS.Orchid,
        minSpotColor: true,
        maxSpotColor: true,
        spotColor: COLORS.Orchid,
        spotRadius: 0
    });

    $('#linecustom6').sparkline('html',{	
        height: '55px',
        width: '100%',
        lineColor: COLORS.RoyalBlue,
        fillColor: COLORS.RoyalBlue,
        minSpotColor: true,
        maxSpotColor: true,
        spotColor: COLORS.RoyalBlue,
        spotRadius: 0
    });

    $('#linecustom7').sparkline('html',{
        height: '55px',
        width: '100%',
        lineColor: COLORS.SkyBlue,
        fillColor: COLORS.SkyBlue,
        minSpotColor: true,
        maxSpotColor: true,
        spotColor: COLORS.SkyBlue,
        spotRadius: 0
    });

    $('#linecustom8').sparkline('html',{
        height: '55px',
        width: '100%',
        lineColor: COLORS.MidnightBlue,
        fillColor: COLORS.MidnightBlue,
        minSpotColor: true,
        maxSpotColor: true,
        spotColor: COLORS.MidnightBlue,
        spotRadius: 0
    });

    $('#linecustom9').sparkline('html',{	
        height: '55px',
        width: '100%',
        lineColor: COLORS.Orchid,
        fillColor: COLORS.Orchid,
        minSpotColor: true,
        maxSpotColor: true,
        spotColor: COLORS.Orchid,
        spotRadius: 0
    });

    $('#linecustom10').sparkline('html',{
        height: '55px',
        width: '100%',
        lineColor: COLORS.RoyalBlue,
        fillColor: COLORS.RoyalBlue,
        minSpotColor: true,
        maxSpotColor: true,
        spotColor: COLORS.RoyalBlue,
        spotRadius: 0
    });
    $('#linecustom11').sparkline('html',{
        height: '55px',
        width: '100%',
        lineColor: COLORS.SkyBlue,
        fillColor: COLORS.SkyBlue,
        minSpotColor: true,
        maxSpotColor: true,
        spotColor: COLORS.SkyBlue,
        spotRadius: 0
    });
    $('#linecustom12').sparkline('html',{
        height: '55px',
        width: '100%',
        lineColor: COLORS.MidnightBlue,
        fillColor: COLORS.MidnightBlue,
        minSpotColor: true,
        maxSpotColor: true,
        spotColor: COLORS.MidnightBlue,
        spotRadius: 0
    });
    $('#linecustom13').sparkline('html',{
        height: '55px',
        width: '100%',
        lineColor: COLORS.Orchid,
        fillColor: COLORS.Orchid,
        minSpotColor: true,
        maxSpotColor: true,
        spotColor: COLORS.Orchid,
        spotRadius: 0
    });
    $('#linecustom14').sparkline('html',{
        height: '55px',
        width: '100%',
        lineColor: COLORS.RoyalBlue,
        fillColor: COLORS.RoyalBlue,
        minSpotColor: true,
        maxSpotColor: true,
        spotColor: COLORS.RoyalBlue,
        spotRadius: 0
    });
    $('#linecustom15').sparkline('html',{
        height: '55px',
        width: '100%',
        lineColor: COLORS.SkyBlue,
        fillColor: COLORS.SkyBlue,
        minSpotColor: true,
        maxSpotColor: true,
        spotColor: COLORS.SkyBlue,
        spotRadius: 0
    });
    $('#linecustom16').sparkline('html',{
        height: '55px',
        width: '100%',
        lineColor: COLORS.MidnightBlue,
        fillColor: COLORS.MidnightBlue,
        minSpotColor: true,
        maxSpotColor: true,
        spotColor: COLORS.MidnightBlue,
        spotRadius: 0
    });
    $('#linecustom17').sparkline('html',{
        height: '55px',
        width: '100%',
        lineColor: COLORS.Orchid,
        fillColor: COLORS.Orchid,
        minSpotColor: true,
        maxSpotColor: true,
        spotColor: COLORS.Orchid,
        spotRadius: 0
    });
    $('#linecustom18').sparkline('html',{
        height: '55px',
        width: '100%',
        lineColor: COLORS.RoyalBlue,
        fillColor: COLORS.RoyalBlue,
        minSpotColor: true,
        maxSpotColor: true,
        spotColor: COLORS.RoyalBlue,
        spotRadius: 0
    });
    $('#linecustom19').sparkline('html',{
        height: '55px',
        width: '100%',
        lineColor: COLORS.SkyBlue,
        fillColor: COLORS.SkyBlue,
        minSpotColor: true,
        maxSpotColor: true,
        spotColor: COLORS.SkyBlue,
        spotRadius: 0
    });
}