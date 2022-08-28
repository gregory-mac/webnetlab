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
    });
    diagram.on('rendered', () => {
        d3.selectAll('.link textPath tspan').attr('x', '60');
        d3.selectAll('.link textPath.reverse tspan').attr('x', '-60');
    });
    diagram.init('interface');
}

$(window).on("load", function () {
    let lab_name = window.location.pathname.split("/").pop()
    $.ajax({
        url: "/graph/" + lab_name + "/topology",
        type: "GET",
        success: function(response) {
            render_graph(response);
        },
        error: function(error){
            console.log(error);
        }
    });
});