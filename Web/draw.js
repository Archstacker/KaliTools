var width = 6000,
    height = 6000,
    img_w = 20,
    img_h = 20,
    r = 6,
    fill = d3.scale.category20();

var tip = d3.tip()
    .attr('class', 'd3-tip')
    .html(function(d) { return d.description })
    .direction('n')
    .offset([0, 3])

var force = d3.layout.force()
    .charge(-2000)
    .linkDistance(1)
    .size([width, height*1.15]);

var svg = d3.select("body").append("svg:svg")
    .attr("width", width)
    .attr("height", height)
    .call(tip);

d3.json("graph.json", function(json) {
    var link = svg.selectAll("line")
        .data(json.links)
        .enter().
        append("svg:line");

    var node = svg.selectAll("image")
        .data(json.nodes)
        .enter().append("image")
        .attr("width", function(d) {return d.power*img_w })
        .attr("height", function(d) {return d.power*img_h; })
        .attr("xlink:href", function(d) { return 'icons/'+d.icon; })
        .attr("text", function(d) { return d.name; })
        .on('mouseover', tip.show)
        .on('mouseout', tip.hide)
        .call(force.drag);

    force
        .nodes(json.nodes)
        .links(json.links)
        .on("tick", tick)
        .start();

    var nodetext = svg.selectAll('.nodetext')
        .data(json.nodes)
        .enter()
        .append("text")
        .attr("class","nodetext")
        .attr("dx",-20)
        .attr("dy",20)
        .text(function(d){
            return d.name;
        });

    function tick(e) {
        // Push sources up and targets down to form a weak tree.
        var k = 6 * e.alpha;
        json.links.forEach(function(d, i) {
          d.source.y -= k;
          d.target.y += k;
        });
        node.attr("x", function(d) { return d.x-img_w*d.power/2; })
            .attr("y", function(d) { return d.y-img_h*d.power/2; });

        link.attr("x1", function(d) { return d.source.x; })
            .attr("y1", function(d) { return d.source.y; })
            .attr("x2", function(d) { return d.target.x; })
            .attr("y2", function(d) { return d.target.y; });

        nodetext.attr("x",function(d){ return d.x-img_w*d.power/4 });
        nodetext.attr("y",function(d){ return d.y + img_w*d.power/2 });
    }
});

