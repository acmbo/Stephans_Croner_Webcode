   var svg = d3.select("#dataviz_spec_kwgraph_svg"),
        //width = +svg.attr("width"),
        //height = +svg.attr("height");
        width = window.innerWidth < 960 ? window.innerWidth - 20 : 920
        height = 600

    
    var color = d3.scaleOrdinal(d3.schemeCategory20);
    
    var simulation = d3.forceSimulation()
        .force("link", d3.forceLink().id(function(d) { return d.id; }))
        .force("charge", d3.forceManyBody())
        .force("center", d3.forceCenter(width / 2, height / 2));
    d3.json("https://gist.githubusercontent.com/abkunal/98d35b9b235312e90f3e43c9f7b6932b/raw/d5589ddd53731ae8eec7abd091320df91cdcf5cd/miserables.json", function(error, graph) {
        console.log(graph)
    } ),
    d3.json("https://gist.githubusercontent.com/abkunal/98d35b9b235312e90f3e43c9f7b6932b/raw/d5589ddd53731ae8eec7abd091320df91cdcf5cd/miserables.json", function(error, graph) {
      if (error) throw error;
    
      var link = svg.append("g")
        .attr("class", "links")
        .selectAll("line")
        .data(graph.links)
        .enter().append("line")
          .attr("stroke-width", function(d) { return Math.sqrt(d.value); });
    
      var node = svg.append("g")
          .attr("class", "nodes")
        .selectAll("g")
        .data(graph.nodes)
        .enter().append("g")
    
      var circles = node.append("circle")
        .attr("r", 5)
        .attr("fill", function(d) { return color(d.group); });
    
      // Create a drag handler and append it to the node object instead
      var drag_handler = d3.drag()
          .on("start", dragstarted)
          .on("drag", dragged)
          .on("end", dragended);
    
      drag_handler(node);
      
      var lables = node.append("text")
          .text(function(d) {
            return d.id;
          })
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
    

    window.addEventListener('resize', function () {
        
    
    var svg = d3.select("#dataviz_spec_kwgraph_svg"),
        //width = +svg.attr("width"),
        //height = +svg.attr("height");
        width = window.innerWidth < 960 ? window.innerWidth - 40 : 920
        height = 600

    svg.selectAll("*").remove();
    var color = d3.scaleOrdinal(d3.schemeCategory20);
    
    var simulation = d3.forceSimulation()
        .force("link", d3.forceLink().id(function(d) { return d.id; }))
        .force("charge", d3.forceManyBody())
        .force("center", d3.forceCenter(width / 2, height / 2));
    d3.json("https://gist.githubusercontent.com/abkunal/98d35b9b235312e90f3e43c9f7b6932b/raw/d5589ddd53731ae8eec7abd091320df91cdcf5cd/miserables.json", function(error, graph) {
        console.log(graph)
    } ),
    d3.json("https://gist.githubusercontent.com/abkunal/98d35b9b235312e90f3e43c9f7b6932b/raw/d5589ddd53731ae8eec7abd091320df91cdcf5cd/miserables.json", function(error, graph) {
      if (error) throw error;
    
      var link = svg.append("g")
        .attr("class", "links")
        .selectAll("line")
        .data(graph.links)
        .enter().append("line")
          .attr("stroke-width", function(d) { return Math.sqrt(d.value); });
    
      var node = svg.append("g")
          .attr("class", "nodes")
        .selectAll("g")
        .data(graph.nodes)
        .enter().append("g")
    
      var circles = node.append("circle")
        .attr("r", 5)
        .attr("fill", function(d) { return color(d.group); });
    
      // Create a drag handler and append it to the node object instead
      var drag_handler = d3.drag()
          .on("start", dragstarted)
          .on("drag", dragged)
          .on("end", dragended);
    
      drag_handler(node);
      
      var lables = node.append("text")
          .text(function(d) {
            return d.id;
          })
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


            });