
        var forcestrength = -12;
        var radius = d3.scaleSqrt()
            .range([0, 6]);

        var svg = d3.select("#dataviz_spec_kwgraph_svg"),
            width = +svg.attr("width"),
            height = +svg.attr("height");
            width = window.innerWidth < 960 ? window.innerWidth - 200 : 920
            height = 400


        var color = d3.scaleOrdinal(d3.schemeCategory20);


        //https://stackoverflow.com/questions/46977022/how-to-adjust-size-of-force-directed-graph-in-d3-js
        var simulation = d3.forceSimulation()
        .force("link", d3.forceLink().id(function(d) { return d.id; }))
        .force("charge", d3.forceManyBody())
        //.force("charge", d3.forceManyBody().strength(forcestrength))  // Use this if you use to want forcestrenght
        .force("center", d3.forceCenter(width / 0.9, height / 0.8));
        //.force("collide", d3.forceCollide(5).iterations(10));  // FOr overlap

        //add encompassing group for the zoom 
        var g = svg.append("g")
            .attr("class", "everything")
            .attr("transform", "scale(0.5)");



        d3.json("https://gist.githubusercontent.com/acmbo/b49be7beef592e8b6088225375db54c2/raw/255d88a91965b1415d950132aeb093f597260f01/graph", function(error, graph) {
            if (error) throw error;

            var link = g.append("g")
                .attr("class", "links")
                .selectAll("line")
                .data(graph.links)
                .enter().append("line")
                .attr("class", "link")
                .attr("stroke-width", function(d) { return Math.sqrt(d.value); });
            
            var node = g.append("g")
                .attr("class", "nodes")
                .selectAll("g")
                .data(graph.nodes)
                .enter().append("g")
            



            // Add degree 
            //https://jsfiddle.net/gilsha/ztp9bqj8/2/
            //https://bl.ocks.org/BTKY/6c282b65246f8f46bb55aadc322db709


            // NOde degree end

            //var circles = node.append("circle")
                //.attr("r", 5) // Without variable radius
            //    .attr("r", function(d) { return radius(d.value / 2); })
             //   .attr("fill", function(d) { return color(d.group); });
            console.log(graph.links)
            node.append('circle')
             .attr("r", function(d) { return radius(d.value / 2); })
             .attr("fill", function(d) { return color(d.group); })
        
            // Create a drag handler and append it to the node object instead
            /*var drag_handler = d3.drag()
            .on("start", dragstarted)
            .on("drag", dragged)
            .on("end", dragended);

            drag_handler(node);
            */

            //add zoom capabilities 
            var zoom_handler = d3.zoom()
                .on("zoom", zoom_actions);

            zoom_handler(svg);

            var lables = node.append("text")
                .text(function(d) {
                return d.id;
                })
                .style("font-size", "8px")
                .attr('x', 6)
                .attr('y', 3);

            node.append("title")
                .text(function(d) { return d.id; });

            simulation
                .nodes(graph.nodes)
                .on("tick", ticked);

            simulation.force("link")
                .links(graph.links);

            function ticked() {
            link
                .attr("x1", function(d) { return d.source.x; })
                .attr("y1", function(d) { return d.source.y; })
                .attr("x2", function(d) { return d.target.x; })
                .attr("y2", function(d) { return d.target.y; });

            node
                .attr("transform", function(d) {
                return "translate(" + d.x + "," + d.y + ")";
                })
            }
        });



        function dragstarted(d) {
        if (!d3.event.active) simulation.alphaTarget(0.3).restart();
                d.fx = d.x;
                d.fy = d.y;
            }

        function dragged(d) {
                d.fx = d3.event.x;
                d.fy = d3.event.y;
            }

        function dragended(d) {
            if (!d3.event.active) simulation.alphaTarget(0);
                d.fx = null;
                d.fy = null;
            }

        //Zoom functions 
        function zoom_actions(){
                g.attr("transform", d3.event.transform)
            }

