function render_graph(topology) {
    $('#diagram').empty();

    // https://stackoverflow.com/questions/3437786/get-the-size-of-the-screen-current-web-page-and-browser-window
    const width  = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
    const height = window.innerHeight|| document.documentElement.clientHeight|| document.body.clientHeight;

    const diagram = new Diagram('#diagram', topology, {
        width: width,
        height: height,
        distance: 250,
        ticks: 1000,
        positionCache: false,
        bundle: true,
        tooltip: 'click',
    });
    diagram.on('rendered', () => {
        d3.selectAll('.link textPath tspan').attr('x', '60');
        d3.selectAll('.link textPath.reverse tspan').attr('x', '-60');
    });
    diagram.init('interface', 'mgmt_ip', 'kind', 'image');
}

$(window).on("load", function () {
    let lab_name = window.location.pathname.split("/").pop()
    $.ajax({
        url: "/graph/" + lab_name + "/topology",
        type: "GET",
        success: function(response) {
            console.log("Got topology data");
            render_graph(response);
        },
        error: function(error){
            console.log(error);
        }
    });
});