const spec = "scripts/step.vg.json";
vegaEmbed("#my_dataviz", spec)
// result.view provides access to the Vega View API
.then(result => console.log(result))
.catch(console.warn);