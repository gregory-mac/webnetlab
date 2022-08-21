function render_graph(topology) {
    $('#diagram').empty();

    const width  = $('#topology').width();
    const height = $('#topology').height();

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